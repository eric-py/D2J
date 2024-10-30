# D2J

`D2J (Date to Jalali)` is a Python module designed for converting dates between the Gregorian and Jalali (Persian) calendars. It offers a range of methods for displaying Jalali dates as strings, retrieving day, month, and year components individually, converting numbers to Persian, and determining the day of the week.

## Features

- **Supports various input types**: Including date strings in multiple formats, `datetime.date` and `datetime.datetime` objects, tuples, lists, and Unix timestamps.
- **Convert Gregorian to Jalali**: Direct conversion of Gregorian dates to Jalali dates.
- **Display as String or Tuple**: Option to display dates as custom strings or to retrieve day, month, and year separately.
- **Add or Subtract Days**: Easily add or subtract a specific number of days from a date.
- **Calculate Day of the Week and Leap Year**: Determine the day of the week and check if the Jalali year is a leap year.
- **New Features**: Includes `__str__`, `__repr__`, `now`, and `get_date` methods for enhanced display and retrieval of original input dates.

## Installation

To install this library, run the following command in your terminal:

```bash
pip install D2J
```

## Using the D2J Class

### Creating a D2J Object

To create a `D2J` object, you can pass various types of date inputs. These inputs include date strings in different formats, `datetime.date` object, Unix timestamp, and tuples or lists containing the year, month, and day.

Examples of creating a `D2J` object with different inputs:

```python
from d2j import D2J
import datetime

# Using various string formats
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

### Methods in the D2J Class

#### 1. `now()`
This class method returns a `D2J` object with the system’s current date.

```python
current_date = D2J.now()
```

#### 2. `__str__()` and `__repr__()`
These methods provide a string representation of the `D2J` object and return the Jalali date by default.

```python
print(date1)  # Outputs the date as a string
repr(date1)   # Shows the string representation with `repr`
```

#### 3. `get_date(sep="-", persian_numbers=False)`
Returns the original input date (Gregorian or Jalali) in its initial format. The `sep` parameter specifies the separator, and `persian_numbers` can be set to True to display numbers in Persian.

```python
input_date = date1.get_date()
input_date_persian = date1.get_date(persian_numbers=True)
```

#### 4. `to_gregorian(sep="-", persian_numbers=False)`
Converts the Jalali date to Gregorian and returns it as a string. If the input date was already Gregorian, it returns the original date unchanged.

```python
gregorian_date = date1.to_gregorian()
gregorian_date_persian = date1.to_gregorian(persian_numbers=True)
```

#### 5. `as_tuple(persian_numbers=False)`
Returns the Jalali date as a tuple `(year, month, day)`. If `persian_numbers=True`, the numbers are displayed in Persian.

```python
jalali_tuple = date1.as_tuple()
jalali_tuple_persian = date1.as_tuple(persian_numbers=True)
```

#### 6. `as_string(sep="-", persian_numbers=False)`
Returns the Jalali date as a string. The `sep` parameter specifies the separator to use (default is `"-"`). If `persian_numbers=True`, the numbers are displayed in Persian.

```python
jalali_string = date1.as_string()
jalali_string_custom_sep = date1.as_string(sep="/")
jalali_string_persian = date1.as_string(persian_numbers=True)
```

#### 7. `as_verbose(persian_numbers=False)`
Returns the Jalali date as a verbose string, including the day, Persian month name, and year. If `persian_numbers=True`, numbers are displayed in Persian.

```python
jalali_verbose = date1.as_verbose()
jalali_verbose_persian = date1.as_verbose(persian_numbers=True)
```

#### 8. `get_day_of_week()`
Returns the name of the weekday for the Gregorian input date in Persian (e.g., "Monday" as "دوشنبه").

```python
day_of_week = date1.get_day_of_week()
```

#### 9. `is_leap_year()`
Checks if the Jalali year is a leap year.

```python
is_leap = date1.is_leap_year()
```

#### 10. `add_days(days)`
Adds the specified number of days to the current date and returns a new `D2J` object with the updated date.

```python
new_date = date1.add_days(10)
```

#### 11. `subtract_days(days)`
Subtracts the specified number of days from the current date and returns a new `D2J` object with the updated date.

```python
new_date = date1.subtract_days(10)
```

#### 12. `get_day(persian_numbers=False)`
Returns the day component of the Jalali date. If `persian_numbers=True`, the day is displayed in Persian.

```python
day = date1.get_day()
day_persian = date1.get_day(persian_numbers=True)
```

#### 13. `get_month(persian_numbers=False)`
Returns the month component of the Jalali date. If `persian_numbers=True`, the month is displayed in Persian.

```python
month = date1.get_month()
month_persian = date1.get_month(persian_numbers=True)
```

#### 14. `get_year(persian_numbers=False)`
Returns the year component of the Jalali date. If `persian_numbers=True`, the year is displayed in Persian.

```python
year = date1.get_year()
year_persian = date1.get_year(persian_numbers=True)
```

### Practical Examples

Here are a few examples to illustrate how to use various methods in the `D2J` module:

```python
# Creating an object with the current system date
current_date = D2J.now()

# Displaying the Jalali date as a string with "/" as the separator
print(current_date.as_string(sep="/"))

# Displaying the Jalali date in verbose form
print(current_date.as_verbose())

# Converting the Jalali date to Gregorian
print(current_date.to_gregorian())

# Adding 15 days to the date
print(current_date.add_days(15).as_string())
print(current_date.add_days(15).as_string(persian_numbers=True, sep='/'))

# Retrieving the weekday
print(current_date.get_day_of_week())

# Checking if the Jalali year is a leap year
print(current_date.is_leap_year())
```

---

## License

This project is licensed under the MIT License. For more details, please refer to the `LICENSE` file.