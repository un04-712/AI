
# QtSql类即QT中的QSqlDatabase类，用于处理与数据库的连接
# QSqlQuery类提供了执行和操作SQL语句的方法
from PyQt5.QtSql import QSqlQuery,QSqlDatabase


class MysqlLite:
    def __init__(self):
        """
            连接数据库
        """
        try:
                 # 创建数据库连接
                self.database = QSqlDatabase.addDatabase('QSQLITE')
                 # 设置数据库名称
                self.database.setDatabaseName("user.db")
                # 连接数据库
                self.database.open()
        except Exception as e:
            print("无法连接数据库",e)

    def operation_sql(self,sql):
        """
            执行sql语句
        """
        # 创建查询对象
        self.query = QSqlQuery()
        # 执行sql语句
        self.query.exec_(sql)

    def selectData(self,sql):
        self.operation_sql(sql)
        # 获取查询到的数据   record()返回一个QSqlRecord对象 包含查询结果的字段数量 字段名信息
        self.result = self.query.record()
        print(self.result)

        while self.query.next():  # 遍历每一行的数据
            for i in range(self.result.count()):
                print(self.query.value(i),end=" ")
            print()



if __name__ == '__main__':
    # 创建数据库连接
    my_sqlite = MysqlLite()

    # 建表  user_info    product_info
    """
        primary Key(主键) 是一个特殊的约束 用于唯一标识每条记录，确保数据的唯一性和完整性
        主键有以下特性：
                唯一性 ： 表中不能有两条记录的主键值相同
                非空性： 主键值不能为NULL
                索引性：数据库会自动为主键创建索引，提升查询效率
        AUTOINCREMENT 自动递增
    """
    # 创建表
    # # ID不会自动递增
    my_sqlite.operation_sql("create table if not exists user_info(ID int primary Key,username text,password text,is_admin int)")
    # # ID会自动递增
    # my_sqlite.operation_sql("create table if not exists product_info(ID integer primary Key AUTOINCREMENT,username text,password text,is_admin int)")


    # 增加
    my_sqlite.operation_sql("insert into user_info values(1,'gscsd','321321',0)")
    my_sqlite.operation_sql("insert into user_info values(2,'gscsd2','321321',0)")
    my_sqlite.operation_sql("insert into user_info values(3,'gscsd3','321321',0)")
    # my_sqlite.operation_sql("insert into user_info values(null,'gscsd4','321321',1)")
    #
    # my_sqlite.operation_sql("insert into product_info values(1,'gscsd','321321',0)")
    # my_sqlite.operation_sql("insert into product_info values(2,'gscsd2','321321',0)")
    # my_sqlite.operation_sql("insert into product_info values(null,'gscsd3','321321',1)")

    # 删除
    # 删除表里面的所有行
    # my_sqlite.operation_sql("delete from user_info")
    # 从表里面删除特定的行
    # my_sqlite.operation_sql("delete from user_info where id = 2")

    # 更新
    # 更新字段中所有的内容
    # my_sqlite.operation_sql("update user_info set username = 'pg' ")
    # 更新id=1的username字段内容
    # my_sqlite.operation_sql("update user_info set username = 'pg' where id =1")

    # 查询   select * from user_info
    my_sqlite.selectData('select * from user_info')
