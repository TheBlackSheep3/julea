CC=gcc
CFLAGS=-Wall -Werror -Wextra
LIBNAME=header_processor
APPNAME=test-app

$(APPNAME): lib$(LIBNAME).so $(APPNAME).c
	$(CC) $(CFLAGS) -c -o $(APPNAME).o $(APPNAME).c
	$(CC) -L. -l$(LIBNAME) -o $(APPNAME) $(APPNAME).o -Wl,-rpath,.

lib$(LIBNAME).so: $(LIBNAME).c
	$(CC) -fPIC $(CFLAGS) $(LIBNAME).c -shared -o lib$(LIBNAME).so

cffi: lib$(LIBNAME).so
	python cffi_build.py
	rm -f cffi_libexample.c

clean:
	$(RM) -f *.o *.so $(APPNAME)
