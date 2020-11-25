#连接数据库
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format("root","ROOT","127.0.0.1","3306","flask_stu")
#设置数据库追踪信息,压制警告
SQLALCHEMY_TRACK_MODIFICATIONS = True