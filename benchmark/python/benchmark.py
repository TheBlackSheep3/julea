from kv import benchmark_kv
from object import benchmark_object()

if __name__ == "__main__":
    runs = []
    iterations = 1000

    # KV Client
    benchmark_kv(runs, iterations)

    # Object Client
    benchmark_distributed_object(runs, iterations)
    benchmark_object(runs, iterations)

    # DB Client
    benchmark_db_entry(runs, iterations)
    benchmark_db_iterator(runs, iterations)
    benchmark_db_schema(runs, iterations)

    # Item Client
    benchmark_collection(runs, iterations)
    benchmark_item(runs, iterations)
