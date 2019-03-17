from datetime import datetime, timedelta
import random

import click
from pony.orm import *

db = Database()
db.bind(provider='postgres', user='night', password='', host='127.0.0.1', database='employee')

STRPTIMR_FORMAT = '%Y-%m-%d %H:%M:%S'

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
    _start_time = datetime.strptime(start_time, STRPTIMR_FORMAT)
    seconds_diff = int(datetime.strptime(end_time, STRPTIMR_FORMAT).timestamp() - _start_time.timestamp())
    return _start_time + timedelta(seconds=random.randint(0, seconds_diff))


@click.command()
@click.option('--start_time', prompt='start time(%Y-%m-%d %H:%M:%S)', type=str, help='start time of created_at column')
@click.option('--end_time', prompt='end time(%Y-%m-%d %H:%M:%S)', type=str, help='end time of created_at column')
@click.option('--min_salary', prompt='min salary', type=int, help='min value of salary column')
@click.option('--max_salary', prompt='max salary', type=int, help='max value of salary column')
@click.option('--item_count', default=1, prompt='item count', type=int, help='item count')
def generate_salary_items(start_time, end_time, min_salary, max_salary, item_count):
    def print_click_error(text):
        click.echo(click.style(text, fg='red'))

    try:
        datetime.strptime(start_time, STRPTIMR_FORMAT) or \
            datetime.strptime(end_time, STRPTIMR_FORMAT)
    except ValueError:
        print_click_error('Error format of start_time or end_time param')
        return
    
    if min_salary >= max_salary:
        print_click_error('Param min_salary must be smaller than max_salary')
        return
    if min_salary < 100 or max_salary < 100:
        print_click_error('Param min_salary and max_salary must be greater than 100')
        return

    with db_session:
        for i in range(item_count):
            created_at = get_random_created_at(start_time, end_time)
            province = random.choice(provinces)
            gender = random.choice([0, 1])
            salary = round(random.randint(min_salary, max_salary) / 100) * 100
            item = SalaryItem(salary=salary,
                            gender=gender,
                            province=province,
                            created_at=created_at)
            db.commit()


if __name__ == '__main__':
    print('enter __main__')
    db.generate_mapping(create_tables=True)
    generate_salary_items()
           
