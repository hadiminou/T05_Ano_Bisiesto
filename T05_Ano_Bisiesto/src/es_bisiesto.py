def esbisiesto(ano:int)->bool:
    res=False
    if ano%400==0 or (ano%4==0 and ano%100!=0):
        res=True
    return res