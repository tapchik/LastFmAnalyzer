from datetime import datetime, timezone

START_DATE = '2024-01-01'  # 00:00 in +5; December 31, 2023 7:00:00 PM in Epoch timestamp = 1704049200


def date_to_epoch_timestamp(date: str):
    """Accepts date as 'YYYY-MM-DD'"""
    # zone = timezone.utc
    # now_utc = datetime.now(zone)
    year = int(date[:4])
    month = int(date[5:7])
    day = int(date[8:10])
    epoch_timestamp = datetime(year, month, day).strftime('%s')
    return epoch_timestamp


if __name__ == '__main__':
    print('Expected:   1704049200')
    ep = date_to_epoch_timestamp('2024-01-01')
    print(f'Calculated: {ep}')

    zone = timezone.utc
    d = datetime(2024, 1, 1)
    print(datetime.now(zone))
