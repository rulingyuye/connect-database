#! -*- coding:utf-8 -*-
from sshtunnel import SSHTunnelForwarder
import pymongo


def dbconn_database():
	'''
	连接MongoDB数据库
	'''
	try:
		with SSHTunnelForwarder(
				('ssh_port', 22312),  # B机器的配置
				ssh_password='ssh_password',
				ssh_username='ssh_username',
				remote_bind_address=('remote_bind_address', 3717)) as server:  # A机器的配置
			target = pymongo.MongoClient(port=server.local_bind_port, connect=True)
			target_db = target.database
			target_db.authenticate('username', 'password')
			db_data = target_db.database.find({{'userId':{'$in':list_all}},
												{'_id':0,'userId':1,'os':1}})
		return db_data
	except Exception as e:
		print(e)
