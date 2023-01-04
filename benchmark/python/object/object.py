from benchmarkrun import BenchmarkRun, append_to_benchmark_list_and_run
from julea import lib, encode, ffi

def benchmark_object(benchmarkrun_list, iterations):
    append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/object/create", iterations), benchmark_object_create)
    append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/object/create-batch", iterations), benchmark_object_create_batch)
    append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/object/delete", iterations), benchmark_object_delete)
    append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/object/delete-batch", iterations), benchmark_object_delete_batch)
    append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/object/status", iterations), benchmark_object_status)
    append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/object/status-batch", iterations), benchmark_object_status_batch)
    append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/object/read", iterations), benchmark_object_read)
    append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/object/read-batch", iterations), benchmark_object_read_batch)
    append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/object/write", iterations), benchmark_object_write)
    append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/object/write-batch", iterations), benchmark_object_write_batch)
    append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/object/unordered-create-delete", iterations), benchmark_object_unordered_create_delete)
    append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/object/unordered-create-delete-batch", iterations), benchmark_object_unordered_create_delete_batch)


def benchmark_object_create(run):
    _benchmark_object_create(run, False)

def benchmark_object_create_batch(run):
    _benchmark_object_create(run, True)

def _benchmark_object_create(run, use_batch):
    batch = lib.j_batch_new_for_template(lib.J_SEMANTICS_TEMPLATE_DEFAULT)
    deletebatch = lib.j_batch_new_for_template(lib.J_SEMANTICS_TEMPLATE_DEFAULT)
    run.start_timer()
    for i in range(run.iterations):
        name = encode(f"benchmark-{i}")
        namespace = encode("benchmark")
        obj = lib.j_object_new(namespace, name)
        lib.j_object_create(obj, batch)
        lib.j_object_delete(obj, deletebatch)
        if not use_batch:
            assert lib.j_batch_execute(batch)
        lib.j_object_unref(obj)
    if use_batch:
        assert lib.j_batch_execute(batch)
    run.stop_timer()
    assert lib.j_batch_execute(deletebatch)
    lib.j_batch_unref(batch)
    lib.j_batch_unref(deletebatch)


def benchmark_object_delete(run):
    _benchmark_object_delete(run, False)

def benchmark_object_delete_batch(run):
    _benchmark_object_delete(run, True)

def _benchmark_object_delete(run, use_batch):
    batch = lib.j_batch_new_for_template(lib.J_SEMANTICS_TEMPLATE_DEFAULT)
    for i in range(run.iterations):
        name = encode(f"benchmark-{i}")
        namespace = encode("benchmark")
        obj = lib.j_object_new(namespace, name)
        lib.j_object_create(obj, batch)
        lib.j_object_unref(obj)
    assert lib.j_batch_execute(batch)
    run.start_timer()
    for i in range(run.iterations):
        name = encode(f"benchmark-{i}")
        namespace = encode("benchmark")
        obj = lib.j_object_new(namespace, name)
        lib.j_object_delete(obj, batch)
        if not use_batch:
            assert lib.j_batch_execute(batch)
        lib.j_object_unref(obj)
    if use_batch:
        assert lib.j_batch_execute(batch)
    run.stop_timer()
    lib.j_batch_unref(batch)

def benchmark_object_status(run):
    _benchmark_object_status(run, False)

def benchmark_object_status_batch(run):
    _benchmark_object_status(run, True)

def _benchmark_object_status(run, use_batch):
    batch = lib.j_batch_new_for_template(lib.J_SEMANTICS_TEMPLATE_DEFAULT)
    name = encode("benchmark")
    obj = lib.j_object_new(name, name)
    lib.j_object_create(obj, batch)
    size_ptr = ffi.new("unsigned long*")
    modification_time_ptr = ffi.new("long*")
    character = encode("A")
    lib.j_object_write(obj, character, 1, 0, size_ptr, batch)
    assert lib.j_batch_execute(batch)
    run.start_timer()
    for i in range(run.iterations):
        lib.j_object_status(obj, modification_time_ptr, size_ptr, batch)
        if not use_batch:
            assert lib.j_batch_execute(batch)
    if use_batch:
        assert lib.j_batch_execute(batch)
    run.stop_timer()
    lib.j_object_delete(obj, batch)
    assert lib.j_batch_execute(batch)
    lib.j_object_unref(obj)
    lib.j_batch_unref(batch)

