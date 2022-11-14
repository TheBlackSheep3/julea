if __name__ == "__main__":
    # KV Client
    benchmark_kv()

    # Object Client
    benchmark_distributed_object()
    benchmark_object()

    # DB Client
    benchmark_db_entry()
    benchmark_db_iterator()
    benchmark_db_schema()

    # Item Client
    benchmark_collection()
    benchmark_item()
