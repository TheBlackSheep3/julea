from julea import JBatchResult, JBatch, ffi, lib, encode, read_from_buffer, get_void_ptr_ptr, get_uint_ptr

if __name__ == "__main__":
    try:
        value = "Hello World!"

        result = JBatchResult()
        hello = encode("hello")
        world = encode("world")
        nbytes_ptr = ffi.new("unsigned long*")
        _object = lib.j_object_new(hello, world)
        kv = lib.j_kv_new(hello, world)
        schema = lib.j_db_schema_new(hello, world, ffi.NULL)
        lib.j_db_schema_add_field(schema, hello, lib.J_DB_TYPE_STRING, ffi.NULL)
        entry = lib.j_db_entry_new(schema, ffi.NULL)

        lib.j_db_entry_set_field(entry, hello, encode(value), len(value) + 1, ffi.NULL)
        with JBatch(result) as batch:
            #lib.j_object_create(_object, batch)
            #lib.j_object_write(_object, encode(value), len(value) + 1, 0, nbytes_ptr, batch)
            lib.j_kv_put(kv, encode(value), len(value) + 1, ffi.NULL, batch)
            #lib.j_db_schema_create(schema, batch, ffi.NULL)
            #lib.j_db_entry_insert(entry, batch, ffi.NULL)

        if result.IsSuccess:
#            result = JBatchResult()
#            buffer = ffi.new("gchar[]", 128)
#            with JBatch(result) as batch:
#                lib.j_object_read(_object, buffer, 128, 0, nbytes_ptr, batch)
#            if result.IsSuccess:
#                print("Object contains: '{value}' ({length} bytes)".format(value=read_from_buffer(buffer), length=nbytes_ptr[0]))

            result = JBatchResult()
            with JBatch(result) as batch:
                ptr = get_void_ptr_ptr()
                length = get_uint_ptr()
                lib.j_kv_get(kv, ptr, length, batch)
            if result.IsSuccess:
                print("KV contains: '{value}' ({length} bytes)".format(value=read_from_buffer(ptr[0]), length=length[0]))

#            try:
#                selector = lib.j_db_selector_new(schema, lib.J_DB_SELECTOR_MODE_AND, ffi.NULL)
#                j_db_selector_add_field(selector, hello, lib.J_DB_SELECTOR_OPERATOR_EQ, encode(value), len(value) + 1, ffi.NULL)
#                iterator = lib.j_db_iterator_new(schema, selector, ffi.NULL)
#                
#                while lib.j_db_iterator_next(iterator, ffi.NULL):
#                    _type = ffi.new("JDBType *")
#                    db_field_ptr = ffi.new("gchar**")
#                    db_length_ptr = ffi.new("unsigned long*")
#                    lib.j_db_iterator_get_field(iterator, hello, _type[0], db_field_ptr, db_length_ptr, ffi.NULL)
#                    print("DB contains: '{value}' ({length} bytes".format(value=read_from_buffer(db_field_ptr[0]), length=db_length_ptr[0]))
#
#            finally:
#                lib.j_db_selector_unref(selector)
#                lib.j_db_iterator_unref(iterator)

    finally:
        lib.j_kv_unref(kv)
#        lib.j_object_unref(_object)
#        lib.j_db_schema_unref(schema)
#        lib.j_db_entry_unref(entry)
