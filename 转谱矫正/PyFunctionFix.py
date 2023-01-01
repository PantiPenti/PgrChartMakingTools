import os
import sys

def round(num, digit = 0):
    if isinstance(num, int):
        num = float(num)
 
    if not isinstance(num, float):
        print("TypeError: a float or int is required")
        return
 
    left, right = str(num).split('.')
 
    if digit >= len(right):
        return num
    else:
        # 四舍五入
        right_int = int(right[digit])
        if int(right[digit]) >= 5:
            right_int += 1
        ans = "{}.{}".format(left, right_int)
        return float(ans)

def gcd(a,b):
    if b==0:    return a
    else:   return gcd(b,a%b)

def intList(List):
    Cur = 0
    while Cur < len(List):
        if List[Cur].isdigit():
            List[Cur] = int(List[Cur])
        Cur = Cur + 1
    return List

def FixDir():
    Path = os.path.dirname(os.path.abspath(sys.argv[0]))
    os.chdir(Path)