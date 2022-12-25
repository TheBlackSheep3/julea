from kv.kv import benchmark_kv
from object.object import benchmark_object
from object.distributed_object import benchmark_distributed_object
from db.entry import benchmark_db_entry
from db.iterator import benchmark_db_iterator
from db.schema import benchmark_db_schema
from item.collection import benchmark_collection
from item.item import benchmark_item

if __name__ == "__main__":
    runs = []
    iterations = 1000

    # KV Client
    benchmark_kv(runs, iterations)

    # Object Client
    # FIXME: comment in other benchmark calls
    #benchmark_distributed_object(runs, iterations)
    benchmark_object(runs, iterations)

    # DB Client
    #benchmark_db_entry(runs, iterations)
    #benchmark_db_iterator(runs, iterations)
    #benchmark_db_schema(runs, iterations)

    # Item Client
    #benchmark_collection(runs, iterations)
    #benchmark_item(runs, iterations)
    for run in runs:
        print(f"run {run.name} took {run.get_runtime_s()} s with {run.get_runtime_ms()/run.iterations} ms per iteration")
