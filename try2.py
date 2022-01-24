while True:
    try:
        sayi=int(input("Bana sayı ver"))
        sayi2=int(input("Bana 2. sayıyı ver"))
        print(sayi/sayi2)
    except ValueError:
        print("Ama ben senden yazı girmeni istedim!")
    except ZeroDivisionError:
        print("Puuuuuu bunda da hata yapmazsın be!")