def benchmark_object_read(run):
    _benchmark_object_read(run, False, 4 * 1024)

def benchmark_object_read_batch(run):
    _benchmark_object_read(run, True, 4 * 1024)

def _benchmark_object_read(run, use_batch, block_size):
    dummy = ffi.new("char[]", block_size)
    nb_ptr = ffi.new("unsigned long*")
    batch = lib.j_batch_new_for_template(lib.J_SEMANTICS_TEMPLATE_DEFAULT)
    name = encode("benchmark")
    obj = lib.j_object_new(name, name)
    lib.j_object_create(obj, batch)
    for i in range(run.iterations):
        lib.j_object_write(obj, dummy, block_size, i * block_size, nb_ptr,
                           batch)
    assert lib.j_batch_execute(batch)
    assert nb_ptr[0] == run.iterations * block_size
    run.start_timer()
    for i in range(run.iterations):
        lib.j_object_read(obj, dummy, block_size, i * block_size, nb_ptr, batch)
        if not use_batch:
            assert lib.j_batch_execute(batch)
            assert nb_ptr[0] == block_size
    if use_batch:
        assert lib.j_batch_execute(batch)
        assert nb_ptr[0] == run.iterations * block_size
    run.stop_timer()
    lib.j_object_delete(obj, batch)
    assert lib.j_batch_execute(batch)
    lib.j_object_unref(obj)
    lib.j_batch_unref(batch)

def benchmark_object_write(run):
    _benchmark_object_write(run, False, 4 * 1024)
    
def benchmark_object_write_batch(run):
    _benchmark_object_write(run, True, 4 * 1024)

def _benchmark_object_write(run, use_batch, block_size):
    dummy = ffi.new("char[]", block_size)
    nb_ptr = ffi.new("unsigned long*")
    batch = lib.j_batch_new_for_template(lib.J_SEMANTICS_TEMPLATE_DEFAULT)
    name = encode("benchmark")
    obj = lib.j_object_new(name, name)
    lib.j_object_create(obj, batch)
    run.start_timer()
    for i in range(run.iterations):
        lib.j_object_write(obj, dummy, block_size, i * block_size, nb_ptr,
                           batch)
        if not use_batch:
            assert lib.j_batch_execute(batch)
            assert nb_ptr[0] == block_size
    if use_batch:
        assert lib.j_batch_execute(batch)
        assert nb_ptr[0] == run.iterations * block_size
    run.stop_timer()
    lib.j_object_delete(obj, batch)
    assert lib.j_batch_execute(batch)
    lib.j_object_unref(obj)
    lib.j_batch_unref(batch)

def benchmark_object_unordered_create_delete(run):
    _benchmark_object_unordered_create_delete(run, False)

def benchmark_object_unordered_create_delete_batch(run):
    _benchmark_object_unordered_create_delete(run, True)

def _benchmark_object_unordered_create_delete(run, use_batch):
    batch = lib.j_batch_new_for_template(lib.J_SEMANTICS_TEMPLATE_DEFAULT)
    run.start_timer()
    for i in range(run.iterations):
        name = encode(f"benchmark-{i}")
        namespace = encode("benchmark")
        obj = lib.j_object_new(namespace, name)
        lib.j_object_create(obj, batch)
        lib.j_object_delete(obj, batch)
        if not use_batch:
            assert lib.j_batch_execute(batch)
        lib.j_object_unref(obj)
    if use_batch:
        assert lib.j_batch_execute(batch)
    run.stop_timer()
    lib.j_batch_unref(batch)
    run.operations = run.iterations * 2