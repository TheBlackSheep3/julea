from time import perf_counter()
from julea import lib, encode, ffi

def benchmark_kv():
    benchmark_kv_put()
    benchmark_kv_put_batch()
    benchmark_kv_get()
    benchmark_kv_get_batch()
    benchmark_kv_delete()
    benchmark_kv_delete_batch()
    benchmark_kv_unordered_put_delete()
    benchmark_kv_unordered_put_delete_batch()

def benchmark_kv_put():
    _benchmark_kv_put(False)

def benchmark_kv_put_batch():
    _benchmark_kv_put(True)

def _benchmark_kv_put(use_batch):
    n = 1000
    batch = lib.j_batch_new_for_template(lib.J_SEMANTICS_TEMPLATE_DEFAULT)
    deletebatch = lib.j_batch_new_for_template(lib.J_SEMANTICS_TEMPLATE_DEFAULT)
    start = perf_counter()
    for i in range(n):
        name = f"benchmark-{i}"
        kv = lib.j_kv_new(encode("benchmark"), encode(name))
        lib.j_kv_put(kv, encode("empty"), 6, ffi.NULL, batch)
        lib.j_kv_delte(kv, deletebatch)
        if not use_batch:
            assert lib.j_batch_execute(batch)
        lib.j_kv_unref(kv)
    if use_batch:
        assert lib.j_batch_execute(batch)
    stop = perf_counter()
    assert lib.j_batch_execute(deletebatch)
    lib.j_batch_unref(batch)
    lib.j_batch_unref(deletebatch)
    # TODO process result


def benchmark_kv_get():
    _benchmark_kv_get(False)

def benchmark_kv_get_batch():
    _benchmark_kv_get(True)

def _benchmark_kv_get(use_batch):
    n = 1000
    batch = lib.j_batch_new_for_template(lib.J_SEMANTICS_TEMPLATE_DEFAULT)
    deletebatch = lib.j_batch_new_for_template(lib.J_SEMANTICS_TEMPLATE_DEFAULT)
    for i in range(n):
        name = f"benchmark-{i}"
        kv = lib.j_kv_new(encode("benchmark"), encode(name))
        lib.j_kv_put(kv, encode(name), len(name) + 1, ffi.NULL, batch)
        lib.j_kv_delte(kv, deletebatch)
    assert lib.j_batch_execute(batch)
    start = perf_counter()
    
    stop = perf_counter()
