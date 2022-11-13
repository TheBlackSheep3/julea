from julea import JKV, JBatch, JBatchResult, NULL
import cffi
ffi = cffi.FFI()

res = JBatchResult()
with JBatch(res) as batch:
    kv = libkv.j_kv_new(encode("python"), encode("value"))

    value = "Hello from Python!"
    JKV.j_kv_put(kv, encode(value), len(value)+1, NULL, batch)

if (res.IsSuccess):
    sys.exit(0)

sys.exit(1)
