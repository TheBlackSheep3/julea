from julea_core import lib as JCore
from julea_kv import lib as JKV
from julea_object import lib as JObject
from julea_db import lib as JDB
from julea_item import lib as JItem
from cffi import FFI

ffi = FFI()
encoding = 'utf-8'
NULL = ffi.NULL

def get_uint_ptr():
    result = ffi.new('unsigned int *')
    return result

def get_void_ptr_ptr():
    result = ffi.new('void * *')
    return result

def encode(string):
    result = ffi.new('char[]', string.encode(encoding)) 
    return result

def read_from_buffer(buffer):
    char = ffi.cast('char*', buffer[0])
    string = ""
    i = 0
    byte = char[i]
    while byte != b'\x00':
        string += byte.decode()
        i += 1
        byte = char[i]
    return string

class JBatchResult:
    IsSuccess = False

    def __init__(self):
        pass

    def Succeed(self):
        self.IsSuccess = True

    def Fail(self):
        self.IsSuccess = False;

class JBatch:
    def __init__(self, result):
        self.batch = JCore.j_batch_new_for_template(JCore.J_SEMANTICS_TEMPLATE_DEFAULT)
        self.result = result

    def __enter__(self):
        return self.batch

    def __exit__(self, exc_type, exc_value, tb):
        if JKV.j_batch_execute(self.batch):
            self.result.Succeed()
        else:
            self.result.Fail()
        JCore.j_batch_unref(self.batch)
        if exc_type is not None:
            return False
        else:
            return True
