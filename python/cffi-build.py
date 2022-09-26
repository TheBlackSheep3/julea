import cffi
from struct import calcsize
import re
import os
import header_processor as hp

ffi = cffi.FFI()

def create_header(filename):
    content = """typedef int gint;
typedef unsigned int guint;
typedef gint gboolean;
typedef char gchar;

typedef unsigned short guint16;
typedef signed int gint32;
typedef unsigned int guint32;
typedef signed long gint64;
typedef unsigned long guint64;

typedef void* gpointer;
typedef const void *gconstpointer;

typedef unsigned long gsize;

typedef guint32 GQuark;

typedef struct _GError GError;
struct _GError
{
    GQuark  domain;
    gint    code;
    gchar  *message;
};

typedef	struct _GModule GModule;

typedef struct _GInputStream GInputStream;
typedef struct _GOutputStream GOutputStream;

typedef struct _GKeyFile GKeyFile;

typedef struct _GSocketConnection GSocketConnection;

typedef void (*GDestroyNotify) (gpointer data);

typedef struct _bson_t
{
    uint32_t    flags;
    uint32_t    len;
    uint8_t     padding[120];
} bson_t;

#include <julea-kv.h>
"""
    with open(filename, "w") as file:
        file.write(content)


def collect_julea(filename, debug = False):
    temp_filename = "temp.h"
    create_header(temp_filename)
    includes = hp.get_additional_compiler_flags(["julea", "julea-object", "julea-kv", "julea-db", "julea-item"])
    flags = list(filter(lambda entry: not "dependencies" in entry, includes))
    # create dummy headers for files intentionally not included
    with open("glib.h", "w") as file:
        file.write("")
    with open("gmodule.h", "w") as file:
        file.write("")
    with open("bson.h", "w") as file:
        file.write("")
    os.system("mkdir -p gio")
    with open("gio/gio.h", "w") as file:
        file.write("")
    # list of macros to be ignored
    macros = [
            "-D'G_DEFINE_AUTOPTR_CLEANUP_FUNC(x, y)='",
            "-D'G_END_DECLS='",
            "-D'G_BEGIN_DECLS='",
            "-D'G_GNUC_WARN_UNUSED_RESULT='",
            "-D'G_GNUC_PRINTF(x, y)='"
            ]
    # let preprocessor collect all declarations
    os.system("gcc -E -P {macros} {file} -I. {include_flags} -o {output}".format(file=temp_filename, include_flags=' '.join(flags), output=filename, macros=' '.join(macros)))
    # remove temporary files needed to please the preprocessor
    os.system("rm -rf glib.h gmodule.h bson.h gio {file}".format(file=temp_filename))

def prepare(filename):
    os.system("gcc -E -P -D'__inline=' -D'__inline__=' -D'__attribute__(ARGS)=' -D'__restrict=' -D'__asm__(x)=' -D'__builtin_va_list=char*' -D'__extension__=' /home/user/julea/include/julea-kv.h $(pkg-config --cflags glib-2.0 julea julea-object julea-kv julea-db) -o header.h")
    header_content = ""
    with open("header.h") as header:
        for line in header:
            if line.startswith("#pragma GCC diagnostic"):
                continue
            header_content += line
    header_content = re.sub(r"static\s+(inline\s+)?(?P<signature>\w+\s*\**\s*\s+\w+\s+(\([\w\s,*]*\)))\s*{[^{}]*({[^{}]*})*[^{}]*}", r"\g<signature>;", header_content)
    header_content = header_content.replace("sizeof (unsigned long int)", str(calcsize('L')))
    header_content = header_content.replace("(int) sizeof (__fd_mask)", str(calcsize('l')))
    header_content = header_content.replace("sizeof (int)", str(calcsize('i')))
    header_content = header_content.replace("~(G_LOG_FLAG_RECURSION | G_LOG_FLAG_FATAL)", "-4")
    header_content = header_content.replace("sizeof (__cpu_mask)", str(calcsize('L')))
    header_content = header_content.replace("sizeof (void *)", str(calcsize('P')))
    header_content = header_content.replace("sizeof (size_t)", str(calcsize('L')))
    header_content = header_content.replace("_ISupper = ((0) < 8 ? ((1 << (0)) << 8) : ((1 << (0)) >> 8))", "_ISupper = 256")
    header_content = header_content.replace("_ISlower = ((1) < 8 ? ((1 << (1)) << 8) : ((1 << (1)) >> 8))", "_ISlower = 512")
    header_content = header_content.replace("_ISalpha = ((2) < 8 ? ((1 << (2)) << 8) : ((1 << (2)) >> 8))", "_ISalpha = 1024")
    header_content = header_content.replace("_ISdigit = ((3) < 8 ? ((1 << (3)) << 8) : ((1 << (3)) >> 8))", "_ISdigit = 2048")
    header_content = header_content.replace("_ISxdigit = ((4) < 8 ? ((1 << (4)) << 8) : ((1 << (4)) >> 8))", "_ISxdigit = 4096")
    header_content = header_content.replace("_ISspace = ((5) < 8 ? ((1 << (5)) << 8) : ((1 << (5)) >> 8))", "_ISspace = 8192")
    header_content = header_content.replace("_ISprint = ((6) < 8 ? ((1 << (6)) << 8) : ((1 << (6)) >> 8))", "_ISprint = 16384")
    header_content = header_content.replace("_ISgraph = ((7) < 8 ? ((1 << (7)) << 8) : ((1 << (7)) >> 8))", "_ISgraph = 32768")
    header_content = header_content.replace("_ISblank = ((8) < 8 ? ((1 << (8)) << 8) : ((1 << (8)) >> 8))", "_ISblank = 1")
    header_content = header_content.replace("_IScntrl = ((9) < 8 ? ((1 << (9)) << 8) : ((1 << (9)) >> 8))", "_IScntrl = 2")
    header_content = header_content.replace("_ISpunct = ((10) < 8 ? ((1 << (10)) << 8) : ((1 << (10)) >> 8))", "_ISpunct = 4")
    header_content = header_content.replace("_ISalnum = ((11) < 8 ? ((1 << (11)) << 8) : ((1 << (11)) >> 8))", "_ISalnum = 8")
    with open(filename, "w") as file:
        file.write(header_content)

