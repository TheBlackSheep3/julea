import cffi
import os
import header_processor as hp

excluded_words = [ "" ]
ffi = cffi.FFI()
#with open(headerfile) as h_file:
#    hellois_comment = False
#    header_content = ""
#    for line in h_file:
#        if not is_comment and "/**" in line:
#            is_comment = True
#            continue
#        if is_comment and "**/" not in line:
#            continue
#        if is_comment and "**/" in line:
#            is_comment = False
#            continue
#        if any(directive in line for directive in excluded_words):
#            continue
#        header_content += line
#    ffi.cdef(header_content)
includes = hp.get_additional_compiler_flags(["glib-2.0", "julea", "julea-object", "julea-kv", "julea-db"])
dirs = hp.get_include_dirs(includes)
header_content = hp.read_header_file("/home/urz/diessner/julea/include/julea-kv.h", dirs)
with open("out.h", "w") as file:
    file.write(header_content)
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
