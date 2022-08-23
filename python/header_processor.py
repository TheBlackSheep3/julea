import os

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

if __name__ == "__main__":
    libs = ["glib-2.0", "julea", "julea-object", "julea-kv", "julea-db"]
    flags = get_additional_compiler_flags(libs, remove_sanitize=True)
    print(20*'*')
    for str in flags:
        print(str)
    print(20*'*')
    includes = get_include_dirs(flags)
    for str in includes:
        print(str)
