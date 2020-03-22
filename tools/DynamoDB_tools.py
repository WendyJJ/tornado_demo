"""
@author: zwq
@time: 2019/7/6
"""

import json, decimal
from boto3.session import Session
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr
from tools.config_tools import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

session = Session(aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                  region_name='ap-south-1')


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


def save_data(table_name, data):
    dynamodb = session.resource('dynamodb', region_name='ap-south-1')
    table = dynamodb.Table(table_name)
    try:
        response = table.put_item(
            Item=data
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        result = json.dumps(response, indent=1, cls=DecimalEncoder)
        if json.loads(result)['ResponseMetadata']['HTTPStatusCode'] == 200:
            return 1
        else:
            return 0


def select_data_id(table_name, key_id, key_val):
    '''
    根据主键查询
    :param table_name:  表名
    :param key_id:      主键
    :param key_val:     主键值
    :return:
    '''
    dynamodb = session.resource('dynamodb', region_name='ap-south-1')
    table = dynamodb.Table(table_name)
    response = table.query(KeyConditionExpression=Key(key_id).eq(str(key_val)))
    # print(response)
    item = response['Items']
    count = response['Count']
    result = json.dumps(item, indent=1, cls=DecimalEncoder)
    return {'item': json.loads(result), 'count': count}


def select_data_id_other(table_name, key_id, key_val, other_id, other_val):
    '''
    根据主键和
    :param table_name:  表名
    :param key_id:      主键
    :param key_val:     主键值
    :param other_id:    条件字段名
    :param other_val:   条件字段值
    :return:
    '''
    dynamodb = session.resource('dynamodb', region_name='ap-south-1')
    table = dynamodb.Table(table_name)
    response = table.query(KeyConditionExpression=Key(key_id).eq(str(key_val)), FilterExpression=Attr(other_id).eq(str(other_val)))
    # print(response)
    item = response['Items']
    count = response['Count']
    result = json.dumps(item, indent=1, cls=DecimalEncoder)
    return {'item': json.loads(result), 'count': count}


def select_data_id_attr(table_name, key_id, key_val, attr_val):
    '''
    根据主键和排序键查询
    :param table_name:  表名
    :param key_id:      主键
    :param key_val:     主键值
    :param attr_val:    排序键值
    :return:
    '''
    dynamodb = session.resource('dynamodb', region_name='ap-south-1')
    table = dynamodb.Table(table_name)
    try:
        response = table.get_item(
            Key={
                key_id: key_val,
                'rank': attr_val
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return {'item': [response['Item']], 'count': 1} if 'Item' in response.keys() else {'item': [], 'count': 0}


def select_data_attr_scan(table_name, query_key, query_value):
    '''
    根据排序键查询
    :param table_name:  表名
    :param query_key:   查询键
    :param query_value:  查询值
    :return:
    '''
    dynamodb = session.resource('dynamodb', region_name='ap-south-1')
    table = dynamodb.Table(table_name)
    try:
        response = table.scan(FilterExpression=Attr(query_key).eq(query_value))
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return {'item': response['Items'], 'count': 1} if 'Items' in response.keys() else {'item': [], 'count': 0}


def select_data_attr_scan_ne(table_name, eq_key, eq_value, ne_key, ne_value):
    '''
    根据条件筛选查询 A=A & B!=B
    :param table_name:  表名
    :param query_key:   查询键
    :param query_value:  查询值
    :return:
    '''
    dynamodb = session.resource('dynamodb', region_name='ap-south-1')
    table = dynamodb.Table(table_name)
    try:
        response = table.scan(FilterExpression=Attr(eq_key).eq(eq_value) & Attr(ne_key).ne(ne_value))
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return {'item': response['Items'], 'count': 1} if 'Items' in response.keys() else {'item': [], 'count': 0}


def select_data_attr_scan_eq(table_name, eq_key, eq_value, eq_key2, eq_value2):
    '''
    根据条件筛选查询 A=A & B=B
    :param table_name:  表名
    :param query_key:   查询键
    :param query_value:  查询值
    :return:
    '''
    dynamodb = session.resource('dynamodb', region_name='ap-south-1')
    table = dynamodb.Table(table_name)
    try:
        response = table.scan(FilterExpression=Attr(eq_key).eq(eq_value) & Attr(eq_key2).eq(eq_value2))
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return {'item': response['Items'], 'count': 1} if 'Items' in response.keys() else {'item': [], 'count': 0}


def select_data_attr_scan_all(table_name, eq_key, eq_value, eq_key2, eq_value2, eq_key3, eq_value3):
    '''
    根据条件筛选查询 A=A & B=B
    :param table_name:  表名
    :param query_key:   查询键
    :param query_value:  查询值
    :return:
    '''
    dynamodb = session.resource('dynamodb', region_name='ap-south-1')
    table = dynamodb.Table(table_name)
    try:
        response = table.scan(FilterExpression=Attr(eq_key).eq(eq_value) & Attr(eq_key2).eq(eq_value2) & Attr(eq_key3).eq(eq_value3))
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return {'item': response['Items'], 'count': 1} if 'Items' in response.keys() else {'item': [], 'count': 0}

if __name__ == '__main__':
    import datetime
    import uuid
    from app.tools.Basic_tools import *
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # table_name = "product_info"
    table_name = "product_information"
    #
    # product_info = "SELECT p_id, lt_id, l_name, rate, l_amount, timeLimit, nop, l_limit, img_url, secured_type, url_link, l_describe, loan_amt, loan_period, interest_rate," \
    #          "acct_management_fee, credit_fee, iscooperation FROM product_info"
    # product_info_list = mysql_connection().mysql_tools(product_info)
    # print(product_info_list)
    # for product_info_data in product_info_list:
    #     print("product_info_data===", product_info_data)
    #     data = {
    #         # "z_id": str(uuid.uuid1()).replace("-", ""),
    #         "rank": "product",
    #         "p_id": str(product_info_data[0]),
    #         "lt_id": str(product_info_data[1]),
    #         "l_name": product_info_data[2],
    #         "rate": str(float(product_info_data[3])),
    #         "l_amount": str(product_info_data[4]),
    #         "timeLimit": str(product_info_data[5]),
    #         "nop": str(product_info_data[6]),
    #         "l_limit": str(product_info_data[7]),
    #         "img_url": product_info_data[8],
    #         "secured_type": product_info_data[9],
    #         "url_link": product_info_data[10],
    #         "l_describe": product_info_data[11],
    #         "loan_amt": str(product_info_data[12]),
    #         "loan_period": str(product_info_data[13]),
    #         "interest_rate": str(float(product_info_data[14])),
    #         "acct_management_fee": str(product_info_data[15]),
    #         "credit_fee": str(product_info_data[16]),
    #         "iscooperation": str(product_info_data[17]),
    #         "update_date": now_time
    #     }
    #     save = save_data("product_info", data)
    #     print(save)
    # a =select_data_id_attr("record_info", "uid", "e7cd619ff85b3dc701fff923df0e1905", "level")
    # print(a)
    # borrow = select_data_attr_scan("order_info", "b_state", 3)["item"]
    # print(borrow)
    # print(len(borrow))
    # for i in borrow:
    #     print(i["p_id"])


    # aa = select_data_attr_scan("order_info", "uid", "b86c0197570261ab0f9be4af127ef4a5")
    # # print(aa["item"])
    # # print(len(aa["item"]))
    # for i in aa["item"]:
    #     if all([i["rank"] == "borrow", i["c_id"] == "1", i["p_id"] == "1"]):
    #         number = i["order_number"]
    #         print("number==", number)
    #         d = select_data_id_attr("order_info", "order_number", number, "bills")
    #         print(d["item"])
    #         print(i)


    # questionsandanswers = "SELECT q_id, cc_id, p_id, questions, answers, c_top FROM questionsandanswers"
    # questionsandanswers_data = mysql_connection().mysql_tools(questionsandanswers)
    # # print(questionsandanswers_data)
    # for i in range(len(questionsandanswers_data)):
    # # for i in range(20):
    #     data = {
    #         "z_id": str(uuid.uuid1()).replace("-", ""),
    #         "rank": "questionsandanswers",
    #         "cc_id": str(questionsandanswers_data[i][1]) if questionsandanswers_data[i][1] is not None else 'NULL',
    #         "p_id": str(questionsandanswers_data[i][2]) if questionsandanswers_data[i][2] is not None else 'NULL',
    #         "questions": str(questionsandanswers_data[i][3]),
    #         "answers": str(questionsandanswers_data[i][4]),
    #         "c_top": str(questionsandanswers_data[i][5]),
    #         "update_date": now_time
    #     }
    #     print(data, '\n---------------------------------------------\n')
    #     save_data('product_information', data)


    # bank = "SELECT bank_id, bank_name, img_url FROM bank"
    # bank_data = mysql_connection().mysql_tools(bank)
    # # print(bank_data)
    # for i in range(len(bank_data)):
    # # for i in range(20):
    #     data = {
    #         "z_id": str(bank_data[i][0]),
    #         "rank": "bank",
    #         "bank_name": str(bank_data[i][1]),
    #         "img_url": str(bank_data[i][2]),
    #         "update_date": now_time
    #     }
    #     print(data, '\n---------------------------------------------\n')
    #     save_data('product_information', data)


    # specialcreditcard = "SELECT sc_id, cc_id, s_describe FROM specialcreditcard"
    # specialcreditcard_data = mysql_connection().mysql_tools(specialcreditcard)
    # # print(bank_data)
    # for i in range(len(specialcreditcard_data)):
    # # for i in range(20):
    #     data = {
    #         "z_id": str(uuid.uuid1()).replace("-", ""),
    #         "rank": "specialcreditcard",
    #         "cc_id": str(specialcreditcard_data[i][1]) if specialcreditcard_data[i][1] is not None else 'NULL',
    #         "s_describe": str(specialcreditcard_data[i][2]),
    #         "update_date": now_time
    #     }
    #     print(data, '\n---------------------------------------------\n')
    #     save_data('product_information', data)


    # creditcardtype = "SELECT ct_id, c_type, img_url FROM creditcardtype"
    # creditcardtype_data = mysql_connection().mysql_tools(creditcardtype)
    # print(creditcardtype_data)
    # for i in range(len(creditcardtype_data)):
    # # for i in range(20):
    #     data = {
    #         "z_id": str(creditcardtype_data[i][0]),
    #         "rank": "creditcardtype",
    #         "c_type": str(creditcardtype_data[i][1]),
    #         "img_url": str(creditcardtype_data[i][2]),
    #         "update_date": now_time
    #     }
    #     print(data, '\n---------------------------------------------\n')
    #     save_data('product_information', data)


    # creditcard = "SELECT cc_id, ct_id, bank_id, cc_name, url_link, c_describe, img_url FROM creditcard"
    # creditcard_data = mysql_connection().mysql_tools(creditcard)
    # print(len(creditcard_data))
    # for i in range(len(creditcard_data)):
    #     # ct_id, bank_id = '', ''
    #     # if creditcard_data[i][1] == 1:
    #     #     ct_id = '21cd3110cb1311e9b07b6c4b901bdd2d'
    #     # elif creditcard_data[i][1] == 6:
    #     #     ct_id = '226c3380cb1311e980f86c4b901bdd2d'
    #     # elif creditcard_data[i][1] == 7:
    #     #     ct_id = '22ea3618cb1311e98e826c4b901bdd2d'
    #     # elif creditcard_data[i][1] == 8:
    #     #     ct_id = '2353ab14cb1311e9a4566c4b901bdd2d'
    #     # elif creditcard_data[i][1] == 9:
    #     #     ct_id = '23be58cccb1311e98b7f6c4b901bdd2d'
    #     # elif creditcard_data[i][1] == 10:
    #     #     ct_id = '24275a18cb1311e994ea6c4b901bdd2d'
    #     #
    #     # if creditcard_data[i][2] == 1:
    #     #     bank_id = 'f3878feccb0611e9bc986c4b901bdd2d'
    #     # elif creditcard_data[i][2] == 2:
    #     #     bank_id = 'f485b578cb0611e99e356c4b901bdd2d'
    #     # elif creditcard_data[i][2] == 3:
    #     #     bank_id = 'f4f3208acb0611e999286c4b901bdd2d'
    #     # elif creditcard_data[i][2] == 4:
    #     #     bank_id = 'f5640a8ccb0611e982076c4b901bdd2d'
    #     # elif creditcard_data[i][2] == 5:
    #     #     bank_id = 'f5c5e4b8cb0611e9a9406c4b901bdd2d'
    #     # elif creditcard_data[i][2] == 6:
    #     #     bank_id = 'f6387c62cb0611e994506c4b901bdd2d'
    #     data = {
    #         "z_id": str(creditcard_data[i][0]),
    #         "rank": "creditcard",
    #         "ct_id": str(creditcard_data[i][1]),
    #         "bank_id": str(creditcard_data[i][2]),
    #         "cc_name": str(creditcard_data[i][3]),
    #         "url_link": str(creditcard_data[i][4]),
    #         "c_describe": str(creditcard_data[i][5]),
    #         "img_url": str(creditcard_data[i][6]),
    #         "update_date": now_time
    #     }
    #     print(data, '\nct_id', data['ct_id'], '\nbank_id', data['bank_id'],'\n---------------------------------------------\n')
    #     save_data('product_information', data)

    a = select_data_attr_scan_all('record_info', "uid", "1907fa6a7863e54aa82c67c2f9ca2e93", "rank", "perfect", "c_id", "1")
    print(a)