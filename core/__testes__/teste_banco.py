import pymysql

con = pymysql.connect(host='localhost',
                      user='root',
                      password='ibg_6000',

                      )

db = con.cursor()
print('entrou')

