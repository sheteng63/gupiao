import sqlite3

class actualData:
    def __init__(self):
        con = sqlite3.connect('data.db')
        con.execute('create table actualData (id integer primary key,'
                    'name varchar(10)'
                    'gidcode varchar(10)'
                    'date varchar(10)'
                    'competitivePri varchar(10)'
                    'increPer varchar(10)'
                    'increase varchar(10)'
                    'time varchar(10)'
                    'todayMax varchar(10)'
                    'todayMin varchar(10)'
                    'todayStartPri varchar(10)'
                    'traAmount varchar(20)'
                    'traNumber varchar(10)'
                    'yestodEndPri varchar(10)'
                    ' UNIQUE）')

        # 上面语句创建了一个叫catalog的表，它有一个主键id，一个pid，和一个name，name是不可以重复的。

        pass
