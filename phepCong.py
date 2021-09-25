import math


def cong(a, b, w, c):
    e = 0
    for i in range(len(a)-1, -1, -1):
        c[i] = a[i] + b[i] + e
        if c[i] >= pow(2, w):
            e = 1
            c[i] = c[i] % pow(2, w)
        else:
            e = 0
    return e


def chuyenDoi(x, w, t, res):
    for i in range(t-1,-1,-1):# chay vong lap tu t-1 den 0
        tmp = math.pow(2, i*w) #tinh 2^(i*w)
        res.append(math.floor(x/tmp)) #them phan nguyen vao mang ket qua
        x = x % tmp #gan lai phan du cho x


def main():
    p = 2147483649
    w = 8
    m = math.ceil(math.log(p, 2))
    t = math.ceil(m/w)
    print("nhap a nguyen:")
    a = int(input())
    print("nhap b nguyen:")
    b = int(input())
    resa = []
    resb = []
    chuyenDoi(a, w, t, resa)
    print("A= ", resa)
    chuyenDoi(b, w, t, resb)
    print("B= ", resb)
    c = [0]*t
    e = cong(resa, resb, w, c)
    print("ket qua sau khi cong la:")
    print("e=%d" %e, ",", c)


if __name__ == '__main__':
    main()
