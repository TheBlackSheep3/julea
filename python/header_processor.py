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

def read_header_file(path, include_dirs=[], debug=False):
    include_dirs.insert(0, ".") # search first in current directory
    filename = get_filename_from_path(path)
    included_files = [ filename ]
    return read_header_file_internal(path, include_dirs, included_files, debug)

def get_filename_from_path(path):
    match_result = re.search(r"\/([\w-]+\/)*([\w-]+\.h)", path)
    if match_result != None:
        return match_result.group(2)
    return ""


def read_header_file_internal(path, include_dirs=[], included_files=[], debug=False):
    content = ""
    if debug:
        debug_print(' '.join(include_dirs))
    with open(path) as header:
        for line in header:
            if debug:
                debug_print(line.strip('\n'))
            is_include_line, filename = is_include(line)
            if is_include_line:
                if debug:
                    debug_print("is include line")
                if filename in included_files:
                    continue
                for directory in include_dirs:
                    path = os.path.join(directory, filename)
                    if os.path.exists(path):
                        included_files.append(filename)
                        if debug:
                            debug_print("found file {file}".format(file=path))
                        content += read_header_file(path, include_dirs, debug)
                        break;
                if debug:
                    debug_print("could not find {file}".format(file=filename))
                continue
            if is_compiler_directive(line):
                if debug:
                    debug_print("is compiler directive")
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

def debug_print(output):
    print("debug: {line}".format(line=output))

if __name__ == "__main__":
    includes = get_additional_compiler_flags(["glib-2.0", "julea", "julea-object", "julea-kv", "julea-db"])
    dirs = get_include_dirs(includes)
    print(dirs)
    content = read_header_file("/home/urz/diessner/julea/include/julea-kv.h", dirs)
    #print(content)
