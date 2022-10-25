import sys

sys.path.insert(0, "/home/user/julea")

from julea_kv import lib as libkv
import cffi
ffi = cffi.FFI()

batch = libkv.j_batch_new_for_template(libkv.J_SEMANTICS_TEMPLATE_DEFAULT)
kv = libkv.j_kv_new("c".encode('utf-8'), "value".encode('utf-8'))

length = ffi.new('unsigned int*')
p = ffi.new('void**')
libkv.j_kv_get(kv, p, length, batch)

if (libkv.j_batch_execute(batch)):
    char = ffi.cast('char*', p[0])
    string = ""
    i = 0
    byte = char[i]
    while byte != b'\x00':
        string += byte.decode()
        i += 1
        byte = char[i]
    print("Python says KV contains: '{value}' ({length} bytes)".format(value=string, length=length[0]))
    # clean up
    libkv.j_kv_delete(kv, batch)
    libkv.j_batch_execute(batch)
