import cffi
import re
import os
import header_processor as hp

ffi = cffi.FFI()

def prepare():
    os.system("gcc -E -P -D'__inline=' -D'__inline__=' -D'__attribute__(ARGS)=' -D'__restrict=' -D'__asm__(x)=' -D'__builtin_va_list=char*' -D'__extension__=' /home/user/julea/include/julea-kv.h $(pkg-config --cflags glib-2.0 julea julea-object julea-kv julea-db) -o header.h")
    header_content = ""
    with open("header.h") as header:
        for line in header:
            if line.startswith("#pragma GCC diagnostic"):
                continue
            header_content += line
    header_content = re.sub(r"static\s+(inline\s+)?(?P<signature>\w+\s*\**\s*\s+\w+\s+(\([\w\s,*]*\)))\s*{[^{}]*({[^{}]*})*[^{}]*}", r"\g<signature>;", header_content)
    header_content = header_content.replace("sizeof (unsigned long int)", "4")
    header_content = header_content.replace("(int) sizeof (__fd_mask)", "4")
    header_content = header_content.replace("sizeof (int)", "4")
    header_content = header_content.replace("~(G_LOG_FLAG_RECURSION | G_LOG_FLAG_FATAL)", "-4")
    with open("header_strip.h", "w") as file:
        file.write(header_content)

def test():
    with open("header_strip.h", "r") as file:
        header_content = file.read()
    includes = hp.get_additional_compiler_flags(["glib-2.0", "julea", "julea-object", "julea-kv", "julea-db"])
    include_dirs = hp.get_include_dirs(includes)
    ffi.cdef(header_content, override=True)
    ffi.set_source(
            "julea_kv",
            """
                #include "julea-kv.h"
                #include "julea.h"
            """,
            libraries=["julea-kv", "julea"],
            include_dirs=include_dirs,
            library_dirs=["bld"],
            extra_compile_args=includes,
            extra_link_args=["-Wl,-rpath,."]
            )
    ffi.compile(verbose=True)

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
    prepare()
    test()
