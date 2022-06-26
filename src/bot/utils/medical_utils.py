from bot.data.dict_data import RECOMENDATIONS
from bot.services.fuzzy_test.main import get_fuzzy_ill_system


async def get_ims(height, weight):
    ims = float(weight) / ((float(height) / 100) ** 2)
    if ims <= 16.0:
        return f"{ims}\nВыраженный дефицит массы тела"
    elif 16 < ims <= 18.5:
        return f"{ims}\nНедостаточная (дефицит) масса тела"
    elif 18.5 < ims <= 25.0:
        return f"{ims}\nНорма"
    elif 25 < ims <= 30:
        return f"{ims}\nИзбыточная масса тела (предожирение)"
    elif 30 < ims <= 35:
        return f"{ims}\nОжирение 1 степени"
    elif 35 < ims <= 40:
        return f"{ims}\nОжирение 2 степени"
    else:
        return f"{ims}\nОжирение 3 стпени"


def get_recomendations(test_result):
    values = list(test_result.values())
    key = list(test_result.keys())[values.index(max(values))]
    return RECOMENDATIONS[key]


if __name__ == '__main__':
    get_recomendations(get_fuzzy_ill_system({
        "temp": True,
        "skin_t": True,
        "lymph": True,
        "weakness": True,
        "edema": True,
        "nausea": True,
        "stiffness": True,
        "noj": True,
        "back_pain": True,
        "mus_pain": True,
        "cancer": True,
    }))