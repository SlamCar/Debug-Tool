# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 21:14:02 2018

@author: Gehaha
"""

import ctypes 
import inspect 
def _async_raise(tid, exc_type): 
    tid = ctypes.c_long(tid) 
    if not inspect.isclass(exc_type): 
        exc_type = type(exc_type) 
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exc_type)) 
        if res == 0: 
            raise ValueError("invalid thread id") 
        elif res != 1: 
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed") 
# 强制关闭线程的方法 
def stop_thread(thread): 
    _async_raise(thread.ident, SystemExit)