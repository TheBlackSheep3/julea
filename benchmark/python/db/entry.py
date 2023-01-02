from benchmarkrun import BenchmarkRun, append_to_benchmark_list_and_run
from julea import lib, encode, ffi
from db.common import _benchmark_db_insert

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
    _benchmark_db_insert(run, None, "benchmark_insert", False, False, False,
                         True)

def benchmark_db_insert_batch(run):
    _benchmark_db_insert(run, None, "benchmark_insert_batch", True, False,
                         False, True)

def benchmark_db_insert_index_single(run):
    _benchmark_db_insert(run, None, "benchmark_insert_index_single", False,
                         False, True, True)

def benchmark_db_insert_batch_index_single(run):
    _benchmark_db_insert(run, None, "benchmark_insert_batch_index_single", True,
                         False, True, True)

def benchmark_db_insert_index_all(run):
    _benchmark_db_insert(run, None, "benchmark_insert_index_all", False, True,
                         False, True)

def benchmark_db_insert_batch_index_all(run):
    _benchmark_db_insert(run, None, "benchmark_insert_batch_index_all", True,
                         True, False, True)

def benchmark_db_insert_index_mixed(run):
    _benchmark_db_insert(run, None, "benchmakr_insert_index_mixed", False, True,
                         True, True)

def benchmark_db_insert_batch_index_mixed(run):
    _benchmark_db_insert(run, None, "benchmakr_insert_batch_index_mixed", True,
                         True, True, True)

def benchmark_db_delete(run):
    _benchmark_db_delete(run, "benchmark_delete", False, False, False)

def benchmark_db_delete_batch(run):
    _benchmark_db_delete(run, "benchmark_delete_batch", True, False, False)

def benchmark_db_delete_index_single(run):
    _benchmark_db_delete(run, "benchmark_delete_index_single", False, False,
                         True)

def benchmark_db_delete_batch_index_single(run):
    _benchmark_db_delete(run, "benchmark_delete_batch_index_single", True,
                         False, True)

def benchmark_db_delete_index_all(run):
    _benchmark_db_delete(run, "benchmark_delete_index_all", False, True, False)

def benchmark_db_delete_batch_index_all(run):
    _benchmark_db_delete(run, "benchmark_delete_batch_index_all", True, True,
                         False)

def benchmark_db_delete_index_mixed(run):
    _benchmark_db_delete(run, "benchmark_delete_index_mixed", False, True, True)

def benchmark_db_delete_batch_index_mixed(run):
    _benchmark_db_delete(run, "benchmark_delete_batch_index_mixed", True, True,
                         True)

def _benchmark_db_delete(run, namespace, use_batch, use_index_all,
                         use_index_single):
    # TODO: implement _benchmark_db_delete
    namespace_encoded = encode(namespace)
    return

def benchmark_db_update(run):
    _benchmark_db_update(run, "benchmark_update", False, False, False)

def benchmark_db_update_batch(run):
    _benchmark_db_update(run, "benchmark_update_batch", True, False, False)

def benchmark_db_update_index_single(run):
    _benchmark_db_update(run, "benchmark_update_index_single", False, False,
                         True)

def benchmark_db_update_batch_index_single(run):
    _benchmark_db_update(run, "benchmark_update_batch_index_single", True,
                         False, True)

def benchmark_db_update_index_all(run):
    _benchmark_db_update(run, "benchmark_update_index_all", False, True, False)

def benchmark_db_update_batch_index_all(run):
    _benchmark_db_update(run, "benchmark_update_batch_index_all", True, True,
                         False)

def benchmark_db_update_index_mixed(run):
    _benchmark_db_update(run, "benchmark_update_index_mixed", False, True, True)

def benchmark_db_update_batch_index_mixed(run):
    _benchmark_db_update(run, "benchmark_update_batch_index_mixed", True, True,
                         True)

def _benchmark_db_update(run, namespace, use_batch, use_index_all,
                         use_index_single):
    # TODO: implement _benchmark_db_update
    namespace_encoded = encode(namespace)
    return
