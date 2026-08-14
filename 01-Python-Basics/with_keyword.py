#with关键字
'''
用于上下文管理协议（Context Management Protocol）。它简化了资源管理代码，特别是那些需要明确释放或清理的资源
'''
#语法格式
#with expression [as variable]:
#expression 返回一个支持上下文管理协议的对象
#as variable 是可选的，用于将表达式结果赋值给变量
#代码块执行完毕后，自动调用清理方法

#实际应用场景
#1文件操作
# with open('input.txt','r') as infile, open('output.txt','w') as outfile:
#     content = infile.read()
#     outfile.write(content.upper())

#2数据库连接
#3线程锁
#4临时修改系统状态


#创建自定义的上下文管理器
#类实现方式
import time
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.end = time.time()
        print(f"耗时：{self.end - self.start:.2f}秒")
        return False


with Timer() as t:
    time.sleep(0.1)
    sum(range(1000))
