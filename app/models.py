from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from utils.conn import Base

def init_db():
    # 模型映射成表， 定义的位置必须和模型定义在一个文件
    Base.metadata.create_all()


class UserTest(Base):
    __tablename__ = "usertest"
    id = Column(Integer, primary_key=True, autoincrement= True)
    username = Column(String(10), unique=True, nullable= True)
    realname = Column(String(10), unique=True, nullable= True)
    creat_time = Column(DateTime, default=datetime.now())