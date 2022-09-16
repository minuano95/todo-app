import sqlite3
from sqlite3 import Error

def create_connection():
    connection = None
    try:
        connection = sqlite3.connect('tasks.sql')
        print('Connection to SQLite DB successful')
    except Error as e:
        print(f'The error {e} occurred')
    
    return connection


def insert_records(conn, cursor, task_name, task_date, task_description):
    try:
        query = f'''
        INSERT INTO Task (tasktitle, taskdescription, tasktime)
        VALUES ('{task_name}', '{task_description}', '{task_date}');
        '''
        cursor.execute(query)
        conn.commit()
        
        print('Tarefa inserida na tabela')
    except Error as e:
        print('Error:', e)

def read_records(cursor):
    cursor.execute('SELECT * FROM Task ORDER BY TaskTime ASC')
    records = cursor.fetchall()
    return records 
    

def update_records(cursor, conn, task_id, task_title, task_description, task_time):
    cursor.execute(f"UPDATE Task SET TaskTitle = '{task_title}', TaskDescription = '{task_description}', TaskTime = '{task_time}' WHERE TaskId = {task_id};")
    conn.commit()

def delete_records(cursor, conn, task_id):
    cursor.execute(f'DELETE FROM Task WHERE TaskId = {task_id}')
    conn.commit()

# Setting the db
conn = create_connection()
cursor = conn.cursor()

# Working
# insert_records(conn, cursor, 'Academia', '2022/09/05 05:15:00', 'Ir treinar')
read_records(cursor)
# update_records(cursor, conn, 1, 'Jantar Agora', '', '2022/09/04 21:45:00')
# delete_records(cursor, conn, 2)



conn.close()