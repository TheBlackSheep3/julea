import os
from build_helper import build, collect_julea

if __name__ == "__main__":
    filename = "test-header.h"
    collect_julea(filename)
    build("julea_kv", ["julea", "julea-kv"])
    os.system("rm -rf {file}".format(file=filename))
