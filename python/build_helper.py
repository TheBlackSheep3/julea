from os import popen, system
from os.path import dirname
import cffi

def create_header(filename, library):
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

"""
    content+=f"#include <{library}.h>"
    with open(filename, "w") as file:
        file.write(content)

def get_additional_compiler_flags(libraries, remove_sanitize=True):
    flags_buffer = popen("pkg-config --cflags {libs}".format(libs=' '.join(libraries)))
    flags = flags_buffer.read().strip().split(' ')
    # remove duplicate parameters
    flags = [*set(flags)]
    if remove_sanitize:
        for s in flags:
            if "-fsanitize" in s:
                flags.remove(s)
    return flags

def get_include_dirs(flags):
    return [ str.strip("-I") for str in flags if "-I" in str ]

def collect_julea(filename, library, debug = False):
    temp_filename = "temp.h"
    create_header(temp_filename, library)
    includes = get_additional_compiler_flags(["julea", "julea-object", "julea-kv", "julea-db", "julea-item"])
    flags = list(filter(lambda entry: not "dependencies" in entry, includes))
    # create dummy headers for files intentionally not included
    with open("glib.h", "w") as file:
        file.write("")
    with open("gmodule.h", "w") as file:
        file.write("")
    with open("bson.h", "w") as file:
        file.write("")
    system("mkdir -p gio")
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
    system("gcc -E -P {macros} {file} -I. {include_flags} -o {output}".format(file=temp_filename, include_flags=' '.join(flags), output=filename, macros=' '.join(macros)))
    # remove temporary files needed to please the preprocessor
    system("rm -rf glib.h gmodule.h bson.h gio {file}".format(file=temp_filename))

def process(libraryname, libs, tempheader, debug=False):
    ffi = cffi.FFI()
    with open(tempheader, "r") as file:
        header_content = file.read()
    includes = get_additional_compiler_flags(libs+["glib-2.0"], remove_sanitize=True)
    include_dirs = get_include_dirs(includes)
    ffi.cdef(header_content, override=True)
    outdir = "{currentdir}/../bld/".format(currentdir=dirname(__file__))
    ffi.set_source(
            libraryname,
            """
                #include "{libname}.h"
            """.format(libname=libraryname.replace('_', '-')),
            libraries=libs+["kv-null"],
            include_dirs=include_dirs,
            library_dirs=[outdir],
            extra_compile_args=includes,
            extra_link_args=["-Wl,-rpath,."]
            )
    ffi.compile(tmpdir=outdir, verbose=debug)
    if not debug:
        system("rm -f {file} {name}.o {name}.c".format(file=tempheader, name=outdir+libraryname))

def build(library_name, include_libs, debug=False):
    header_name = "header_{base}.h".format(base=library_name)
    collect_julea(header_name, library_name.replace('_','-'), debug)
    process(library_name, include_libs, header_name, debug)
