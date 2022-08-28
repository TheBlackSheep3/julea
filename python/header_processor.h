#pragma once
#include <stdbool.h>

int read_header_file(char* content, char const* path, char const* const* include_dirs, bool debug);
int get_additional_compiler_flags(char* flags, char const* const* libraries, bool remove_sanitize);
int get_include_dirs(char** include_dirs, int* include_dirs_length_ptr, char const* const* flags, int flags_length);
