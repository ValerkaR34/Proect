# import sqlite3
# from mass import x,d,s,q
#
# base = sqlite3.connect('news.db')
# cur = base.cursor()
#
# base.execute('CREATE TABLE IF NOT EXISTS {}(id,login,Password,phone_number)'.format('user'))
# base.commit()
#
# cur.execute('INSERT INTO user VALUES(?,?,?,?)',('1','Fox12','f23244','79803455501'))
# base.commit()
# cur.execute('INSERT INTO user VALUES(?,?,?,?)',('2','Valk','103244','703103455501'))
# base.commit()
# cur.executemany('INSERT INTO user VALUES(?,?,?,?)',(x))
# base.commit()
#
# base.execute('CREATE TABLE IF NOT EXISTS {}(id,Firmid,Name,rights)'.format('Firms'))
# base.commit()
#
# cur.execute('INSERT INTO Firms VALUES(?,?,?,?)',('1','1','Zaro','Clothes'))
# base.commit()
#
# cur.execute('INSERT INTO Firms VALUES(?,?,?,?)',('2','2','Zapro','Food'))
# base.commit()
#
# cur.execute('INSERT INTO Firms VALUES(?,?,?,?)',('3','3','Dark','Door'))
# base.commit()
#
# base.execute('CREATE TABLE IF NOT EXISTS {}(id,prise,date_time,view)'.format('Resourses'))
# base.commit()
#
# cur.executemany('INSERT INTO Resourses VALUES(?,?,?,?)',(d))
# base.commit()
#
# base.execute('CREATE TABLE IF NOT EXISTS {}(id,name,surname,rating,post,salary,chart)'.format('Personal'))
# base.commit()
#
# cur.executemany('INSERT INTO Personal VALUES(?,?,?,?,?,?,?)',(s))
# base.commit()
#
# base.execute('CREATE TABLE IF NOT EXISTS {}(id,typeId,status,condition,FirmId)'.format('Extraction_points'))
# base.commit()
#
# cur.executemany('INSERT INTO Extraction_points VALUES(?,?,?,?,?)',(q))
# base.commit()