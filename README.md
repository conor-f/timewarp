# Timewarp

Timewarp is a wrapper for the headaches of `datetime`. It relies heavily on
`python-dateutil` and `datetime` itself. Supports Python3.6+ and can be
installed from pip with `python3 -m pip install timewarp`.


## Usage

You create a `Timewarp` by specifying modifiers to the current timestamp.

`@` snaps to the previous point in time.

The following table denotes what primitive keywords `Timewarp` understands:

| Keyword | Meaning |
|---------|---------|
| y       | year    |
| mon     | month   |
| w       | week    |
| d       | day     |
| h       | hour    |
| m       | minute  |
| s       | second  |


Some examples:

```py
from timewarp.timewarp import Timewarp

Timewarp('@y')  # The start of the current year.
Timewarp('@mon')  # The start (midnight of day 1) of the current month.
```

`+/-` moves the time relative to where it currently stands. These must be
combined with numeric values to specify how far to move:

```py
Timewarp('-1h')  # The current time minus one hour.
Timewarp('-3w')  # The current time minus three calendar weeks.
```

All of these operations can be composed arbitrarily to easily construct complex
points in time:

```py
Timewarp('-5y@y')  # Midnight of 1st January five years ago.
Timewarp('@y+3mon')  # The 1st of March of this year.
Timewarp('@y+6mon+23d')  # Midnight of the 23rd of June this year.
```

To get a native `datetime` object from a `Timewarp`, simply do:
```py
t = Timewarp('-6w@w')
d = t.to_datetime()
```

# Further Usage

 - `Timewarp` is conceptually subtractive (i.e. it revolves around the current
   time and applying modifications). You can also easily make it additive:
```py
Timewarp('+2000y+8mon', additive=True)  # 01/08/2000 00:00:00
```

 - `Timewarp` also supports pytz timezones:
```py
Timewarp('@w', timezone=pytz.GMT)  # The most recent Monday, GMT specific.
```
