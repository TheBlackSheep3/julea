from benchmarkrun import BenchmarkRun, append_to_benchmark_list_and_run
from julea import lib, encode, ffi

def benchmark_item(benchmarkrun_list, iterations):
	append_to_benchmark_list_and_run(benchmarkrunlist, BenchmarkRun("/item/item/create", iterations), benchmark_item_create)
	append_to_benchmark_list_and_run(benchmarkrunlist, BenchmarkRun("/item/item/create-batch", iterations), benchmark_item_create_batch)
	append_to_benchmark_list_and_run(benchmarkrunlist, BenchmarkRun("/item/item/delete", iterations), benchmark_item_delete)
	append_to_benchmark_list_and_run(benchmarkrunlist, BenchmarkRun("/item/item/delete-batch", iterations), benchmark_item_delete_batch)
	append_to_benchmark_list_and_run(benchmarkrunlist, BenchmarkRun("/item/item/delete-batch-without-get", iterations), benchmark_item_delete_batch_without_get)
	append_to_benchmark_list_and_run(benchmarkrunlist, BenchmarkRun("/item/item/get-status", iterations), benchmark_item_get_status)
	append_to_benchmark_list_and_run(benchmarkrunlist, BenchmarkRun("/item/item/get-status-batch", iterations), benchmark_item_get_status_batch)
    # TODO: benchmark get (also missing in c benchmark)
	append_to_benchmark_list_and_run(benchmarkrunlist, BenchmarkRun("/item/item/read", iterations), benchmark_item_read)
	append_to_benchmark_list_and_run(benchmarkrunlist, BenchmarkRun("/item/item/read-batch", iterations), benchmark_item_read_batch)
	append_to_benchmark_list_and_run(benchmarkrunlist, BenchmarkRun("/item/item/write", iterations), benchmark_item_write)
	append_to_benchmark_list_and_run(benchmarkrunlist, BenchmarkRun("/item/item/write-batch", iterations), benchmark_item_write_batch)
	append_to_benchmark_list_and_run(benchmarkrunlist, BenchmarkRun("/item/item/unordered-create-delete", iterations), benchmark_item_unordered_create_delete)
	append_to_benchmark_list_and_run(benchmarkrunlist, BenchmarkRun("/item/item/unordered-create-delete-batch", iterations), benchmark_item_unordered_create_delete_batch)

def benchmark_item_create(run):
    _benchmark_item_create(run, False)

def benchmark_item_create_batch(run):
    _benchmark_item_create(run, True)

def _benchmark_item_create(run, use_batch):
    # TODO: implement _benchmark_item_create
    return

def benchmark_item_delete(run):
    _benchmark_item_delete(run, False)

def benchmark_item_delete_batch(run):
    _benchmark_item_delete(run, True)

def _benchmark_item_delete(run, use_batch):
    # TODO: implement _benchmark_item_delete
    return

def benchmark_item_delete_batch_without_get(run):
    # TODO: implement benchmark_item_delete_batch_without_get
    return

def benchmark_item_get_status(run):
    _benchmark_item_get_status(run, False)

def benchmark_item_get_status_batch(run):
    _benchmark_item_get_status(run, True)

def _benchmark_item_get_status(run, use_batch):
    # TODO: implement _benchmark_item_get_status
    return

def benchmark_item_read(run):
    _benchmark_item_read(run, False)

def benchmark_item_read_batch(run):
    _benchmark_item_read(run, True)

def _benchmark_item_read(run, use_batch):
    # TODO: implement _benchmark_item_read
    return

def benchmark_item_write(run):
    _benchmark_item_write(run, False)

def benchmark_item_write_batch(run):
    _benchmark_item_write(run, True)

def _benchmark_item_write(run, use_batch):
    # TODO: implement _benchmark_item_write
    return

def benchmark_item_unordered_create_delete(run):
    _benchmark_item_unordered_create_delete(run, False)

def benchmark_item_unordered_create_delete_batch(run):
    _benchmark_item_unordered_create_delete(run, True)

def _benchmark_item_unordered_create_delete(run, use_batch):
    # TODO: implement _benchmark_item_unordered_create_delete
    run.operations = run.iterations * 2
    return
