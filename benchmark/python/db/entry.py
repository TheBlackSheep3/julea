from benchmarkrun import BenchmarkRun, append_to_benchmark_list_and_run
from julea import lib, encode, ffi

def benchmark_db_entry(benchmarkrun_list, iterations):
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/entry/insert", iterations), benchmark_db_insert)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/entry/insert-batch", iterations), benchmark_db_insert_batch)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/entry/insert-index-single", iterations), benchmark_db_insert_index_single)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/entry/insert-batch-index-single", iterations), benchmark_db_insert_batch_index_single)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/entry/insert-index-all", iterations), benchmark_db_insert_index_all)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/entry/insert-batch-index-all", iterations), benchmark_db_insert_batch_index_all)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/entry/insert-index-mixed", iterations), benchmark_db_insert_index_mixed)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/entry/insert-batch-index-mixed", iterations), benchmark_db_insert_batch_index_mixed)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/entry/delete", iterations), benchmark_db_delete)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/entry/delete-batch", iterations), benchmark_db_delete_batch)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/entry/delete-index-single", iterations), benchmark_db_delete_index_single)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/entry/delete-batch-index-single", iterations), benchmark_db_delete_batch_index_single)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/entry/delete-index-all", iterations), benchmark_db_delete_index_all)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/entry/delete-batch-index-all", iterations), benchmark_db_delete_batch_index_all)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/entry/delete-index-mixed", iterations), benchmark_db_delete_index_mixed)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/entry/delete-batch-index-mixed", iterations), benchmark_db_delete_batch_index_mixed)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/entry/update", iterations), benchmark_db_update)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/entry/update-batch", iterations), benchmark_db_update_batch)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/entry/update-index-single", iterations), benchmark_db_update_index_single)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/entry/update-batch-index-single", iterations), benchmark_db_update_batch_index_single)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/entry/update-index-all", iterations), benchmark_db_update_index_all)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/entry/update-batch-index-all", iterations), benchmark_db_update_batch_index_all)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/entry/update-index-mixed", iterations), benchmark_db_update_index_mixed)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/entry/update-batch-index-mixed", iterations), benchmark_db_update_batch_index_mixed)

def benchmark_db_insert(run):
    _benchmark_db_insert(run, False)

def benchmark_db_insert_batch(run):
    _benchmark_db_insert(run, True)

def _benchmark_db_insert(run, use_batch):
    # TODO: implement _benchmark_db_insert
    return

def benchmark_db_insert_index_single(run):
    _benchmark_db_insert_index_single(run, False)

def benchmark_db_insert_batch_index_single(run):
    _benchmark_db_insert_index_single(run, True)

def _benchmark_db_insert_index_single(run, use_batch):
    # TODO: implement _benchmark_db_insert_index_single
    return

def benchmark_db_insert_index_all(run):
    _benchmark_db_insert_index_all(run, False)

def benchmark_db_insert_batch_index_all(run):
    _benchmark_db_insert_index_all(run, True)

def _benchmark_db_insert_index_all(run, use_batch):
    # TODO: implement _benchmark_db_insert_index_all
    return

def benchmark_db_insert_index_mixed(run):
    _benchmark_db_insert_index_mixed(run, False)

def benchmark_db_insert_batch_index_mixed(run):
    _benchmark_db_insert_index_mixed(run, True)

def _benchmark_db_insert_index_mixed(run, use_batch):
    # TODO: implement _benchmark_db_insert_index_mixed
    return

# FIXME: write one method for insert, one for delete and one for update
# don't forget common db to make iterator easier to write
def _benchmark_db_insert(

def benchmark_db_delete(run):
    _benchmark_db_delete(run, False)

def benchmark_db_delete_batch(run):
    _benchmark_db_delete(run, True)

def _benchmark_db_delete(run, use_batch):
    # TODO: implement _benchmark_db_delete
    return

def benchmark_db_delete_index_single(run):
    _benchmark_db_delete_index_single(run, False)

def benchmark_db_delete_batch_index_single(run):
    _benchmark_db_delete_index_single(run, True)

def _benchmark_db_delete_index_single(run, use_batch):
    # TODO: implement _benchmark_db_delete_index_single
    return

def benchmark_db_delete_index_all(run):
    _benchmark_db_delete_index_all(run, False)

def benchmark_db_delete_batch_index_all(run):
    _benchmark_db_delete_index_all(run, True)

def _benchmark_db_delete_index_all(run, use_batch):
    # TODO: implement _benchmark_db_delete_index_all
    return

def benchmark_db_delete_index_mixed(run):
    _benchmark_db_delete_index_mixed(run, False)

def benchmark_db_delete_batch_index_mixed(run):
    _benchmark_db_delete_index_mixed(run, True)

def _benchmark_db_delete_index_mixed(run, use_batch):
    # TODO: implement _benchmark_db_delete_index_mixed
    return

def benchmark_db_update(run):
    _benchmark_db_update(run, False)

def benchmark_db_update_batch(run):
    _benchmark_db_update(run, True)

def _benchmark_db_update(run, use_batch):
    # TODO: implement _benchmark_db_update
    return

def benchmark_db_update_index_single(run):
    _benchmark_db_update_index_single(run, False)

def benchmark_db_update_batch_index_single(run):
    _benchmark_db_update_index_single(run, True)

def _benchmark_db_update_index_single(run, use_batch):
    # TODO: implement _benchmark_db_update_index_single
    return

def benchmark_db_update_index_all(run):
    _benchmark_db_update_index_all(run, False)

def benchmark_db_update_batch_index_all(run):
    _benchmark_db_update_index_all(run, True)

def _benchmark_db_update_index_all(run, use_batch):
    # TODO: implement _benchmark_db_update_index_all
    return

def benchmark_db_update_index_mixed(run):
    _benchmark_db_update_index_mixed(run, False)

def benchmark_db_update_batch_index_mixed(run):
    _benchmark_db_update_index_mixed(run, True)

def _benchmark_db_update_index_mixed(run, use_batch):
    # TODO: implement _benchmark_db_update_index_mixed
    return
