import pandas as pd
from sqlalchemy import create_engine, MetaData
from sqlalchemy.types import Integer, String, Float, DateTime

# Step 1: 读取Excel文件
file_path = r"C:\Users\keith\Desktop\美工组-无图片.xlsx"
df = pd.read_excel(file_path)

# 查看数据
print(df.head())

# Step 2: 创建数据库连接
db_username = 'root'  # 替换为你的数据库用户名
db_password = '111111'  # 替换为你的数据库密码
db_host = '192.168.10.207'  # 替换为你的数据库主机地址
db_port = '3306'  # 通常是3306
db_name = 'art_data_demo'  # 替换为你的数据库名称

engine = create_engine(f'mysql+mysqlconnector://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')
metadata = MetaData()

# Step 3: 自动创建表并插入数据到MySQL数据库
table_name = 'data_app_product'  # 替换为你的目标表名

# 定义数据类型映射
dtype_mapping = {
    'int64': Integer(),
    'float64': Float(),
    'object': String(255),
    'datetime64[ns]': DateTime()
}

# 生成SQLAlchemy兼容的数据类型字典
dtype = {col: dtype_mapping[str(dtype)] for col, dtype in df.dtypes.items()}

try:
    df.to_sql(table_name, con=engine, if_exists='replace', index=False, dtype=dtype)
    print(f"Table '{table_name}' created and data inserted successfully.")
except Exception as e:
    print(f"Error inserting data: {e}")
