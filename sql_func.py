import pymysql
from datetime import datetime

# 資料庫連線設定
db_config = {
    'host': 'localhost',
    'user': 'mcas',
    'password': '000000',
    'database': 'edu'
}

def connect_db():
    """建立資料庫連線"""
    return pymysql.connect(**db_config)

def create_table(table_name):
    """創建資料表，若資料表已存在則不創建"""
    conn = connect_db()
    cursor = conn.cursor()
    sql = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        `id` INT AUTO_INCREMENT PRIMARY KEY,
        `KEY` VARCHAR(255) NOT NULL,
        `VALUE` FLOAT NOT NULL,
        `created_at` DATETIME NOT NULL
    )
    """
    print(sql)
    cursor.execute(sql)
    conn.commit()
    print(f"資料表 {table_name} 創建成功（若尚未存在）")
    cursor.close()
    conn.close()

def insert_data(group_name, key, value):
    """向指定資料表插入資料，包括名字、年齡和當前時間"""
    conn = connect_db()
    cursor = conn.cursor()
    sql = f"INSERT INTO {group_name} (`KEY`, `VALUE`, created_at) VALUES (%s, %s, %s)"
    now = datetime.now()
    cursor.execute(sql, (key, value, now))
    conn.commit()
    print("資料插入成功")
    cursor.close()
    conn.close()
def get_data(group_name):
    dict_data = {}
    conn = connect_db()
    cursor = conn.cursor()
    
    sql = f"SELECT `KEY` ,`created_at`, `value` FROM `{group_name}`"
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        if data[0] not in dict_data:
            dict_data[data[0]] = {'time':[],'value':[]}
        dict_data[data[0]]['time'].append(datetime.isoformat(data[1]))
        dict_data[data[0]]['value'].append(data[2])
    # print(dict_data)
    return dict_data
if __name__ == "__main__":
    # table_name = 'group10'
    # create_table(table_name)  # 創建資料表
    # table_name = 'group11'
    # create_table(table_name)  # 創建資料表
    # table_name = 'group12'
    # create_table(table_name)  # 創建資料表
    # table_name = 'group13'
    # create_table(table_name)  # 創建資料表
    # table_name = 'group14'
    # create_table(table_name)  # 創建資料表
    # table_name = 'group15'
    # create_table(table_name)  # 創建資料表
    # table_name = 'group16'
    # create_table(table_name)  # 創建資料表
    # table_name = 'group17'
    # create_table(table_name)  # 創建資料表
    # table_name = 'group18'
    # create_table(table_name)  # 創建資料表
    # table_name = 'group19'
    # create_table(table_name)  # 創建資料表
    table_name = 'group00'
    insert_data(table_name, 'John Doe2', 30.5)  # 插入一筆資料，年齡使用小數
