import numpy as np
# QtSql类即QT中的QSqlDatabase类，用于处理与数据库的连接
# QSqlQuery类提供了执行和操作SQL语句的方法
from PyQt5.QtSql import QSqlQuery, QSqlDatabase
from matplotlib import pyplot as plt
import mplcursors
import pandas as pd



class MysqlLite:
    def __init__(self):
        """
            连接数据库
        """
        try:
            # 创建数据库连接
            self.database = QSqlDatabase.addDatabase('QSQLITE')
            # 设置数据库名称
            self.database.setDatabaseName("test.db")
            # 连接数据库
            self.database.open()
        except Exception as e:
            print("无法连接数据库", e)

    def operation_sql(self, sql):
        """
            执行sql语句
        """
        # 创建查询对象
        self.query = QSqlQuery()
        # 执行sql语句
        self.query.exec_(sql)

    def selectData(self, sql):
        self.operation_sql(sql)
        # 获取查询到的数据   record()返回一个QSqlRecord对象 包含查询结果的字段数量 字段名信息
        self.result = self.query.record()
        print(self.result)

        while self.query.next():  # 遍历每一行的数据
            for i in range(self.result.count()):
                print(self.query.value(i), end=" ")
            print()


if __name__ == '__main__':
    # 创建数据库连接
    my_sqlite = MysqlLite()
    # 查询   select * from user_info
    my_sqlite.operation_sql('select * from order_items')
    my_sqlite.result = my_sqlite.query.record()

    # 获取查询到的数据   record()返回一个QSqlRecord对象 包含查询结果的字段数量 字段名信息




    order_ids = []
    order_total = []

    last_id = None  # 上一个用户id
    price_sum = 0.0
    while my_sqlite.query.next():  # 遍历每一行的数据
            order_id = my_sqlite.query.value(1)
            quantity = my_sqlite.query.value(3)
            price = my_sqlite.query.value(4)
            if last_id is None:
                last_id = order_id

                # 订单ID变化时，保存上一个订单的累计金额
            if order_id != last_id:

                order_ids.append(last_id)
                order_total.append(price_sum)
                last_id = order_id
                price_sum = quantity * price
            else:
                price_sum += quantity * price

    # 保存最后一个订单的数据
    if last_id is not None:
        order_ids.append(last_id)
        order_total.append(price_sum)

    order_ids_np = np.array(order_ids, dtype=int)
    order_total_np = np.array(order_total, dtype=int)

    x = np.array(order_ids_np)
    y = np.array(order_total_np)
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用雅黑字体
    plt.rcParams['axes.unicode_minus'] = False  # 显示负号'

    bars = plt.bar(x, y,
                   width=0.6,
                   color='#37ABD4',
                   linewidth=0.6,

                   align='center',
                   alpha=0.5,
                   )
    plt.xlabel('order_id')
    plt.ylabel('order_total')

    # 悬停提示
    cursor = mplcursors.cursor(bars, hover=True)
    cursor.connect("add", lambda sel: sel.annotation.set_text(
        f"用户: {x[sel.index]}\n金额: {y[sel.index]:.2f}元"
    ))
    plt.show()

    res = np.stack((order_ids_np, order_total_np), axis=1)

    np.set_printoptions(suppress=True, precision=2)
    print(res)
    max_index = np.argmax(res[:, 1])
    min_index = np.argmin(res[:, 1])
    # 获取对应的order_id和金额
    max_order_id = res[max_index, 0]
    max_total = res[max_index, 1]
    min_order_id = res[min_index, 0]
    min_total = res[min_index, 1]
    # 输出结果
    print(f"最大金额: {max_total}，对应的order_id: {max_order_id}")
    print(f"最小金额: {min_total}，对应的order_id: {min_order_id}")



