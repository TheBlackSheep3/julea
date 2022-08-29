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
