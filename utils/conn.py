from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 连接数据库格式
db_url = 'mysql+pymysql://yd_loan_admin:abcde123!@#@rds93vu04hr3rn0o2d5io.mysql.rds.aliyuncs.com/yd_loan_sys'

# 创建引擎， 建立连接
engine = create_engine(db_url)

# 实现模型与数据库表进行关联的基类， 模型必须继承于Base
Base = declarative_base(bind=engine)

# 创建session会话
DbSession = sessionmaker(bind=engine)
session = DbSession()