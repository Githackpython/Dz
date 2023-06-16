def sravn(stroka):
    if stroka==stroka[::-1]:
        return True
    else:return False
while True:
    a=input("введи строку")
    print(sravn(a))