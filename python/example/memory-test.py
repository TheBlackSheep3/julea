import sys
from os.path import dirname

sys.path.insert(0, "{currentdir}/../../bld/".format(currentdir=dirname(__file__)))

from julea_kv import lib as libkv

while True:
    kv = libkv.j_kv_new("python".encode('utf-8'), "value".encode('utf-8'))
    libkv.j_kv_unref(kv)
