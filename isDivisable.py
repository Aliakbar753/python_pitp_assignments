def isDisiable(num):
    if num%5==0:
        return num,"is divisible by 5"
    else:
        return num,"is not divisible by 5"

print(isDisiable(11))