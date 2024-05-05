import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta


def period(start_date: datetime, finish_date: datetime) -> list[str]:
    """
    Returns a list[str] of dates.
    Parameters
    ----------
    start_date : datetime
        The first date in array
    finish_date : datetime
        The last date in array
    """
    # exceptional case
    if start_date >= finish_date:
        raise Exception()
    # calculating
    delta = finish_date - start_date
    result = []
    for i in range(delta.days):
        date = start_date + timedelta(i)
        result += [date.date()]
    return result


d1 = datetime(2024, 5, 31)
d2 = d1 + timedelta(1)
print(d1.date())
print(d2.date())
print(d2 > d1)

p = period(datetime(2024, 1, 28), datetime(2024, 2, 7))
xpoints = [datetime.now() - timedelta(days=_) for _ in range(10)]
ypoints = np.array([1, 8, 4, 6, 7, 9, 4, 3, 5, 9])

fig, ax = plt.subplots()
plt.plot(xpoints, ypoints)
fig.autofmt_xdate(rotation=45)

plt.show()
