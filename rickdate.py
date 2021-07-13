#!/usr/bin/env python3
import base36
import datetime
now = datetime.datetime.now()
print("{year}{month}{day}".format(
    year=base36.dumps(now.year)[-1:],
    month=base36.dumps(now.month),
    day=base36.dumps(now.day)
))
