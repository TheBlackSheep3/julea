from benchmarkrun import BenchmarkRun, append_to_benchmark_list_and_run
# FIX: comment in import
# from julea import lib, encode, ffi

def benchmark_kv(benchmarkrun_list, iterations):
    # FIX: remove debug output
    print("benchmark_kv called")
    return
    append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/kv/put", iterations), benchmark_kv_put)
    append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/kv/put_batch", iterations), benchmark_kv_put_batch)
    append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/kv/get", iterations), benchmark_kv_get)
    append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/kv/get-batch", iterations), benchmark_kv_get_batch)
    append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/kv/delete", iterations), benchmark_kv_delete)
    append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/kv/delete-batch", iterations), benchmark_kv_delete_batch)
    append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/kv/unordered_put_delete", iterations), benchmark_kv_unordered_put_delete)
    append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/kv/unordered_put_delete_batch", iterations), benchmark_kv_unordered_put_delete_batch)

def benchmark_kv_put(run):
    _benchmark_kv_put(run, False)

def benchmark_kv_put_batch(run):
    _benchmark_kv_put(run, True)

def _benchmark_kv_put(run, use_batch):
    batch = lib.j_batch_new_for_template(lib.J_SEMANTICS_TEMPLATE_DEFAULT)
    deletebatch = lib.j_batch_new_for_template(lib.J_SEMANTICS_TEMPLATE_DEFAULT)
    run.start_timer()
    for i in range(run.iterations):
        name = f"benchmark-{i}"
        kv = lib.j_kv_new(encode("benchmark"), encode(name))
        lib.j_kv_put(kv, encode("empty"), 6, ffi.NULL, batch)
        lib.j_kv_delte(kv, deletebatch)
        if not use_batch:
            assert lib.j_batch_execute(batch)
        lib.j_kv_unref(kv)
    if use_batch:
        assert lib.j_batch_execute(batch)
    run.stop_timer()
    assert lib.j_batch_execute(deletebatch)
    lib.j_batch_unref(batch)
    lib.j_batch_unref(deletebatch)

def benchmark_kv_get(run):
    _benchmark_kv_get(run, False)

def benchmark_kv_get_batch(run):
    _benchmark_kv_get(run, True)

def _benchmark_kv_get(run, use_batch):
    batch = lib.j_batch_new_for_template(lib.J_SEMANTICS_TEMPLATE_DEFAULT)
    deletebatch = lib.j_batch_new_for_template(lib.J_SEMANTICS_TEMPLATE_DEFAULT)
    for i in range(run.iterations):
        name = f"benchmark-{i}"
        kv = lib.j_kv_new(encode("benchmark"), encode(name))
        lib.j_kv_put(kv, encode(name), len(name) + 1, ffi.NULL, batch)
        lib.j_kv_delte(kv, deletebatch)
        lib.j_kv_unref(kv)
    assert lib.j_batch_execute(batch)
    run.start_timer()
    for i in range(run.iterations):
        name = f"benchmark-{i}"
        kv = lib.j_kv_new(encode("benchmark"), encode(name))
        lib.j_kv_get_callback(kv, ffi.NULL, ffi.NULL, batch)
        if not use_batch:
            assert lib.j_batch_execute(batch)
        lib.j_kv_unref(kv)
    if use_batch:
        assert lib.j_batch_execute(batch)
    run.stop_timer()
    assert lib.j_batch_execute(deletebatch)
    lib.j_batch_unref(batch)
    lib.j_batch_unref(deletebatch)

def benchmark_kv_delete(run):
    _benchmark_kv_delete(run, False)

def benchmark_kv_delete_batch(run):
    _benchmark_kv_delete(run, True)

def _benchmark_kv_delete(run, use_batch):
    batch = lib.j_batch_new_for_template(lib.J_SEMANTICS_TEMPLATE_DEFAULT)
    for i in range(run.iterations):
        name = f"benchmark-{i}"
        kv = lib.j_kv_new(encode("benchmark"), encode(name))
        lib.j_kv_put(kv, encode("empty"), 6, ffi.NULL, batch)
        lib.j_kv_unref(kv)
    assert lib.j_batch_execute(batch)
    run.start_timer()
    for i in range(run.iterations):
        name = f"benchmark-{i}"
        kv = lib.j_kv_new(encode("benchmark"), encode(name))
        lib.j_kv_delete(kv, batch)
        if not use_batch:
            assert lib.j_batch_execute(batch)
        lib.j_kv_unref(kv)
    if use_batch:
        assert lib.j_batch_execute(batch)
    run.stop_timer()
    lib.j_batch_unref(batch)

def benchmark_kv_unordered_put_delete(run):
    _benchmark_kv_unordered_put_delete(run, False)

def benchmark_kv_unordered_put_delete_batch(run):
    _benchmark_kv_unordered_put_delete(run, True)

def _benchmark_kv_unordered_put_delete(run, use_batch):
    batch = lib.j_batch_new_for_template(lib.J_SEMANTICS_TEMPLATE_DEFAULT)
    run.start_timer()
    for i in range(run.iterations):
        name = f"benchmark-{i}"
        kv = lib.j_kv_new(encode("benchmark"), encode(name))
        lib.j_kv_put(kv, encode("empty"), 6, ffi.NULL, batch)
        lib.j_kv_delete(kv, batch)
        if not use_batch:
            assert lib.j_batch_execute(batch)
        lib.j_kv_unref(kv)
    if use_batch:
        assert lib.j_batch_execute(batch)
    run.stop_timer()
    lib.j_batch_unref(batch)
