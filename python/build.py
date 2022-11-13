from build_helper import build, copy_main_module

if __name__ == "__main__":
    build("julea_core", "julea", ["julea"])
    build("julea_object", "julea-object", ["julea", "julea-object"])
    build("julea_kv", "julea-kv", ["julea", "julea-kv"])
    build("julea_db", "julea-db", ["julea", "julea-db"])
    build("julea_item", "julea-item", ["julea", "julea-item"])
    copy_main_module()
