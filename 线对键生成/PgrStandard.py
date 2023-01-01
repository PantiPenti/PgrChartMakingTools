import PyFunctionFix as py

LineEventType = ["alphaEvents","moveXEvents","moveYEvents","rotateEvents","speedEvents"]

def TimeJudge(Time1, Time2):
    if Time1[0] == Time2[0]:
        if Time1[2] == Time2[2]:
            if Time1[1] == Time2[1]:   return 2
            elif Time1[1] > Time2[1]:    return 3
            else:    return 1
        else:
            if Time1[1] * Time2[2] > Time1[2] * Time2[1]:   return 3
            else:    return 1
    elif Time1[0] > Time2[0]:    return 3
    else:    return 1

def TimeAdd(Time1, Time2):
    t1up = Time1[0] * Time1[2] + Time1[1]
    t2up = Time2[0] * Time2[2] + Time2[1]
    tup = t1up * Time2[2] + t2up  *Time1[2]
    tdown = Time1[2] * Time2[2]
    g = py.gcd(tup, tdown)
    tup, tdown = tup // g, tdown // g
    return [tup // tdown, tup % tdown, tdown]

def TimeMinus(Time1, Time2):
    t1up = Time1[0] * Time1[2] + Time1[1]
    t2up = Time2[0] * Time2[2] + Time2[1]
    tup = t1up * Time2[2] - t2up * Time1[2]
    tdown = Time1[2] * Time2[2]
    g = py.gcd(tup, tdown)
    tup, tdown = tup // g, tdown // g
    return [tup // tdown, tup % tdown, tdown]

def time(obj):
    if isinstance(obj, str):    return time(obj.split(":"))
    elif isinstance(obj, list):
        obj = py.intList(obj)
        if len(obj) == 1: return [obj[0],0,1]
        elif len(obj) == 3: return obj
        else: 
            print("时间转换出错：必须为符合条件的字符串或列表！")
            return
    else:
        print("时间转换出错：必须为符合条件的字符串或列表！")
        return
