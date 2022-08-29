CC=g++
CFLAGS=-Wall -Werror -Wextra
LIBNAME=header_processor
APPNAME=test-app

$(APPNAME): lib$(LIBNAME).so $(APPNAME).cpp
	$(CC) $(CFLAGS) -c -o $(APPNAME).o $(APPNAME).cpp
	$(CC) -L. -l$(LIBNAME) -o $(APPNAME) $(APPNAME).o -Wl,-rpath,.

lib$(LIBNAME).so: $(LIBNAME).cpp
	$(CC) -fPIC $(CFLAGS) $(LIBNAME).cpp -shared -o lib$(LIBNAME).so

cffi: lib$(LIBNAME).so
	python cffi_build.py
	rm -f cffi_libexample.cpp

clean:
	$(RM) -f *.o *.so $(APPNAME)
