import re


async def is_phone_number_valid(number: str):
    pattern = r"^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$"
    res = re.fullmatch(pattern, number)
    return True if res else False
