from julea_wrapper import lib, ffi

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
    char = ffi.cast('char*', buffer)
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
        self.batch = lib.j_batch_new_for_template(lib.J_SEMANTICS_TEMPLATE_DEFAULT)
        self.result = result

    def __enter__(self):
        return self.batch

    def __exit__(self, exc_type, exc_value, tb):
        if lib.j_batch_execute(self.batch):
            self.result.Succeed()
        else:
            self.result.Fail()
        lib.j_batch_unref(self.batch)
        if exc_type is not None:
            return False
        else:
            return True
