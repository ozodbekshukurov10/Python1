def yoshbolasiz():
    print('siz yosh bolasiz')


def yosh():
    print('siz yoshsiz')



def yaxshi_holatda():
    print('siz yaxshisiz')
 
def ortacha():
    print('siz ortacha yoshdasiz')

def yaxshi():
    print('siz ortachadan baland lekn qaridan pastroq')



def boladi():
    print('boladi')

def qari():
    print('siz qarisiz')

def ota_qari():
    print('ota qari')

def super_qari():
    print('super qari')

def Dinazavr_korgan():
    print('dinazavr korgan')

def yura_daavri():
    print('yura davri')
while True:
    yosh_soni = int(input('yoshingizni kiriting: '))

    if yosh_soni in range(0, 12):
        yoshbolasiz()
    elif yosh_soni in range(12, 18):
        yosh()
    elif yosh_soni in range(18, 27):
        ortacha()
    elif yosh_soni in range(27, 35):
        yaxshi()
    elif yosh_soni in range(35, 50):
        yaxshi_holatda()
    elif yosh_soni in range(50, 60):
        boladi()
    elif yosh_soni in range(60, 75):
        qari()
    elif yosh_soni in range(75,100):
        ota_qari()
    elif yosh_soni in range(100, 120):
        super_qari()
    elif yosh_soni in range(120, 150):
        Dinazavr_korgan()
    elif yosh_soni in range(150, 200):
        yura_daavri()
    else:
        print('siz odam emasiz')

    chiqish = input('davom etamizmi: ').lower()

    if chiqish != 'ha':
        print('dastur tugadi')
        break
    elif chiqish != 'yoq':
        continue