from init import keyword_list, end_date, start_date
from do_data import do_data
import datetime

if __name__ == '__main__':
    str_startDate = start_date

    str_endDate = end_date

    date_Start = datetime.datetime.strptime(str_startDate, '%Y-%m-%d')

    date_End = datetime.datetime.strptime(str_endDate, '%Y-%m-%d')

    dec_data_list = do_data()

    # 写时间表头
    first = 1
    with open("merge.csv", "a+", encoding="utf-8") as fp:
        while date_Start <= date_End:
            if first == 1:
                fp.write(",")
                first = 0
            str_date_Start = date_Start.strftime("%Y-%m-%d")
            print(str_date_Start)
            fp.write(str_date_Start+",")
            date_Start += datetime.timedelta(days=1)
        fp.write("\n")

    # 写关键词所对应的每天的数据
    cnt = 0
    with open("merge.csv", "a+", encoding="utf-8") as fp:
        for key in keyword_list:
            fp.write(key+",")
            for data in dec_data_list[cnt]:
                fp.write(data+",")
            cnt += 1
            fp.write("\n")
