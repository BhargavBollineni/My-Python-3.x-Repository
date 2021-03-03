

def details(name, **data):
    print(name)

    for i,j in data.items():
      print(i,j)
details(input('enter the Name : '), age = int(input('enter the age : ')), city = input('enter the city name : '),
                                                                   col = input('enter the col name : '))



