import datetime
from enum import Enum

class PersianMonth(Enum):
    FARVARDIN = ("فروردین", 1)
    ORDIBEHESHT = ("اردیبهشت", 2)
    KHORDAD = ("خرداد", 3)
    TIR = ("تیر", 4)
    MORDAD = ("مرداد", 5)
    SHAHRIVAR = ("شهریور", 6)
    MEHR = ("مهر", 7)
    ABAN = ("آبان", 8)
    AZAR = ("آذر", 9)
    DEY = ("دی", 10)
    BAHMAN = ("بهمن", 11)
    ESFAND = ("اسفند", 12)

    def __init__(self, persian_name, number):
        self.persian_name = persian_name
        self.number = number

    @classmethod
    def from_number(cls, number):
        for month in cls:
            if month.number == number:
                return month
        raise ValueError(f"{number} is not a valid Persian month number")

class D2J:
    PERSIAN_NUMBERS = "۰۱۲۳۴۵۶۷۸۹"
    DATE_FORMATS = ('%Y-%m-%d', '%d-%m-%Y', '%m/%d/%Y', '%Y/%m/%d', '%d.%m.%Y', '%Y.%m.%d')

    def __init__(self, date_input):
        self.gregorian_date = self._parse_input(date_input)
        self.jalali_date = self._convert_to_jalali(self.gregorian_date)
    
    def _parse_input(self, date_input):
        if isinstance(date_input, datetime.date):
            return date_input
        elif isinstance(date_input, datetime.datetime):
            return date_input.date()
        elif isinstance(date_input, (tuple, list)) and len(date_input) == 3:
            year, month, day = date_input
            return datetime.date(year, month, day)
        elif isinstance(date_input, (int, float)):
            return datetime.date.fromtimestamp(date_input)
        elif isinstance(date_input, str):
            for fmt in self.DATE_FORMATS:
                try:
                    return datetime.datetime.strptime(date_input, fmt).date()
                except ValueError:
                    continue
            raise ValueError("Unsupported date string format. Try YYYY-MM-DD or similar formats.")
        else:
            raise TypeError("Unsupported date type. Please use datetime.date, datetime.datetime, tuple, timestamp, or string.")

    def _convert_to_jalali(self, gregorian_date):
        gy, gm, gd = gregorian_date.year, gregorian_date.month, gregorian_date.day
        
        if not self._is_valid_gregorian_date(gy, gm, gd):
            raise ValueError("Invalid Gregorian date.")

        days_in_month = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        gy2 = gy + 1 if gm > 2 else gy
        
        days = 355666 + (365 * gy) + ((gy2 + 3) // 4) - ((gy2 + 99) // 100) + ((gy2 + 399) // 400) + gd + days_in_month[gm - 1]
        jy = -1595 + (33 * (days // 12053))
        days %= 12053
        jy += 4 * (days // 1461)
        days %= 1461

        if days > 365:
            jy += (days - 1) // 365
            days = (days - 1) % 365

        if days < 186:
            jm = 1 + (days // 31)
            jd = 1 + (days % 31)
        else:
            jm = 7 + ((days - 186) // 30)
            jd = 1 + ((days - 186) % 30)

        return jy, jm, jd

    @staticmethod
    def _is_valid_gregorian_date(year, month, day):
        try:
            datetime.date(year, month, day)
            return True
        except ValueError:
            return False

    def _to_persian_numbers(self, text):
        return ''.join(self.PERSIAN_NUMBERS[int(d)] if d.isdigit() else d for d in text)

    def as_tuple(self, persian_numbers=False):
        if persian_numbers:
            return tuple(self._to_persian_numbers(str(x)) for x in self.jalali_date)
        return self.jalali_date

    def as_string(self, sep="-", persian_numbers=False):
        jy, jm, jd = self.jalali_date
        result = f"{jy}{sep}{jm:02d}{sep}{jd:02d}"
        return self._to_persian_numbers(result) if persian_numbers else result

    def as_verbose(self, persian_numbers=False):
        jy, jm, jd = self.jalali_date
        month = PersianMonth.from_number(jm)
        result = f"{jd} {month.persian_name} {jy}"
        return self._to_persian_numbers(result) if persian_numbers else result

    def to_gregorian(self, persian_numbers=False):
        jy, jm, jd = self.jalali_date
        if jm < 1 or jm > 12 or jd < 1 or jd > 31:
            raise ValueError("Invalid Jalali date.")
    
        jy += 1595
        days = -355668 + (365 * jy) + ((jy // 33) * 8) + (((jy % 33) + 3) // 4) + jd
        if jm < 7:
            days += (jm - 1) * 31
        else:
            days += ((jm - 7) * 30) + 186
    
        gy = 400 * (days // 146097)
        days %= 146097
        if days > 36524:
            days -= 1
            gy += 100 * (days // 36524)
            days %= 36524
            if days >= 365:
                days += 1
    
        gy += 4 * (days // 1461)
        days %= 1461
        if days > 365:
            gy += (days - 1) // 365
            days = (days - 1) % 365
    
        gd = days + 1
        if (gy % 4 == 0 and gy % 100 != 0) or (gy % 400 == 0):
            gm_days = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]
        else:
            gm_days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
    
        gm = next(i for i, v in enumerate(gm_days) if v >= gd)
        gd = gd - gm_days[gm - 1]
    
        result = f"{gy}-{gm:02d}-{gd:02d}"
        return self._to_persian_numbers(result) if persian_numbers else result

    def get_day_of_week(self):
        days = ["دوشنبه", "سه‌شنبه", "چهارشنبه", "پنج‌شنبه", "جمعه", "شنبه", "یکشنبه"]
        return days[self.gregorian_date.weekday()]

    def is_leap_year(self):
        year = self.jalali_date[0]
        return (year % 33 in [1, 5, 9, 13, 17, 22, 26, 30])

    def add_days(self, days):
        new_date = self.gregorian_date + datetime.timedelta(days=days)
        return D2J(new_date)

    def subtract_days(self, days):
        new_date = self.gregorian_date - datetime.timedelta(days=days)
        return D2J(new_date)

    def get_day(self, persian_numbers=False):
        return self._get_date_component(2, persian_numbers)

    def get_month(self, persian_numbers=False):
        return self._get_date_component(1, persian_numbers)

    def get_year(self, persian_numbers=False):
        return self._get_date_component(0, persian_numbers)

    def _get_date_component(self, index, persian_numbers=False):
        component = self.jalali_date[index]
        return self._to_persian_numbers(str(component)) if persian_numbers else component