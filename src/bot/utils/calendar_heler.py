import datetime


async def fix_date_format(date: str) -> str:
    date = date.split("-")
    date.reverse()
    return ".".join(date[:2])


async def get_date_list() -> list:
    date_list = []
    today = datetime.date.today()
    date_list.append(await fix_date_format(str(today)))
    for i in range(13):
        today = today + datetime.timedelta(days=1)
        date_list.append(await fix_date_format(str(today)))
    return date_list

