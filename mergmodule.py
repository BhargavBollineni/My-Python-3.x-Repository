

def details(name, **data):
    print(name)

    for i,j in data.items():
      print(i,j)
details(__name__)



def fib(n):
    a = 0
    b = 1

    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)
#fib(int(input('enter the num :', n)))

def main():
    print('in mergModule main')
    print(details)
    print(fib(10))

if __name__ == '__main__':
    main()