
import sys
from os.path import dirname

sys.path.insert(0, "{currentdir}/../../bld/".format(currentdir=dirname(__file__)))

from julea_kv import lib as libkv
import cffi
ffi = cffi.FFI()

def get_string(p_buffer, length):
    res = b''
    char = ffi.cast('char*', p_buffer[0])
    for i in range(length):
        res += char[i]
    return res.decode()

def ffi_encode(string):
    p = ffi.new('char[]', string.encode('utf-8'))
    return p

batch = libkv.j_batch_new_for_template(libkv.J_SEMANTICS_TEMPLATE_DEFAULT)
kv1 = libkv.j_kv_new("python".encode('utf-8'), "value".encode('utf-8'))
kv2 = libkv.j_kv_new_for_index(0, "my".encode('utf-8'), "other".encode('utf-8'))

value1 = "Hello from Python!"
value2 = "test"
char_p1 = ffi_encode(value1)
char_p2 = ffi_encode(value2)
libkv.j_kv_put(kv1, char_p1, len(value1)+1, ffi.NULL, batch)
libkv.j_kv_put(kv2, char_p2, len(value2)+1, ffi.NULL, batch)

if (libkv.j_batch_execute(batch)):
    length1 = ffi.new('unsigned int*')
    p1 = ffi.new('void**')
    length2 = ffi.new('unsigned int*')
    p2 = ffi.new('void**')
    libkv.j_kv_get(kv1, p1, length1, batch)
    libkv.j_kv_get(kv2, p2, length2, batch)
    if (libkv.j_batch_execute(batch)):
        print("Python says KV contains: '{value}' ({length} bytes)".format(value=get_string(p1, length1[0]), length=length1[0]))
        print("Python says KV contains: '{value}' ({length} bytes)".format(value=get_string(p2, length2[0]), length=length2[0]))
        # clean up
        libkv.j_kv_delete(kv1, batch)
        libkv.j_kv_delete(kv2, batch)
        libkv.j_batch_execute(batch)
    sys.exit(0)

sys.exit(1)