def test(filename, debug=False):
    with open(filename, "r") as file:
        header_content = file.read()
    includes = hp.get_additional_compiler_flags(["glib-2.0", "julea", "julea-object", "julea-kv", "julea-db"], remove_sanitize=False)
    include_dirs = hp.get_include_dirs(includes)
    ffi.cdef(header_content, override=True)
    ffi.set_source(
            "julea_kv",
            """
                #include "julea-kv.h"
            """,
            libraries=["julea", "julea-object", "julea-kv", "julea-db", "kv-null"],
            include_dirs=include_dirs,
            library_dirs=["/home/user/julea/bld"],
            extra_compile_args=includes,
            extra_link_args=["-fsanitize=address", "-static-libasan", "-Wl,-rpath,."]
            )
    ffi.compile(verbose=debug)
    if not debug:
        os.system("rm -f {file}".format(file=filename))

def alt():
    os.system("gcc -E -P -DJULEA_KV_COMPILATION -D'__inline=' -D'__inline__=' -D'__attribute__(ARGS)=' -D'__restrict=' -D'__asm__(x)=' -D'__builtin_va_list=char*' -D'__extension__=' /home/user/julea/include/julea-kv.h $(pkg-config --cflags glib-2.0 julea julea-object julea-kv julea-db) -o header.h")
    os.system("gcc -E -P -DJULEA_KV_COMPILATION -D'__inline=' -D'__inline__=' -D'__attribute__(ARGS)=' -D'__restrict=' -D'__asm__(x)=' -D'__builtin_va_list=char*' -D'__extension__=' /home/user/julea/lib/kv/jkv.c $(pkg-config --cflags glib-2.0 julea julea-object julea-kv julea-db) -o jkv_pre.c")
    os.system("gcc -E -P -DJULEA_KV_COMPILATION -D'__inline=' -D'__inline__=' -D'__attribute__(ARGS)=' -D'__restrict=' -D'__asm__(x)=' -D'__builtin_va_list=char*' -D'__extension__=' /home/user/julea/lib/kv/jkv-iterator.c $(pkg-config --cflags glib-2.0 julea julea-object julea-kv julea-db) -o jkv-iterator_pre.c")
    os.system("gcc -E -P -DJULEA_KV_COMPILATION -D'__inline=' -D'__inline__=' -D'__attribute__(ARGS)=' -D'__restrict=' -D'__asm__(x)=' -D'__builtin_va_list=char*' -D'__extension__=' /home/user/julea/lib/kv/jkv-uri.c $(pkg-config --cflags glib-2.0 julea julea-object julea-kv julea-db) -o jkv-uri_pre.c")
    includes = open("header.h").read()
    source = open("jkv_pre.c").read()
    source += open("jkv-iterator_pre.c").read()
    source += open("jkv-uri_pre.c").read()

    ffi.cdef(includes)
    ffi.set_source("julea_kv", source, libraries=["julea-kv", "julea"], include_dirs=["/home/user/julea/include"])
    ffi.compile(verbose=True)

if __name__ == "__main__":
    filename = "test-header.h"
    debug = True
    collect_julea(filename, debug)
    test(filename, debug)
