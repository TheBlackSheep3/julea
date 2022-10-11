import sys

sys.path.insert(0, "/home/user/julea")

from julea_kv import lib as libkv
import cffi
ffi = cffi.FFI()

batch = libkv.j_batch_new_for_template(libkv.J_SEMANTICS_TEMPLATE_DEFAULT)
kv = libkv.j_kv_new("hello".encode('utf-8'), "world".encode('utf-8'))

value = "Hello World!"
libkv.j_kv_put(kv, ffi.new('char[]', value.encode('utf-8')), len(value)+1, ffi.NULL, batch)

if (libkv.j_batch_execute(batch)):
    buffer = bytes(128)
    length = 0
    # TODO pass correct object to recieve return value
#    libkv.j_kv_get(kv, buffer, length, batch)
#
#    if (libkv.j_batch_execute(batch)):
#        print("KV contains: {value} ({length} bytes)".format(value=buffer.decode(), length=length))
