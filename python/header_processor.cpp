#include <vector>
#include <string>
#include "header_processor.hpp"

//int read_header_file(char* content, char const* path, char const* const* include_dirs, bool debug)
//{
//	FILE* file_pointer = fopen(path, "r");
//	if (file_pointer == NULL)
//	{
//
//	}
//	fclose(file_pointer);
//	return 0;
//}
//
//
//int get_additional_compiler_flags(char* flags, char const* const* libraries, bool remove_sanitize)
//{
//	return 0;
//}

#include <cstdio>
#include <iostream>
#include <memory>
#include <stdexcept>
#include <array>
#include <set>

std::string exec(const char* cmd) {
    std::array<char, 128> buffer;
    std::string result;
    std::unique_ptr<FILE, decltype(&pclose)> pipe(popen(cmd, "r"), pclose);
    if (!pipe) {
        throw std::runtime_error("popen() failed!");
    }
    while (fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr) {
        result += buffer.data();
    }
    return result;
}

std::vector<std::string> splitstr(std::string str, std::string deli = " ")
{
	int start = 0;
	int end = str.find(deli);
	auto result = std::vector<std::string>();
	while (end != -1) {
	    result.push_back(str.substr(start, end - start));
	    start = end + deli.size();
	    end = str.find(deli, start);
	}
	result.push_back(str.substr(start, end - start));
	return result;
}

std::vector<std::string> get_additional_compiler_flags(std::vector<std::string> libraries)
{
	std::string command = "pkg-config --cflags";
	for (std::string lib_name : libraries)
	{
		command.append(" ");
		command.append(lib_name);
	}
	auto command_result = exec(command.c_str());
	auto result = splitstr(command_result);
	// remove duplicates
	std::set<std::string> set(result.begin(), result.end());
	result.assign(set.begin(), set.end());
	return result;
}

std::vector<std::string> get_include_dirs(std::vector<std::string> flags)
{
	int flags_length = flags.size();
	auto includes = std::vector<std::string>();
	for (int i = 0; i < flags_length; ++i)
	{
		if (flags[i].compare(0, 2, "-I") == 0) // starts with "-I"
		{
			includes.push_back(flags[i].substr(2));
		}
	}
	return includes;
}
