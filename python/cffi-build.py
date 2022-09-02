import cffi
import os

ffi = cffi.FFI()
os.system("gcc -E -P -D'__attribute__(ARGS)=' /home/user/julea/include/julea-kv.h $(pkg-config --cflags glib-2.0 julea julea-object julea-kv julea-db) -o header.h")
with open("header.h") as header:
    header_content = header.read()
ffi.cdef(header_content)
ffi.set_source(
        "julea_kv",
        '#include "include/julea-kv.h"',
        libraries=["julea-kv", "julea"],
        library_dirs=["bld"],
        extra_compile_args=includes,
        extra_link_args=["-Wl,-rpath,."]
)
ffi.compile(verbose=True)
