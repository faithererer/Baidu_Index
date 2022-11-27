import requests
from header import header
from url_pool import url_get_data, url_uniqid
import json
from init import keyword_list, start_date, end_date


def get_data():
    data_list = []
    for keyword in keyword_list:
        word = f'[[{{"name":"{keyword}","wordType":1}}],[]]'
        params = {
            "area": "0",
            "word": word,
            "startDate": start_date,
            "endDate": end_date
        }
        # 找数据
        res = requests.get(url=url_get_data, params=params, headers=header)
        print(res.text)
        print("-------------")
        data_json = json.loads(res.text)
        data = data_json["data"]["userIndexes"][0]["all"]["data"]
        print(data)
        # 处理密匙
        uniqid = data_json["data"]["uniqid"]
        print("密匙id是：" + uniqid)
        res = requests.get(url=url_uniqid + uniqid, headers=header)
        key = json.loads(res.text)["data"]
        print("密钥是:", key)
        data_list.append({"data": data, "key": key})
    return data_list



