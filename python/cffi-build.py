import cffi
import os

ffi = cffi.FFI()
headerfile = "test.h"
#with open(headerfile) as h_file:
#    ffi.cdef(h_file.read())
include_buffer = os.popen('pkg-config --cflags glib-2.0 julea julea-object julea-kv julea-db')
includes = include_buffer.read().strip().split(' ')
ffi.set_source(
        "julea_kv",
        '#include "include/julea-kv.h"',
        libraries=["julea-kv", "julea"],
        library_dirs=["bld"],
        extra_compile_args=includes,
        extra_link_args=["-Wl,-rpath,."]
)
ffi.compile(verbose=True)
