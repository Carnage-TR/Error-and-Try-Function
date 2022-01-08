while True:
    try:
        sayi=int(input("Bana sayı ver"))
        sayi2=int(input("Bana 2. sayıyı ver"))
        print(sayi/sayi2)
    except ValueError:
        print("lan ben sana sayı gir dedim sen neden isim giriyon lan *********. Seni ben Özgürlük heykelinin yanmayan meşalesinde...")
    except ZeroDivisionError:
        print("Puuuuuu bunda hata yapmazsın be pirenses be!")



