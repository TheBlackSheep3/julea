import cffi
import os
import header_processor as hp

excluded_words = [ "" ]
ffi = cffi.FFI()
headerfile = "test.h"
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
ffi.set_source(
        "julea_kv",
        '#include "include/julea-kv.h"',
        libraries=["julea-kv", "julea"],
        library_dirs=["bld"],
        extra_compile_args=includes,
        extra_link_args=["-Wl,-rpath,."]
)
ffi.compile(verbose=True)
