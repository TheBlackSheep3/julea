#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "header_processor.h"

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

int get_include_dirs(char** include_dirs, int* include_dirs_length_ptr, char const* const* flags, int flags_length)
{
	int added_item_count = 0;
	for (int i = 0; i < flags_length; ++i)
	{
		if (strncmp("-I", flags[i], 2) == 0) // compare first 2 characters
		{
			include_dirs[added_item_count] = (char*)malloc(sizeof(char)*strlen(flags[i])-1); // +1 for null character and -2 for missing "-I"
			strcpy(include_dirs[added_item_count], flags[i]+2);
			++added_item_count;
		}
	}
	*include_dirs_length_ptr = added_item_count;
	return 0;
}
