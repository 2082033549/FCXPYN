# 2  编写一个装饰器，能记录其他函数调用的日志，将日志写入到文件中；
import functools
import logging
def log(func):
    @functools.wraps(func)
    def wr(*args, **kw):
        logfile = r"G:\text111\text_1.txt"
        logging.basicConfig(level=logging.INFO,  
                            format='%(asctime)s %(levelname)s %(message)s', 
                            datefmt='%Y-%m-%d %H:%M:%S', 
                            filename=logfile,  
                   )
        logging.info('valid passed.\r') 
        return func(*args, **kw)
    return wr
def test():
    return 1
f1 = log(test)
print(f1())