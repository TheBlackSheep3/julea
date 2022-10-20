import sys

sys.path.insert(0, "/home/user/julea")

from julea_kv import lib as libkv
import cffi
ffi = cffi.FFI()

batch = libkv.j_batch_new_for_template(libkv.J_SEMANTICS_TEMPLATE_DEFAULT)
kv = libkv.j_kv_new("python".encode('utf-8'), "value".encode('utf-8'))

value = "Hello from Python!"
libkv.j_kv_put(kv, ffi.new('char[]', value.encode('utf-8')), len(value)+1, ffi.NULL, batch)

if (libkv.j_batch_execute(batch)):
    sys.exit(0)

sys.exit(1)
