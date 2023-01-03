from benchmarkrun import BenchmarkRun, append_to_benchmark_list_and_run
from julea import lib, encode, ffi

def benchmark_db_schema(benchmarkrun_list, iterations):
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/schema/create", iterations), benchmark_db_schema_create)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/schema/create-batch", iterations), benchmark_db_schema_create_batch)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/schema/delete", iterations), benchmark_db_schema_delete)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/schema/delete-batch", iterations), benchmark_db_schema_delete_batch)

def benchmark_db_schema_create(run):
    _benchmark_db_schema_create(run, False)

def benchmark_db_schema_create_batch(run):
    _benchmark_db_schema_create(run, True)

def _benchmark_db_schema_create(run, use_batch):
    batch = lib.j_batch_new_for_template(lib.J_SEMANTICS_TEMPLATE_DEFAULT)
    delete_batch = lib.j_batch_new_for_template(lib.J_SEMANTICS_TEMPLATE_DEFAULT)
    run.start_timer()
    for i in range(run.iterations):
        error_ptr = ffi.new("GError*")
        name = encode(f"benchmark-schema-{i}")
        namespace = encode("benchmark-ns")
        schema = lib.j_db_schema_new(namespace, name, error_ptr)
        for j in range(10):
            fname = encode("field{j}")
            lib.j_db_schema_add_field(schema, fname, lib.J_DB_TYPE_STRING,
                                      error_ptr)
        j_db_schema_create(schema, batch, ffi.NULL)
        j_db_schema_delete(schema, delete_batch, ffi.NULL)
        if not use_batch:
            assert lib.j_batch_execute(batch)
        lib.j_db_schema_unref(schema)
    if use_batch:
        assert lib.j_batch_execute(batch)
    run.stop_timer()
    assert lib.j_batch_execute(delete_batch)
    lib.j_batch_unref(batch)
    lib.j_batch_unref(delete_batch)

def benchmark_db_schema_delete(run):
    _benchmark_db_schema_delete(run, False)

def benchmark_db_schema_delete_batch(run):
    _benchmark_db_schema_delete(run, True)

def _benchmark_db_schema_delete(run, use_batch):
    batch = lib.j_batch_new_for_template(lib.J_SEMANTICS_TEMPLATE_DEFAULT)
    for i in range(run.iterations):
        name = encode(f"benchmark-schema-{i}")
        namespace = encode("benchmark-ns")
        schema = lib.j_db_schema_new(namespace, name, ffi.NULL)
        for j in range(10):
            fname = encode(f"field{j}")
            lib.j_db_schema_add_field(schema, fname, lib.J_DB_TYPE_STRING,
                                      ffi.NULL)
        lib.j_db_schema_create(schema, batch, ffi.NULL)
        lib.j_db_schema_unref(schema)
    assert lib.j_batch_execute(batch)
    run.start_timer()
    for i in range(run.iterations):
        name = encode(f"benchmark-schema-{i}")
        namespace = encode("benchmark-ns")
        schema = lib.j_db_schema_new(namespace, name, ffi.NULL)
        lib.j_db_schema_delete(schema, batch, ffi.NULL)
        if not use_batch:
            assert lib.j_batch_execute(batch)
        lib.j_db_schema_unref(schema)
    if use_batch:
        assert lib.j_batch_execute(batch)
    run.stop_timer()
    lib.j_batch_unref(batch)
