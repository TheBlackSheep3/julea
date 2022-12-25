from time import perf_counter_ns

class BenchmarkRun:
    def __init__(self, name, iterations):
        self.name = name
        self.iterations = iterations
        self.timer_started = False
        self.start = None
        self.stop = None

    def start_timer(self):
        self.timer_started = True
        self.start = perf_counter_ns()

    def stop_timer(self):
        self.timer_started = False
        self.stop = perf_counter_ns()

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
