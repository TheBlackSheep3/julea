from julea import JKV, JObject, JDB, JBatch, JBatchResult, encode, NULL
from cffi import FFI

if __name__ == "__main__":
    try:
        ffi = FFI()
        value = "Hello World!"

        result = JBatchResult()
        hello = encode("hello")
        world = encode("world")
        _object = JObject.j_object_new(hello, world)
        kv = JKV.j_kv_new(hello, world)
        schema = JDB.j_db_schema_new(hello, world, NULL)
        JDB.j_db_schema_add_field(schema, hello, JDB.J_DB_TYPE_STRING, NULL)
        entry = JDB.j_db_entry_new(schema, NULL)

        JDB.j_db_entry_set_field(entry, hello, encode(value), len(value) + 1, NULL)
        with JBatch(result) as batch:
            JObject.j_object_create(_object, batch)
            JObject.j_object_write(_object, encode(value), len(value) + 1, 0, ??, batch)
            JKV.j_kv_put(kv, encode(value), len(value) + 1, NULL, batch)
            JDB.j_db_schema_create(schema, batch, NULL)
            JDB.j_db_entry_insert(entry, batch, NULL)

        if result.IsSuccess:
            result = JBatchResult()
            with JBatch(result) as batch:
                JObject.j_object_read(_object, ?buffer?, 128, 0, ??, batch)
            if result.IsSuccess:
                print("Object contains: '{value}' ({length} bytes)".format(value=read_from_buffer(??), ??))

            result = JBatchResult()
            with JBatch(result) as batch:
                ptr = get_void_ptr_ptr()
                length = get_uint_ptr()
                JKV.j_kv_get(kv, ptr, length, batch)
            if result.IsSuccess:
                print("KV contains: '{value}' ({length} bytes)".format(value=read_from_buffer(ptr), length=length[0]))

            try:
                selector = JDB.j_db_selector_new(schema, JDB.J_DB_SELECTOR_MODE_AND, NULL)
                j_db_selector_add_field(selector, hello, JDB.J_DB_SELECTOR_OPERATOR_EQ, encode(value), len(value) + 1, NULL)
                iterator = JDB.j_db_iterator_new(schema, selector, NULL)
                
                while JDB.j_db_iterator_next(iterator, NULL):
                    _type = ffi.new("JDBType *")
                    JDB.j_db_iterator_get_field(iterator, hello, _type[0], ??, ??, NULL)
                    print("DB contains: '{value}' ({length} bytes".format(value=read_from_buffer(??), ??))

            finally:
                JDB.j_db_selector_unref(selector)
                JDB.j_db_iterator_unref(iterator)

    finally:
        JKV.j_kv_unref(kv)
        JObject.j_object_unref(_object)
        JDB.j_db_schema_unref(schema)
        JDB.j_db_entry_unref(entry)
