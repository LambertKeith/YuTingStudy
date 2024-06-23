import mysql.connector

# MySQL数据库连接参数
config = {
  'user': 'root',          # 替换为你的数据库用户名
  'password': '111111',    # 替换为你的数据库密码
  'host': '192.168.10.207',# 替换为你的数据库主机地址
  'port': 3306,            # 通常是3306
  'database': 'yuting_study' # 替换为你的数据库名称
}

# 连接到MySQL数据库
try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # 读取名为"id"的列数据
    #cursor.execute(f"SELECT id FROM mouth_gatherwater_db")
    cursor.execute("SELECT id FROM test_db")
    db_ids = [row[0] for row in cursor.fetchall()]

    # 生成从1到541991的整数列表
    expected_ids = list(range(1, 541992))

    # 比较两个列表并打印其不同项
    diff_items = list(set(expected_ids) - set(db_ids))
    print(f"Differences between expected ids and database ids:\n{diff_items}")
    print(len(db_ids))
    print(db_ids[10086])

except mysql.connector.Error as err:
    import traceback; traceback.print_exc()
    print(f"Error: {err}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
