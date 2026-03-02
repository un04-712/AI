#导入python编译器模块
import py_compile
#导入操作系统模块
import os


source_file = '01python程序转字节码.py'

target_dir = 'pyc_files'

py_compile.compile(source_file,cfile=os.path.join(target_dir,'main.pyc'))