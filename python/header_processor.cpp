#include <vector>
#include <string>
#include <cstdio>
#include <iostream>
#include <memory>
#include <stdexcept>
#include <array>
#include <set>
#include <fstream>
#include <regex>
#include <tuple>
#include "header_processor.hpp"

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

std::tuple<bool, std::string> is_include(std::string line)
{
	std::regex regex("#include\\s+(<(([\\w-]+\\/)*[\\w-]+\\.h)>|\\\"(([\\w-]+\\/)*[\\w-]+\\.h)\\\")");
	std::match_results<std::string::const_iterator> match_result;

	if (!std::regex_search(line, match_result, regex))
	{
		return { false, "" };
	}

	std::string filename = match_result[2];
	if (filename != "")
	{
		return { true, filename };
	}

	filename = match_result[4];
	if (filename != "")
	{
		return { true, filename };
	}

	return { false, "" };
}

bool is_compiler_directive(std::string line)
{
	return line[0] == '#';
}

std::string path_combine(std::string dir, std::string file)
{
	std::string full_path = dir;
	if (full_path.back() != '/')
	{
		full_path.push_back('/');
	}
	return full_path + file;
}

std::string read_header_file(std::string file_path, std::vector<std::string> include_dirs)
{
	std::string content = "";
	std::string line;
	std::ifstream header(file_path);

	if(!header.is_open())
	{
		return "";
	}

	while(getline(header, line))
	{
		auto tuple = is_include(line);
		if (std::get<0>(tuple))
		{
			for (auto dir : include_dirs)
			{
				std::string file_content = read_header_file(path_combine(dir, std::get<1>(tuple)), include_dirs);
				if (file_content != "")
				{
					content += file_content;
					break;
				}
			}
			continue;
		}

		if (is_compiler_directive(line))
		{
			continue;
		}

		content += line + "\n";
	}

	return content;
}