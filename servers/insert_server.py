import pandas as pd
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column
from sqlalchemy.types import String, Float, DateTime, BIGINT, NullType
import traceback
from .FindHead import func



class TableInserter:
    #初始化
    def __init__(self, file_path, db_username, db_password, host, port, db_name, table_name):
        self.file_path = file_path
        self.db_username = db_username
        self.db_password = db_password
        self.host = host
        self.port = port
        self.db_name = db_name
        self.table_name = table_name
        #创建数据库链接
        self.engine = create_engine(f'mysql+mysqlconnector://{self.db_username}:{self.db_password}@{self.host}:{self.port}/{self.db_name}')
        self.metadata = MetaData()

    def read_excel_to_df(self):
        try:
            print("wenjianm", self.file_path)
            start_row = func(self.file_path)
            self.df = pd.read_excel(self.file_path, skiprows=start_row)
            self.df.columns = self.df.columns.astype(str).str.strip()
            print("Excel文件读取成功！")
            print(self.df.head())
        except Exception as e:
            print(f"Error reading Excel file:{e}")
            self.df = None

    def insert_data_to_mysql(self):
        table_name = self.table_name
        try:
            if self.df is not None:
                #定义数据类型映射
                dtype_mapping = {
                    'int64': BIGINT(),
                    'float64': Float(),
                    'object': String(255),
                    'datetime64[ns]': DateTime(),
                    'NullType': NullType()
                }

                #生成SQLAlchemy兼容的数据类型字典
                dtype = {col: dtype_mapping[str(dtype)] for col, dtype in self.df.dtypes.items()}

                # 创建数据库表
                self.table = Table(table_name, self.metadata, *[Column(col, type_, nullable=True) for col, type_ in dtype.items()])
                self.metadata.create_all(self.engine)

                #分批插入数据
                batch_size = 10000
                try:
                    total_rows = self.df.shape[0]
                    inserted_rows = 0
                    with self.engine.begin() as conn:
                        for start_row in range(0, total_rows, batch_size):
                            end_row = min(start_row + batch_size, total_rows)
                            batch_df = self.df.iloc[start_row:end_row]
                            batch_df.to_sql(table_name, self.engine, if_exists='append', index=False, dtype=dtype, chunksize=1000)
                            print(f'Inserted rows {start_row} to {end_row} into database.')
                            inserted_rows += len(batch_df)
                        if inserted_rows == total_rows:
                            print('All data inserted successfully.')
                        else:
                            print(f'Error: Total inserted rows {inserted_rows} do not match total_rows {total_rows}.')
                        print(f'All data inserted into {table_name} successfully.')
                except Exception as e:
                    print(f"Error inserting data into database:{e}")
                finally:
                    self.engine.dispose()
        except Exception as e:
            traceback.print_exc()
            print(f"Error inserting data to Mysql:{e}")
#     #插入数据
#     with self.engine.connect() as conn:
#         # 处理空值
#         self.df.fillna(pd.NA, inplace=True)
#         self.df.to_sql(table_name, con=conn, if_exists='replace', index=False, dtype=dtype)
#     print(f"Table '{table_name}' created and data inserted successfully")
# else:
#     print("No data to insert. Please read Excel file first.")


