from os import system
from build_helper import build

if __name__ == "__main__":
    build("julea_object", ["julea", "julea-object"])
    build("julea_kv", ["julea", "julea-kv"])
