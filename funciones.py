def suma(a:int,b:int) -> int:
    try:
      print(a/b)
    except ZeroDivisionError:
        print("no se puede dividir entre cero ")
    except TypeError:
        print("no se puede dividir entre cero ")
    except exception:
        print("hubo otro error")
    
suma(1,0)
    