CFLAGS := -std=c11 -Wall -Wextra -Wpedantic -Og $(shell pkg-config --cflags glib-2.0 julea julea-object julea-kv julea-db)
LDLIBS := $(shell pkg-config --libs glib-2.0 julea julea-object julea-kv julea-db)

run:
	../../scripts/setup.sh start
	python hello-world.py
	../../scripts/setup.sh stop

check: checker
	../../scripts/setup.sh start
	./checker
	../../scripts/setup.sh stop

write: writer
	../../scripts/setup.sh start
	./writer
	../../scripts/setup.sh stop

check-py:
	../../scripts/setup.sh start
	python read.py
	../../scripts/setup.sh stop

clean:
	$(RM) checker write
	../../scripts/setup.sh stop
	../../scripts/setup.sh clean
