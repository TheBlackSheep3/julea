from benchmarkrun import BenchmarkRun, append_to_benchmark_list_and_run
from julea import lib, encode, ffi

def benchmark_db_iterator(benchmarkrun_list, iterations):
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/iterator/get-simple", iterations), benchmark_db_get_simple)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/iterator/get-simple-index-single", iterations), benchmark_db_get_simple_index_single)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/iterator/get-simple-index-all", iterations), benchmark_db_get_simple_index_all)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/iterator/get-simple-index-mixed", iterations), benchmark_db_get_simple_index_mixed)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/iterator/get-range", iterations), benchmark_db_get_range)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/iterator/get-range-index-single", iterations), benchmark_db_get_range_index_single)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/iterator/get-range-index-all", iterations), benchmark_db_get_range_index_all)
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/db/iterator/get-range-index-mixed", iterations), benchmark_db_get_range_index_mixed)

def benchmark_db_get_simple(run):
    _benchmark_db_get_simple(run, "benchmark_get_simple", False, False)

def benchmark_db_get_simple_index_single(run):
    _benchmark_db_get_simple(run, "benchmark_get_simple_index_single", False,
                             True)

def benchmark_db_get_simple_index_all(run):
    _benchmark_db_get_simple(run, "benchmark_get_simple_index_all", True, False)

def benchmark_db_get_simple_index_mixed(run):
    _benchmark_db_get_simple(run, "benchmark_get_simple_index_mixed", True, True)

def _benchmark_db_get_simple(run, namespace, use_index_all, use_index_single):
    namespace_encoded = encode(namespace)
    # TODO: implement _benchmark_db_get_simple
    return

def benchmark_db_get_range(run):
    _benchmark_db_get_range(run, "benchmark_get_range", False, False)

def benchmark_db_get_range_index_single(run):
    _benchmark_db_get_range(run, "benchmark_get_range_index_single", False,
                             True)

def benchmark_db_get_range_index_all(run):
    _benchmark_db_get_range(run, "benchmark_get_range_index_all", True, False)

def benchmark_db_get_range_index_mixed(run):
    _benchmark_db_get_range(run, "benchmark_get_range_index_mixed", True, True)

def _benchmark_db_get_range(run, namespace, use_index_all, use_index_single):
    namespace_encoded = encode(namespace)
    # TODO: implement _benchmark_db_get_range
    return
