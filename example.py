import pandas as pd
from sqlalchemy import create_engine, MetaData
from sqlalchemy.types import String, Float, DateTime, BIGINT, NullType
from servers.FindHead import func

# Step 1: 读取Excel文件
file_path = r"C:\Users\Admin\Desktop\源表\女鞋物价信息查询数据.xls"
start_row = func(file_path)
print(start_row)
# 男/女鞋儒家信息查询数据.xls导入失败
df = pd.read_excel(file_path, skiprows=start_row)
df.columns = df.columns.astype(str).str.strip()

# 查看数据
print(df.head())

# Step 2: 创建数据库连接
db_username = 'root'  # 替换为你的数据库用户名
db_password = '111111'  # 替换为你的数据库密码
db_host = '192.168.10.207'  # 替换为你的数据库主机地址
db_port = '3306'  # 通常是3306
db_name = 'yuting_study'  # 替换为你的数据库名称

engine = create_engine(f'mysql+mysqlconnector://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')
metadata = MetaData()

# Step 3: 自动创建表并插入数据到MySQL数据库
table_name = 'test_db'  # 替换为你的目标表名

# 定义数据类型映射
dtype_mapping = {
    'int64': BIGINT(),
    'float64': Float(),
    'object': String(255),
    'datetime64[ns]': DateTime(),
    'NullType': NullType()
}

# 生成SQLAlchemy兼容的数据类型字典
dtype = {col: dtype_mapping[str(dtype)] for col, dtype in df.dtypes.items()}

batch_size = 10000
try:
    total_rows = df.shape[0]
    inserted_rows = 0

    with engine.connect() as conn:
        for start_row in range(0, total_rows, batch_size):
            end_rows = min(total_rows, start_row + batch_size)
            batch_df = df.iloc[start_row:end_rows]
            batch_df.to_sql(table_name, engine, if_exists='append', index=False, dtype=dtype, chunksize=1000)
            print(f'Inserted rows {start_row} to {end_rows} into database.')
            inserted_rows += len(batch_df)
    if inserted_rows == total_rows:
        print('All data inserted successfully.')
    else:
        print(f'Error: Total inserted rows {inserted_rows} do not match total rows {total_rows}.')
except Exception as e:
    print(f'Error: {e}')
finally:
    engine.dispose()