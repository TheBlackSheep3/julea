#pragma once
#include <vector>
#include <string>
#include <tuple>

std::vector<std::string> get_include_dirs(std::vector<std::string> flags);
std::vector<std::string> get_additional_compiler_flags(std::vector<std::string> libraries);
//std::string read_header_file(std::string file_path, std::vector<std::string> include_dirs, bool debug);
std::tuple<bool, std::string> is_include(std::string line);
