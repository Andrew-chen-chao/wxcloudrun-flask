from datetime import datetime
from flask import render_template, request
from run import app
from wxcloudrun.dao import delete_counterbyid, query_pulserbyimeianduser, \
    query_counterbyid, insert_counter, update_counterbyid, query_pulser_by_imei_user_all, quer_pulser_list
from wxcloudrun.model import Counters, Pulser
from wxcloudrun.response import make_succ_empty_response, \
    make_succ_response, make_err_response


@app.route('/')
def index():
    """
    :return: 返回index页面
    """
    return render_template('index.html')

@app.route('/jieshou')
def jieshou():
    # print(request.args)
    dia = request.args.get("dia")
    ano = request.args.get("ano")
    user = request.args.get("user")
    tel = request.args.get("tel")
    pul = request.args.get("pul")
    imei = request.args.get("imei")
    sys = request.args.get("sys")
    imsi = request.args.get("imsi")
    iccid = request.args.get("iccid")
    if imei:
        pulse = Pulser()
        pulse.sys = sys
        pulse.dia = dia
        pulse.user = user
        pulse.tel = tel
        pulse.pul = pul
        pulse.imei = imei
        pulse.imsi = imsi
        pulse.iccid = iccid
        pulse.ano = ano
        pulse.created_at = datetime.now()
        pulse.updated_at = datetime.now()
        insert_counter(pulse)
        return "OK{}#end#".format(datetime.now().strftime('%Y%m%d%H%M'))
    else:
        return "False"

@app.route('/api/chaxun_zuijin')
def chaxun():
    '''
    根据请求的mei和user返回最新的一次测量数据
    :return:
    '''
    imei = request.args.get('imei')
    user = request.args.get('user')
    print(imei,user)
    if imei:
        plusers = query_pulserbyimeianduser(imei, user)
        print(plusers.imei, plusers.user, plusers.pul)
        # sys = plusers.sys
        # dia = plusers.dia
        # pul = plusers.pul
        data = {'sys':plusers.sys, 'dia':plusers.dia, 'pul':plusers.pul}
        # return "OK %s %d %s" % (plusers.imei, plusers.user, plusers.pul)
        return make_succ_response(data)

@app.route('/api/chaxun_all')
def chaxunall():
    '''
    根据请求的imei和user返回对应次数的测量数据
    :return:
    '''
    imei = request.args.get('imei')
    user = request.args.get('user')
    n = request.args.get('n')
    print(imei, user, n)
    if imei:
        plusers = query_pulser_by_imei_user_all(imei, user, n)
        obj_list = []
        high_press_list = []
        low_press_list = []
        pul_list = []
        for i in plusers:
            created_at = i.created_at.strftime('%m月%d日 %H:%M')
            data = {'sys': i.sys, 'dia': i.dia, 'pul': i.pul, 'creat_at': created_at}
            obj_list.append(data)
            high_press_list.append(i.sys)
            low_press_list.append(i.dia)
            pul_list.append(i.pul)
        obj_list.reverse()
        press_min = min(low_press_list)
        press_max = max(high_press_list)
        pul_min = min(pul_list)
        pul_max = max(pul_list)
        data = {"press_min": press_min, "press_max": press_max, "pul_min": pul_min, "pul_max": pul_max, "obj_list": obj_list}
        # data = {'sys':plusers.sys, 'dia':plusers.dia, 'pul':plusers.pul}
        # # return "OK %s %d %s" % (plusers.imei, plusers.user, plusers.pul)
        return make_succ_response(data)

@app.route("/api/list")
def cha_xun_1000():
    data_list = []
    pulsers = quer_pulser_list()
    # print(pulsers)
    for i in pulsers:
        # print(i.pul)
        if i.created_at:
            created_at = i.created_at.strftime('%Y年%m月%d日 %H:%M')
            data = {'id': i.id, 'sys': i.sys, 'dia': i.dia, 'user': i.user, 'tel': i.tel, 'pul': i.pul, 'imei': i.imei, 'imsi': i.imsi,
                    'iccid': i.iccid, 'ano': i.ano, 'created_at': created_at}
            data_list.append(data)
    return make_succ_response(data_list)

@app.route('/api/count', methods=['POST'])
def count():
    """
    :return:计数结果/清除结果
    """

    # 获取请求体参数
    params = request.get_json()

    # 检查action参数
    if 'action' not in params:
        return make_err_response('缺少action参数')

    # 按照不同的action的值，进行不同的操作
    action = params['action']

    # 执行自增操作
    if action == 'inc':
        counter = query_counterbyid(1)
        if counter is None:
            counter = Counters()
            counter.id = 1
            counter.count = 1
            counter.created_at = datetime.now()
            counter.updated_at = datetime.now()
            insert_counter(counter)
        else:
            counter.id = 1
            counter.count += 1
            counter.updated_at = datetime.now()
            update_counterbyid(counter)
        return make_succ_response(counter.count)

    # 执行清0操作
    elif action == 'clear':
        delete_counterbyid(1)
        return make_succ_empty_response()

    # action参数错误
    else:
        return make_err_response('action参数错误')


@app.route('/api/count', methods=['GET'])
def get_count():
    """
    :return: 计数的值
    """
    counter = Counters.query.filter(Counters.id == 1).first()
    return make_succ_response(0) if counter is None else make_succ_response(counter.count)
