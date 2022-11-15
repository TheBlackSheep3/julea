from time import perf_counter

class BenchmarkRun:
    def __init__(self, name, iterations):
        self.name = name
        self.iterations = iterations

    def start_timer(self):
        self.timer_started = True
        self.start = perf_counter()

    def stop_timer(self):
        self.timer_started = False
        self.stop = perf_counter()

    def get_runtime(self):
        if not self.timer_started or self.stop == None:
            return None
        else:
            return self.stop - self.start

def append_to_benchmark_list_and_run(_list, run, func):
    _list.append(run)
    func(run)
