import pandas as pd
import os
import xlrd
def func(file_path):
    # Step 1: 读取Excel文件
    # df = pd.read_excel(file_path, header=None)
    df = pd.read_excel(file_path)
    # print(df.head())
    count = 0

    for index, row in df.iterrows():
        print(index, row)
        for item in row:
            if pd.isnull(item) or item == '':
                pass
                print(f'项 "{item}" 是空的')
            else:
                count += 1
                print(count)
                if count == len(row):
                    print(count)
                    # print(index)
                    return index