from servers.insert_server import TableInserter


# if __name__ == "__main__":
#     table_inserter = TableInserter(
#         r'C:\Users\Admin\Desktop\源表\订单.xlsx',
#         'root',
#         '111111',
#         '192.168.10.207',
#         '3306',
#         'yuting_study',
#         'orders_db'
#     )
#     table_inserter.read_excel_to_df()
#     table_inserter.insert_data_to_mysql()

if __name__ == "__main__":
    table_inserter = TableInserter(
        r'C:\Users\Admin\Desktop\源表\商品库存.xlsx',
        'root',
        '111111',
        '192.168.10.207',
        '3306',
        'yuting_study',
        'product_stock_db'
    )
    table_inserter.read_excel_to_df()
    table_inserter.insert_data_to_mysql()

# if __name__ == "__main__":
#     table_inserter = TableInserter(
#         r'C:\Users\Admin\Desktop\源表\月罗盘.xlsx',
#         'root',
#         '111111',
#         '192.168.10.207',
#         '3306',
#         'yuting_study',
#         'lunar_compass_db'
#     )
#     table_inserter.read_excel_to_df()
#     table_inserter.insert_data_to_mysql()
#
# if __name__ == "__main__":
#     table_inserter = TableInserter(
#         r'C:\Users\Admin\Desktop\源表\月聚水潭.xlsx',
#         'root',
#         '111111',
#         '192.168.10.207',
#         '3306',
#         'yuting_study',
#         'month_gatherwater_db'
#     )
#     table_inserter.read_excel_to_df()
#     table_inserter.insert_data_to_mysql()

# if __name__ == "__main__":
#     table_inserter = TableInserter(
#         r'C:\Users\Admin\Desktop\源表\男鞋商品信息数据.xls',
#         'root',
#         '111111',
#         '192.168.10.207',
#         '3306',
#         'yuting_study',
#         'man_shoes_db'
#     )
#     table_inserter.read_excel_to_df()
#     table_inserter.insert_data_to_mysql()

# if __name__ == "__main__":
#     table_inserter = TableInserter(
#         r'C:\Users\Admin\Desktop\源表\男鞋物价信息查询数据.xls',
#         'root',
#         '111111',
#         '192.168.10.207',
#         '3306',
#         'yuting_study',
#         'man_price_db'
#     )
#     table_inserter.read_excel_to_df()
#     table_inserter.insert_data_to_mysql()

# if __name__ == "__main__":
#     table_inserter = TableInserter(
#         r'C:\Users\Admin\Desktop\源表\女鞋商品信息数据.xls',
#         'root',
#         '111111',
#         '192.168.10.207',
#         '3306',
#         'yuting_study',
#         'woman_price_db'
#     )
#     table_inserter.read_excel_to_df()
#     table_inserter.insert_data_to_mysql()

# if __name__ == "__main__":
#     table_inserter = TableInserter(
#         r'C:\Users\Admin\Desktop\源表\女鞋物价信息查询数据.xls',
#         'root',
#         '111111',
#         '192.168.10.207',
#         '3306',
#         'yuting_study',
#         'women_price_db'
#     )
#     table_inserter.read_excel_to_df()
#     table_inserter.insert_data_to_mysql()