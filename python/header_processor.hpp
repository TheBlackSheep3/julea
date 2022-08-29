#pragma once
#include <vector>
#include <string>

//int read_header_file(char* content, char const* path, char const* const* include_dirs, bool debug);
//int get_additional_compiler_flags(char* flags, char const* const* libraries, bool remove_sanitize);
std::vector<std::string> get_include_dirs(std::vector<std::string> flags);
