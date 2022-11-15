from benchmarkrun import BenchmarkRun, append_to_benchmark_list_and_run
from julea import lib, encode, ffi

def benchmark_object(benchmarkrun_list, iterations):
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/object/create", iterations), benchmark_object_create);
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/object/create-batch", iterations), benchmark_object_create_batch);
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/object/delete", iterations), benchmark_object_delete);
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/object/delete-batch", iterations), benchmark_object_delete_batch);
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/object/status", iterations), benchmark_object_status);
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/object/status-batch", iterations), benchmark_object_status_batch);
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/object/read", iterations), benchmark_object_read);
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/object/read-batch", iterations), benchmark_object_read_batch);
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/object/write", iterations), benchmark_object_write);
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/object/write-batch", iterations), benchmark_object_write_batch);
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/object/unordered-create-delete", iterations), benchmark_object_unordered_create_delete);
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/object/unordered-create-delete-batch", iterations), benchmark_object_unordered_create_delete_batch);


def benchmark_object_create(run):
    _benchmark_object_create(run, False)

def benchmark_object_create_batch(run):
    _benchmark_object_create(run, True)

def _benchmark_object_create(run, use_batch):

def benchmark_object_delete(run):
    _benchmark_object_delete(run, False)

def benchmark_object_delete_batch(run):
    _benchmark_object_delete(run, True)

def _benchmark_object_delete(run, use_batch):

def benchmark_object_status(run):
    _benchmark_object_status(run, False)

def benchmark_object_status_batch(run):
    _benchmark_object_status(run, True)

def _benchmark_object_status(run, use_batch):

def benchmark_object_read(run):
    _benchmark_object_read(run, False)

def benchmark_object_read_batch(run):
    _benchmark_object_read(run, True)

def _benchmark_object_read(run, use_batch):

def benchmark_object_write(run):
    _benchmark_object_write(run, False)
    
def benchmark_object_write_batch(run):
    _benchmark_object_write(run, True)

def _benchmark_object_write(run, use_batch):

def benchmark_object_unordered_create_delete(run):
    _benchmark_object_unordered_create_delete(run, False)

def benchmark_object_unordered_create_delete_batch(run):
    _benchmark_object_unordered_create_delete(run, True)

def _benchmark_object_unordered_create_delete(run, use_batch):
