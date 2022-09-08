my_list = [223, 334, 567, 555, 3456, 65, 23,
           40, 39, 52, 876, 22, 100, 10, 50, 34]
n = int(input("Enter a number :"))
result = list(filter(lambda x: (x % n == 0), my_list))
print("Numbers divisable by the Given number  are : ", result)
