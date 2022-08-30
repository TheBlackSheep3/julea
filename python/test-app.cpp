#include <vector>
#include <string>
#include <iostream>
#include "header_processor.hpp"

int main()
{
	//std::vector<std::string> flags = {
	//	"-I/home/urz/diessner/julea/dependencies/opt/spack/linux-centos8-zen3/gcc-11.2.0/glib-2.72.1-l5vgngsq6g4fyb36ty2kv7rmgvl5cy6m/include/glib-2.0",
	//	"-I/home/urz/diessner/julea/dependencies/opt/spack/linux-centos8-zen3/gcc-11.2.0/glib-2.72.1-l5vgngsq6g4fyb36ty2kv7rmgvl5cy6m/lib/glib-2.0/include",
	//	"-I/home/urz/diessner/julea/dependencies/opt/spack/linux-centos8-zen3/gcc-11.2.0/pcre-8.45-yhkorzhmm3c5kqrpgzvad3ktxx5et6t3/include",
	//	"-I/home/urz/diessner/julea/bld",
	//	"-I/home/urz/diessner/julea",
	//	"-I/home/urz/diessner/julea/bld/include",
	//	"-I/home/urz/diessner/julea/include",
	//	"-I/home/urz/diessner/julea/bld/include/core",
	//	"-I/home/urz/diessner/julea/include/core",
	//	"-I/home/urz/diessner/julea/dependencies/opt/spack/linux-centos8-zen3/gcc-11.2.0/glib-2.72.1-l5vgngsq6g4fyb36ty2kv7rmgvl5cy6m/include",
	//	"-I/home/urz/diessner/julea/dependencies/opt/spack/linux-centos8-zen3/gcc-11.2.0/libffi-3.4.2-dc4iw6aejktwlhpxca6ki3xf5lr6asn6/include",
	//	"-I/home/urz/diessner/julea/dependencies/opt/spack/linux-centos8-zen3/gcc-11.2.0/zlib-1.2.12-sshieq3awkfusca6uo6x46gbswqdbbyn/include",
	//	"-I/home/urz/diessner/julea/dependencies/opt/spack/linux-centos8-zen3/gcc-11.2.0/libbson-1.21.0-pzyeaxrxejpticny4oom7fimu2ncqipi/include/libbson-1.0",
	//	"-I/home/urz/diessner/julea/dependencies/opt/spack/linux-centos8-zen3/gcc-11.2.0/libfabric-1.14.1-vfwmso4ggwx22o2weldw5dtr74t6uuxu/include",
	//	"-fsanitize=address,undefined",
	//	"-fsanitize=address,undefined",
	//	"-fsanitize=address,undefined",
	//	"-pthread"
	//};

	//std::vector<std::string> include_dirs = get_include_dirs(flags);
	//int size = include_dirs.size();
	//if (size > 0)
	//{
	//	for (int i = 0; i < size; ++i)
	//	{
	//		std::cout << include_dirs[i] << std::endl;
	//	}
	//}
	//else
	//{
	//	printf("something went wrong");
	//}

	//std::vector<std::string> libs = {
	//	"glib-2.0",
	//	"julea",
	//	"julea-object",
	//	"julea-kv",
	//	"julea-db"
	//};
	//auto flags = get_additional_compiler_flags(libs);
	//for (auto flag : flags)
	//{
	//	std::cout << flag << std::endl;
	//}
	
	is_include("#include \"header_processor.h\"");
	is_include("#include <vector.h>");

	return 0;
}
