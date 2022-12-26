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
    # TODO: implement _benchmark_db_schema_create
    return

def benchmark_db_schema_delete(run):
    _benchmark_db_schema_delete(run, False)

def benchmark_db_schema_delete_batch(run):
    _benchmark_db_schema_delete(run, True)

def _benchmark_db_schema_delete(run, use_batch):
    # TODO: implement _benchmark_db_schema_delete
    return
