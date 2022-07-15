from datetime import datetime

from wxcloudrun import db


# 计数表
class Counters(db.Model):
    # 设置结构体表格名称
    __tablename__ = 'Counters'

    # 设定结构体对应表格的字段
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, default=1)
    created_at = db.Column('createdAt', db.TIMESTAMP, nullable=False, default=datetime.now())
    updated_at = db.Column('updatedAt', db.TIMESTAMP, nullable=False, default=datetime.now())


class Pulser(db.Model):
    __tablename__ = 'xueya'

    id = db.Column(db.Integer, primary_key=True)
    imei = db.Column(db.String(20))
    tel = db.Column(db.String(11))
    iccid = db.Column(db.String(20))
    imsi = db.Column(db.String(20))
    user = db.Column(db.Integer)
    sys = db.Column(db.Integer)
    dia = db.Column(db.Integer)
    pul = db.Column(db.Integer)
    ano = db.Column(db.Integer)
    created_at = db.Column('createdAt', db.TIMESTAMP, nullable=False, default=datetime.now())
    updated_at = db.Column('updatedAt', db.TIMESTAMP, nullable=False, default=datetime.now())

class BlueTooth(db.Model):
    __tablename__ = 'xueya_lanya'

    id = db.Column(db.Integer, primary_key=True)
    deviceid = db.Column(db.String(40))
    user = db.Column(db.Integer)
    sys = db.Column(db.Integer)
    dia = db.Column(db.Integer)
    pul = db.Column(db.Integer)
    created_at = db.Column('createdAt', db.TIMESTAMP, nullable=False, default=datetime.now())
    updated_at = db.Column('updatedAt', db.TIMESTAMP, nullable=False, default=datetime.now())

