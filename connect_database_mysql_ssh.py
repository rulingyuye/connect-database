#! -*- coding:utf-8 -*-
import pymysql
from sshtunnel import SSHTunnelForwarder


def dbconn_database(sql_code,**kw):
	'''
	连接MySQL数据库，并且带ssh的，另外可以传入相应的参数
	'''
	try:
		with SSHTunnelForwarder(
				('ssh_host', 22312),  # B机器的配置
				ssh_password='ssh_password',
				ssh_username='ssh_username',
				remote_bind_address=('remote_bind_address', 3306)) as server:  # A机器的配置
			database = pymysql.connect(host='127.0.0.1',  # 此处必须是是127.0.0.1
										 port=server.local_bind_port,
										 user='user',
										 passwd='passwd',
										 db='db',
										 charset='utf8')
			cursor = database.cursor()
			cursor.execute(sql_code.format(**kw))
			data = cursor.fetchall()
		return data
	except Exception as e:
		print(e)
