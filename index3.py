def summa(lst):
    s = 0
    for i in lst:
        s += i
    return s

print(sum([1, 2, 3, 4, 5, 6, 7, 8, 9]))


def ayirma(a, b):
    print(a - b)

ayirma(5, 3)

def salom(ism="Tohir"):
    print(ism, "Salom xush kelibsiz!")   

salom("Salim")     

def tashtirish(ism, yosh, joy):
    print(f"Ism: {ism},\nyosh: {yosh}\njoy: {joy}")

tashtirish(yosh=21, joy="Namangan viloyat Chust tumani", ism="Muhammadjon", )    

def summa_args(*args):
    print(args)
    # return sum(args)

print(summa_args(1, 3, 5, 6, 7, 8, 9, "salom"))

def info(**kwargs):
    print(kwargs)

info(ism="Boburbek", familiya="Xoldorov", yosh=89, joy="Samarqand")

def test(a, b=10, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

test(1, 2, 3, 4, 5, 6, 7, 8, x=12, y="salom", baho=True)   


def bolish(a: int, b: int) -> int:
    return a / b

print(bolish(3, 2))