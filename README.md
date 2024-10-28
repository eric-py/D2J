# D2J

`D2J(Date to Jalali)` is a Python module for converting dates between the Gregorian and Jalali (Persian) calendars. This module also offers features for displaying Jalali dates as strings, showing day, month, and year separately, converting numbers to Persian, and determining the weekday.

## Features
- Supports various input formats, including date strings in multiple formats, `datetime.date` and `datetime.datetime` objects, tuples and lists, and Unix timestamps.
- Converts Gregorian dates to the Jalali calendar.
- Displays dates as strings or tuples.
- Shows the day, month, and year, as well as the month name, in Persian.
- Adds and subtracts days from a date.
- Calculates the day of the week and checks for leap years.

## Installation

To install, run the following command in the terminal:

```bash
pip install D2J
```

## Usage

### Creating a D2J Object

To create a `D2J` object, you can pass various types of input as a date. Below are examples of supported input types:

```python
from d2j import D2J
import datetime

# Using different string formats
date1 = D2J("2024-10-27")
date2 = D2J("27-10-2024")
date3 = D2J("10/27/2024")

# Using a datetime.date object
date4 = D2J(datetime.date(2024, 10, 27))

# Using a datetime.datetime object
date5 = D2J(datetime.datetime(2024, 10, 27, 12, 30))

# Using a tuple or list
date6 = D2J((2024, 10, 27))
date7 = D2J([2024, 10, 27])

# Using a Unix timestamp
date8 = D2J(1730057449)
```

### Methods in D2J

#### 1. `as_tuple(persian_numbers=False)`

This method returns the Jalali date as a tuple `(year, month, day)`. If `persian_numbers=True`, the numbers are displayed in Persian.

```python
jalali_tuple = date1.as_tuple()
jalali_tuple_persian = date1.as_tuple(persian_numbers=True)
```

#### 2. `as_string(sep="-", persian_numbers=False)`

This method returns the Jalali date as a string. `sep` specifies the separator between the year, month, and day (default is `"-"`). If `persian_numbers=True`, the numbers are displayed in Persian.

```python
jalali_string = date1.as_string()
jalali_string_custom_sep = date1.as_string(sep="/")
jalali_string_persian = date1.as_string(persian_numbers=True)
```

#### 3. `as_verbose(persian_numbers=False)`

This method returns a descriptive string of the Jalali date, including the day, month name in Persian, and year. If `persian_numbers=True`, the numbers are displayed in Persian.

```python
jalali_verbose = date1.as_verbose()
jalali_verbose_persian = date1.as_verbose(persian_numbers=True)
```

#### 4. `to_gregorian(persian_numbers=False)`

This method returns the original Gregorian input date, useful for retrieving the initial input date. If `persian_numbers=True`, the numbers are displayed in Persian.

```python
gregorian_date = date1.to_gregorian()
gregorian_date_persian = date1.to_gregorian(persian_numbers=True)
```

#### 5. `get_day_of_week()`

This method returns the day of the week (e.g., "Monday", "Tuesday", etc.) for the input Gregorian date.

```python
day_of_week = date1.get_day_of_week()
```

#### 6. `is_leap_year()`

This method checks if the Jalali year is a leap year.

```python
is_leap = date1.is_leap_year()
```

#### 7. `add_days(days)`

This method returns a new date by adding a specified number of days to the current date.

```python
new_date = date1.add_days(10)
```

#### 8. `subtract_days(days)`

This method returns a new date by subtracting a specified number of days from the current date.

```python
new_date = date1.subtract_days(10)
```

#### 9. `get_day(persian_numbers=False)`

Returns the day of the Jalali date. If `persian_numbers=True`, the day is displayed in Persian.

```python
day = date1.get_day()
day_persian = date1.get_day(persian_numbers=True)
```

#### 10. `get_month(persian_numbers=False)`

Returns the month of the Jalali date. If `persian_numbers=True`, the month is displayed in Persian.

```python
month = date1.get_month()
month_persian = date1.get_month(persian_numbers=True)
```

#### 11. `get_year(persian_numbers=False)`

Returns the year of the Jalali date. If `persian_numbers=True`, the year is displayed in Persian.

```python
year = date1.get_year()
year_persian = date1.get_year(persian_numbers=True)
```

### Examples

Below are some examples of using the methods in the `D2J` module:

```python
# Convert date to Jalali string with "/" separator
print(date1.as_string(sep="/"))

# Display the Jalali date in verbose form
print(date1.as_verbose())

# Convert the Jalali date back to Gregorian
print(date1.to_gregorian())

# Add 15 days to the date
print(date1.add_days(15).as_string())
print(date1.add_days(15).as_string(persian_numbers=True, sep='/'))

# Get the day of the week
print(date1.get_day_of_week())

# Check if the year is a leap year
print(date1.is_leap_year())
```

## License

This project is licensed under the MIT License. For more details, refer to the `LICENSE` file.