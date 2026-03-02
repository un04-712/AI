                    # 就绪态
import time
a = 1

b = a + 1           # 运行态

c = input ( '>>')   # 阻塞态
                    # 就绪态
c = int(c)          # 运行态


time.sleep(5)       # 阻塞态
                    # 就绪态
d = b + c           # 运行态

print(d)            # 阻塞态


                    # 结束