import datetime
from get_data import get_data

# 解密函数
def decryption(keys, data):
    dec_dict = {}

    for j in range(len(keys) // 2):
        dec_dict[keys[j]] = keys[len(keys) // 2 + j]

    dec_data = ''

    for k in range(len(data)):
        dec_data += dec_dict[data[k]]

    return dec_data

# 处理加密数据并整理[[],[]..]
def do_data():
    data_list = get_data()
    dec_data_list = []
    for one_data in data_list:
        temp_list = []
        dec_one_data = decryption(keys=one_data["key"], data=one_data["data"])
        temp_list.append(dec_one_data)
        dec_data_list.append(temp_list)
    return dec_data_list


