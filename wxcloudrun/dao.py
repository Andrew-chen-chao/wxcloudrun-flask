import logging

from sqlalchemy.exc import OperationalError

from wxcloudrun import db
from wxcloudrun.model import Counters, Pulser, BlueTooth

# 初始化日志
logger = logging.getLogger('log')


def query_counterbyid(id):
    """
    根据ID查询Counter实体
    :param id: Counter的ID
    :return: Counter实体
    """
    try:
        return Counters.query.filter(Counters.id == id).first()
    except OperationalError as e:
        logger.info("query_counterbyid errorMsg= {} ".format(e))
        return None


def query_pulserbyimeianduser(imei, user):
    """
    根据imei和user查询Pulser实体
    """
    try:
        return Pulser.query.filter(Pulser.imei == imei, Pulser.user == user).first()
    except OperationalError as e:
        logger.info("query_pulserbyimeianduser errorMsg= {} ".format(e))
        return None

def query_pulser_by_imei_user_all(imei, user, n):
    try:
        return Pulser.query.filter(Pulser.imei == imei, Pulser.user == user).order_by(Pulser.created_at.desc()).limit(n)
    except OperationalError as e:
        logger.info("query_pulser_by_imei_user_all errorMsg= {} ".format(e))
        return None

def query_pulser_by_deviceid_all(device_id, n):
    try:
        return BlueTooth.query.filter(BlueTooth.deviceid == device_id).order_by(BlueTooth.created_at.desc()).limit(n)
    except OperationalError as e:
        logger.info("query_pulser_by_deviceid_all errorMsg= {} ".format(e))
        return None

def quer_pulser_list():
    try:
        return Pulser.query.order_by(Pulser.created_at.desc()).limit(1000)
    except OperationalError as e:
        logger.info("query_pulser_list errorMsg= {} ".format(e))
        return None


def delete_counterbyid(id):
    """
    根据ID删除Counter实体
    :param id: Counter的ID
    """
    try:
        counter = Counters.query.get(id)
        if counter is None:
            return
        db.session.delete(counter)
        db.session.commit()
    except OperationalError as e:
        logger.info("delete_counterbyid errorMsg= {} ".format(e))


def insert_counter(counter):
    """
    插入一个Counter实体
    :param counter: Counters实体
    """
    try:
        db.session.add(counter)
        db.session.commit()
    except OperationalError as e:
        logger.info("insert_counter errorMsg= {} ".format(e))


def update_counterbyid(counter):
    """
    根据ID更新counter的值
    :param counter实体
    """
    try:
        counter = query_counterbyid(counter.id)
        if counter is None:
            return
        db.session.flush()
        db.session.commit()
    except OperationalError as e:
        logger.info("update_counterbyid errorMsg= {} ".format(e))
