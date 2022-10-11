CFLAGS := -std=c11 -Wall -Wextra -Wpedantic -Og $(shell pkg-config --cflags glib-2.0 julea julea-object julea-kv julea-db)
LDLIBS := $(shell pkg-config --libs glib-2.0 julea julea-object julea-kv julea-db)

BIN = retrieve

all: $(BIN)

clean:
	rm -f $(BIN)
