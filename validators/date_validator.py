import datetime

from lexicon import lexicon


def date_validator(user_date: str, current_date: datetime) -> datetime.date:
    try:
        day, month = [int(i) for i in user_date.split('.')]
    except:
        raise Exception(lexicon.DATE_IS_NOT_CORRECT)

    max_date = (current_date + datetime.timedelta(days=5)).date()
    dt = datetime.date(day=day, month=month, year=current_date.year)

    if dt < current_date.date() or dt > max_date:
        raise Exception(
            lexicon.DATE_VALIDATOR.format(current_date.day, current_date.month, max_date.day, max_date.month))

    return dt
