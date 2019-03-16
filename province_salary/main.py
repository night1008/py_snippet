
import math
from datetime import datetime, timedelta
import random
from pony.orm import *

db = Database()
db.bind(provider='postgres', user='user', password='', host='127.0.0.1', database='employee')

class SalaryItem(db.Entity):
    gender = Required(bool)
    salary = Required(int)
    province = Required(str)
    created_at = Required(datetime)

# random.choice(provinces)
provinces = [
    '北京市',
    '天津市',
    '上海市',
    '重庆市',
    '河北省',
    '山西省',
    '辽宁省',
    '吉林省',
    '黑龙江省',
    '江苏省',
    '浙江省',
    '安徽省',
    '福建省',
    '江西省',
    '山东省',
    '河南省',
    '湖北省',
    '湖南省',
    '广东省',
    '海南省',
    '四川省',
    '贵州省',
    '云南省',
    '陕西省',
    '甘肃省',
    '青海省',
    '台湾省',
    '内蒙古自治区',
    '广西壮族自治区',
    '西藏自治区',
    '宁夏回族自治区',
    '新疆维吾尔自治区',
]

def get_random_created_at(start_time, end_time):
    strptime_format = '%Y-%m-%d %H:%M:%S'
    _start_time = datetime.strptime(start_time, strptime_format)
    seconds_diff = int(datetime.strptime(end_time, strptime_format).timestamp() - _start_time.timestamp())
    return _start_time + timedelta(seconds=random.randint(0, seconds_diff))

if __name__ == '__main__':
    print('enter __main__')
    db.generate_mapping(create_tables=True)
    with db_session:
        for i in range(100):
            created_at = get_random_created_at('2019-03-12 00:00:00', '2019-03-13 00:00:00')
            province = random.choice(provinces)
            gender = random.choice([0, 1])
            salary = round(random.randint(6000, 15000) / 100) * 100
            item = SalaryItem(salary=salary,
                            gender=gender,
                            province=province,
                            created_at=created_at)
            db.commit()
           
