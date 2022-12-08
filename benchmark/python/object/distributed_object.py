from benchmarkrun import BenchmarkRun, append_to_benchmark_list_and_run
# FIX: comment in import
# from julea import lib, encode, ffi

def benchmark_distributed_object(benchmarkrun_list, iterations):
	# FIX: remove debug output
	print("benchmark_distributed_object called")
	return
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/distributed_object/create", iterations), benchmark_distributed_object_create);
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/distributed_object/create-batch", iterations), benchmark_distributed_object_create_batch);
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/distributed_object/delete", iterations), benchmark_distributed_object_delete);
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/distributed_object/delete-batch", iterations), benchmark_distributed_object_delete_batch);
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/distributed_object/status", iterations), benchmark_distributed_object_status);
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/distributed_object/status-batch", iterations), benchmark_distributed_object_status_batch);
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/distributed_object/read", iterations), benchmark_distributed_object_read);
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/distributed_object/read-batch", iterations), benchmark_distributed_object_read_batch);
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/distributed_object/write", iterations), benchmark_distributed_object_write);
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/distributed_object/write-batch", iterations), benchmark_distributed_object_write_batch);
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/distributed_object/unordered-create-delete", iterations), benchmark_distributed_object_unordered_create_delete);
	append_to_benchmark_list_and_run(benchmarkrun_list, BenchmarkRun("/object/distributed_object/unordered-create-delete-batch", iterations), benchmark_distributed_object_unordered_create_delete_batch);

def benchmark_distributed_object_create(run):
	_benchmark_distributed_object_create(run, False)

def benchmark_distributed_object_create_batch(run):
	_benchmark_distributed_object_create(run, True)

def _benchmark_distributed_object_create(run, use_batch):
	distribution = lib.j_distribution_new(lib.J_DISTRIBUTION_ROUND_ROBIN)
	batch = lib.j_batch_new_for_template(lib.J_SEMANTICS_TEMPLATE_DEFAULT)
	deletebatch = lib.j_batch_new_for_template(lib.J_SEMANTICS_TEMPLATE_DEFAULT)
	run.start_timer()
	for i in range(run.iterations):
		name = f"benchmark-{i}"
		obj = lib.j_distributed_object_new(encode("benchmark"), encode(name),
										   distribution)
		lib.j_distributed_object_create(obj, batch)
		lib.j_distributed_object_delte(obj, deletebatch)
		if not use_batch:
			assert lib.j_batch_execute(batch)
		lib.j_distributed_object_unref(obj)
	if use_batch:
		assert lib.j_batch_execute(batch)
	run.stop_timer()
	assert lib.j_batch_execute(deletebatch)
	lib.j_batch_unref(batch)
	lib.j_batch_unref(deletebatch)
	lib.j_distribution_unref(distribution)

def benchmark_distributed_object_delete(run):
	_benchmark_distributed_object_delete(run, False)

def benchmark_distributed_object_delete_batch(run):
	_benchmark_distributed_object_delete(run, True)

def _benchmark_distributed_object_delete(run, use_batch):
	distribution = lib.j_distribution_new(lib.J_DISTRIBUTION_ROUND_ROBIN)
	batch = lib.j_batch_new_for_template(lib.J_SEMANTICS_TEMPLATE_DEFAULT)
	for i in range(run.iterations):
		name = f"benchmark-{i}"
		obj = lib.j_distributed_object_new(encode("benchmark"), encode(name),
										   distribution)
		lib.j_distributed_object_create(obj, batch)
		lib.j_distributed_object_unref(obj)
	assert lib.j_batch_execute(batch)
	run.start_timer()
	for i in range(run.iterations):
		name = f"benchmark-{i}"
		obj = lib.j_distributed_object_new(encode("benchmark"), encode(name),
										   distribution)
		lib.j_distributed_object_delete(obj, batch)
		if not use_batch:
			assert lib.j_batch_execute(batch)
		lib.j_distributed_object_unref(obj)
	if use_batch:
		assert lib.j_batch_execute(batch)
	run.stop_timer()
	lib.j_batch_unref(batch)
	lib.j_distribution_unref(distribution)

def benchmark_distributed_object_status(run):
	_benchmark_distributed_object_status(run, False)
	
def benchmark_distributed_object_status_batch(run):
	_benchmark_distributed_object_status(run, True)

def _benchmark_distributed_object_status(run, use_batch):
	# TODO: finish _benchmark_distributed_object_status implementation
	batch = lib.j_batch_new_for_template(lib.J_SEMANTICS_TEMPLATE_DEFAULT)
	obj = lib.j_object_new(encode("benchmark"), encode("benchmark"))
	lib.j_object_create(obj, batch)
	size_ptr = ffi.new("unsigned long*")
	modification_time_ptr = ffi.new("long*")
	lib.j_object_write(obj, encode("A"), 1, 0, size_ptr, batch)
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

	
def benchmark_distributed_object_read(run):
	_benchmark_distributed_object_read(run, False)

def benchmark_distributed_object_read_batch(run):
	_benchmark_distributed_object_read(run, True)

def _benchmark_distributed_object_read(run, use_batch):
	# TODO: implement _benchmark_distributed_object_read
    return

def benchmark_distributed_object_write(run):
	_benchmark_distributed_object_write(run, False)

def benchmark_distributed_object_write_batch(run):
	_benchmark_distributed_object_write(run, True)

def _benchmark_distributed_object_write(run, use_batch):
	# TODO: implement _benchmark_distributed_object_write
    return

def benchmark_distributed_object_unordered_create_delete(run):
	_benchmark_distributed_object_unordered_create_delete(run, False)

def benchmark_distributed_object_unordered_create_delete_batch(run):
	_benchmark_distributed_object_unordered_create_delete(run, True)

def _benchmark_distributed_object_unordered_create_delete(run, use_batch):
	# TODO: implement _benchmark_distributed_object_unordered_create_delete
    return
