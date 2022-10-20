CFLAGS := -std=c11 -Wall -Wextra -Wpedantic -Og $(shell pkg-config --cflags glib-2.0 julea julea-object julea-kv julea-db)
LDLIBS := $(shell pkg-config --libs glib-2.0 julea julea-object julea-kv julea-db)

READ = read
WRITE = write
CLEANUP = cleanup_checker

all: $(READ) $(WRITE) $(CLEANUP)

run: all
	../../scripts/setup.sh start
	./write
	python write.py
	echo done writing
	./read
	python read.py
	echo done reading
	./cleanup_checker
	../../scripts/setup.sh stop

clean:
	rm -f $(READ) $(WRITE) $(CLEANUP)
