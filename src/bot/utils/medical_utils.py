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
