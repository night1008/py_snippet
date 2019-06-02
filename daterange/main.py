from datetime import datetime, timedelta


def daterange(start_date, end_date, interval='day'):
    """
    start_date: str or datetime, such as datetime(2019, 5, 12) or '2019-05-12'
    end_date: str or datetime, such as datetime(2019, 5, 18) or '2019-05-18'
    interval: str, such as minute, hour, day, week, month
    """
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

    end_date += timedelta(days=1)

    if interval == 'minute':
        for n in range(int((end_date - start_date).days * 24 * 60)):
            yield start_date + timedelta(minutes=n)
    elif interval == 'hour':
        for i in range(int((end_date - start_date).days * 24)):
            yield start_date + timedelta(hours=i)
    elif interval == 'day':
        for i in range(int((end_date - start_date).days)):
            yield start_date + timedelta(days=i)
    elif interval == 'week':
        start_date = start_date - timedelta(days=start_date.weekday())
        for i in range(0, int((end_date - start_date).days), 7):
            yield start_date + timedelta(days=i)
    elif interval == 'month':
        start_date = start_date.replace(day=1)
        for i in range(start_date.month, (end_date.year - start_date.year) * 12 + end_date.month + 1):
            year  = int((i - 1) / 12) + start_date.year
            month = (i - 1) % 12 + 1
            yield datetime(year, month, 1)
    else:
        raise ValueError('error interval')

if __name__ == '__main__':
    for d in daterange('2019-05-02', '2019-05-20'):
        print(d)
