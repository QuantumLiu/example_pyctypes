import ctypes
import numpy as np

def get_cfuncs():
    '''
    加载动态库，返回包装调用C函数的python函数
    '''
    objdll = ctypes.CDLL('./mat_add.dll')#使用ctypes加载dll动态库

    def cfunc1(x, y):
        '''
        本函数使用numpy的ctypeslib.ndpointer作为参数
        '''
        nrow, ncol = x.shape
        
        
        func = objdll.matAdd1#动态库中的函数
        #定义C函数的参数类型
        func.argtypes = [
            ctypes.c_int,
            ctypes.c_int,
            np.ctypeslib.ndpointer(dtype=np.int32, ndim=2, shape=(nrow, ncol)),
            np.ctypeslib.ndpointer(dtype=np.int32, ndim=2, shape=(nrow, ncol)),
            np.ctypeslib.ndpointer(dtype=np.int32, ndim=2, shape=(nrow, ncol))
        ]
        func_restype = None
        
        z = np.empty_like(x)#储存结果的输出数组
        func(nrow, ncol, x, y, z)#调用C函数
        return z

    def cfunc2(x, y):
        '''
        本函数使用int32指针作为参数
        '''
        nrow, ncol = x.shape
                
        func = objdll.matAdd2#动态库中的函数
        #定义C函数的参数类型
        func.argtypes = [
            ctypes.c_int,
            ctypes.c_int,
            ctypes.POINTER(ctypes.c_int),#c_int类型的指针
            ctypes.POINTER(ctypes.c_int),
            ctypes.POINTER(ctypes.c_int)
        ]
        func_restype = None
        
        z = np.empty_like(x)#储存结果的输出数组
        #调用C函数，使用numpy.ndarray.ctypes.data_as方法获得数组指针
        func(nrow, ncol, x.ctypes.data_as(ctypes.POINTER(ctypes.c_int)),\
                y.ctypes.data_as(ctypes.POINTER(ctypes.c_int)),\
                z.ctypes.data_as(ctypes.POINTER(ctypes.c_int)))
        return z

    return cfunc1, cfunc2

if __name__ == '__main__':
    cfunc1,cfunc2=get_cfuncs()

    #输入数组，numpy的int32对应C语言的int类型
    x = np.array([[1, 2], [3, 4]], dtype=np.int32)
    y = np.array([[2, 2], [5, 6]], dtype=np.int32)
    print("Inputs:\nx:\n",x,"\n")
    print("y:\n",y,"\n")

    print("Calculate x + y by C funtion1: ")
    z = cfunc1(x, y)
    print(z)

    print("Calculate x + y by C funtion1: ")
    z = cfunc2(x, y)
    print(z)

    print("Calculate x + y by numpy: ")
    print(x+y)

