from benchmarkrun import BenchmarkRun, append_to_benchmark_list_and_run
from julea import lib, encode, ffi

def benchmark_collection(benchmarkrun_list, iterations):
    print("benchmark_collection called")
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/item/collection/create", iterations), benchmark_collection_create)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/item/collection/create-batch", iterations), benchmark_collection_create_batch)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/item/collection/delete", iterations), benchmark_collection_delete)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/item/collection/delete-batch", iterations), benchmark_collection_delete_batch)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/item/collection/delete-batch-without-get", iterations), benchmark_collection_delete_batch_without_get)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/item/collection/unordered-create-delete", iterations), benchmark_collection_unordered_create_delete)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/item/collection/unordered-create-delete-batch", iterations), benchmark_collection_unordered_create_delete_batch)
    # TODO: benchmark get (also missing in c benchmark)

def benchmark_collection_create(run):
    _benchmark_collection_create(run, False)

def benchmark_collection_create_batch(run):
    _benchmark_collection_create(run, True)

def _benchmark_collection_create(run, use_batch):
    # TODO: implement _benchmark_collection_create
    return

def benchmark_collection_delete(run):
    _benchmark_collection_delete(run, False)

def benchmark_collection_delete_batch(run):
    _benchmark_collection_delete(run, True)

def _benchmark_collection_delete(run, use_batch):
    # TODO: implement _benchmark_collection_delete
    return

def benchmark_collection_delete_batch_without_get(run):
    # TODO: implement benchmark_collection_delete_batch_without_get
    return

def benchmark_collection_unordered_create_delete(run):
    _benchmark_collection_unordered_create_delete(run, False)

def benchmark_collection_unordered_create_delete_batch(run):
    _benchmark_collection_unordered_create_delete(run, True)

def _benchmark_collection_unordered_create_delete(run, use_batch):
    # TODO: implement _benchmark_collection_unordered_create_delete
    run.operations = run.iterations * 2
    return
