import os
import re

def get_additional_compiler_flags(libraries, remove_sanitize=True):
    flags_buffer = os.popen("pkg-config --cflags {libs}".format(libs=' '.join(libraries)))
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

def read_header_file(path, include_dirs=["."]):
    content = ""
    with open(path) as header:
        for line in header:
            is_include_line, filename = is_include(line)
            if is_include_line:
                print("TODO include {file}".format(file=filename))
                continue
            if is_compiler_directive(line):
                continue
            content += line
        return content

def is_compiler_directive(line):
    return line.startswith('#')

def is_include(line):
    match_result = re.search(r"#include\s+(<(([\w-]+\/)*[\w-]+\.h)>|\"(([\w-]+\/)*[\w-]+\.h)\")", line)
    if match_result == None:
        return False, ""
    filename = match_result.group(2)
    if filename != None:
        return True, filename
    filename = match_result.group(4)
    if filename != None:
        return True, filename
    # this should never need to be called
    return False, ""

if __name__ == "__main__":
    file = "../include/julea-kv.h"
    #file = "tester.h"
    content = read_header_file(file)
    print(20*'*'+2*'\n'+"content is"+2*'\n'+content)
