import django.db.backends.sqlite3
from django.db import connection

cursor=connection.cursor()


cursor.execute('select * from AssetTransportationRequest')

rows=cursor.fetchall()
print(rows)
