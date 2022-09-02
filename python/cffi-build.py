import cffi
import os
import header_processor as hp

ffi = cffi.FFI()
os.system("gcc -E -P -D'__attribute__(ARGS)=' -D'__restrict=' -D'__asm__(x)=' -D'__builtin_va_list=char*' -D'__extension__=' /home/user/julea/include/julea-kv.h $(pkg-config --cflags glib-2.0 julea julea-object julea-kv julea-db) -o header.h")
header_content = ""
with open("header.h") as header:
    for line in header:
        if line.startswith("#pragma GCC diagnostic"):
            continue
        header_content += line
includes = hp.get_additional_compiler_flags(["glib-2.0", "julea", "julea-object", "julea-kv", "julea-db"])
include_dirs = hp.get_include_dirs(includes)
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
