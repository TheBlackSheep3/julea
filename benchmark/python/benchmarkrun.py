from time import perf_counter_ns

class BenchmarkRun:
    def __init__(self, name, iterations):
        self.name = name
        self.iterations = iterations
        self.timer_started = False
        self.start = None
        self.stop = None
        self.operations = iterations

    def start_timer(self):
        self.timer_started = True
        self.start = perf_counter_ns()

    def stop_timer(self):
        self.timer_started = False
        self.stop = perf_counter_ns()
        name_col = self.name.ljust(60," ")
        runtime_col = f"{self.get_runtime_s():.3f}".rjust(8," ") + " seconds"
        operations_col = f"{int(self.operations/self.get_runtime_s())}/s".rjust(12," ")
        print(f"{name_col} | {runtime_col} | {operations_col}")

    def get_runtime_ms(self):
        val = self.get_runtime_ns()
        return val / 1000000 if val != None else None

    def get_runtime_s(self):
        val = self.get_runtime_ns()
        return val / 1000000000 if val != None else None

    def get_runtime_ns(self):
        if self.timer_started or self.stop == None:
            return None
        else:
            return self.stop - self.start

def append_to_benchmark_list_and_run(_list, run, func):
    _list.append(run)
    func(run)

def print_result_table_header():
    name_col = "Name".ljust(60," ")
    runtime_col = "Duration".ljust(16," ")
    operations_col = f"Operations/s".rjust(12," ")
    header = f"{name_col} | {runtime_col} | {operations_col}"
    print(header+"\n"+len(header)*"-")
