import sqlite3 as sq

async def try_create_db():
  conn = sq.connect('zabotum.db')
  cur = conn.cursor()

  cur.execute('CREATE TABLE IF NOT EXISTS users \
              (name varchar(50), \
              tg_id varchar(50) primary key,\
               tg_username varchar(50))')
  cur.execute('CREATE TABLE IF NOT EXISTS menu \
              (row_name varchar(20) primary key,\
               text varchar(100),\
               photo varchar(100), video_note varchar(100))')
  cur.execute('CREATE TABLE IF NOT EXISTS depression_test \
              (question varchar(100) primary key)')
  cur.execute('CREATE TABLE IF NOT EXISTS anxiety_test \
              (question varchar(100) primary key)')
  cur.execute('CREATE TABLE IF NOT EXISTS results \
              (user_id varchar(50), test varchar(50),\
              q_num int, questions varchar(300))')

  conn.commit()
  cur.close()
  conn.close()