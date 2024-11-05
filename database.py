import mysql.connector


def execute_sql(query):
    try:
        # 建立数据库连接
        connection = mysql.connector.connect(
            host="localhost",  # 替换为实际的主机地址
            user="test_user",  # 替换为实际的用户
            password="test_password",  # 替换为实际的密码
            database="test_database"  # 替换为实际的数据库名
        )
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        connection.close()
        print(f"[Database] 执行的 SQL 查询: {query}")  # 记录查询语句
        print(f"[Database] 查询结果: {results}")  # 记录查询结果
        return results

    except mysql.connector.Error as err:
        print(f"数据库连接失败: {err}")  # 输出错误信息，帮助排查问题
        return [("数据库连接失败，返回默认信息",)]

