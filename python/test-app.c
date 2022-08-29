#include <stdio.h>
#include <stdlib.h>
#include "header_processor.h"

int main()
{
	const char* flags[] = {
		"-I/home/urz/diessner/julea/dependencies/opt/spack/linux-centos8-zen3/gcc-11.2.0/glib-2.72.1-l5vgngsq6g4fyb36ty2kv7rmgvl5cy6m/include/glib-2.0",
		"-I/home/urz/diessner/julea/dependencies/opt/spack/linux-centos8-zen3/gcc-11.2.0/glib-2.72.1-l5vgngsq6g4fyb36ty2kv7rmgvl5cy6m/lib/glib-2.0/include",
		"-I/home/urz/diessner/julea/dependencies/opt/spack/linux-centos8-zen3/gcc-11.2.0/pcre-8.45-yhkorzhmm3c5kqrpgzvad3ktxx5et6t3/include",
		"-I/home/urz/diessner/julea/bld",
		"-I/home/urz/diessner/julea",
		"-I/home/urz/diessner/julea/bld/include",
		"-I/home/urz/diessner/julea/include",
		"-I/home/urz/diessner/julea/bld/include/core",
		"-I/home/urz/diessner/julea/include/core",
		"-I/home/urz/diessner/julea/dependencies/opt/spack/linux-centos8-zen3/gcc-11.2.0/glib-2.72.1-l5vgngsq6g4fyb36ty2kv7rmgvl5cy6m/include",
		"-I/home/urz/diessner/julea/dependencies/opt/spack/linux-centos8-zen3/gcc-11.2.0/libffi-3.4.2-dc4iw6aejktwlhpxca6ki3xf5lr6asn6/include",
		"-I/home/urz/diessner/julea/dependencies/opt/spack/linux-centos8-zen3/gcc-11.2.0/zlib-1.2.12-sshieq3awkfusca6uo6x46gbswqdbbyn/include",
		"-I/home/urz/diessner/julea/dependencies/opt/spack/linux-centos8-zen3/gcc-11.2.0/libbson-1.21.0-pzyeaxrxejpticny4oom7fimu2ncqipi/include/libbson-1.0",
		"-I/home/urz/diessner/julea/dependencies/opt/spack/linux-centos8-zen3/gcc-11.2.0/libfabric-1.14.1-vfwmso4ggwx22o2weldw5dtr74t6uuxu/include",
		"-fsanitize=address,undefined",
		"-fsanitize=address,undefined",
		"-fsanitize=address,undefined",
		"-pthread"
	};
	int flags_length = 18;
	char** include_dirs = (char**)malloc(flags_length*sizeof(char**));
	int include_dirs_length = 0;

	if (get_include_dirs(include_dirs, &include_dirs_length, flags, flags_length) == 0)
	{
		for (int i = 0; i < include_dirs_length; ++i)
		{
			printf("%s\n", include_dirs[i]);
		}
	}
	else
	{
		printf("something went wrong");
	}

	return 0;
}
