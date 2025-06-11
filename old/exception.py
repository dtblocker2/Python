try:
    num = int(input("a:"))
    den = int(input("b:"))
    result = num/den
except ZeroDivisionError:
    print("can't divide by zero")
except ValueError:
    print("input numbers only")
except Exception:
    print("something went wrong")
else:
    print(result)
finally:
    print("this will be always shown")