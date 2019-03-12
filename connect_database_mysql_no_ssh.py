#! -*- coding:utf-8 -*-
import pymysql

def dbconn_database(sql_code,**kw):
	'''
	连接MySQL数据库，并且不带ssh的，另外可以传入相应的参数
	'''
	try:
		database = pymysql.connect(host='host',
								 db='db',
							   user='user',
							 passwd='passwd',
							   port=3306,
							   charset='utf8')
		cursor = database.cursor()
		cursor.execute(sql_code.format(**kw))
		data = cursor.fetchall()
		database.close()
		cursor.close()
		return data
	except Exception as e:
		print(e)
