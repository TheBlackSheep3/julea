import cffi
import os

excluded_words = [ "" ]
ffi = cffi.FFI()
headerfile = "test.h"
with open(headerfile) as h_file:
    is_comment = False
    header_content = ""
    for line in h_file:
        if not is_comment and "/**" in line:
            is_comment = True
            continue
        if is_comment and "**/" not in line:
            continue
        if is_comment and "**/" in line:
            is_comment = False
            continue
        if any(directive in line for directive in excluded_words):
            continue
        header_content += line
    ffi.cdef(header_content)
include_buffer = os.popen('pkg-config --cflags glib-2.0 julea julea-object julea-kv julea-db')
includes = include_buffer.read().strip().split(' ')
# remove duplicate parameters
includes = [*set(includes)]
includes.remove("-fsanitize=address,undefined")
ffi.set_source(
        "julea_kv",
        '#include "include/julea-kv.h"',
        libraries=["julea-kv", "julea"],
        library_dirs=["bld"],
        extra_compile_args=includes,
        extra_link_args=["-Wl,-rpath,."]
)
ffi.compile(verbose=True)
