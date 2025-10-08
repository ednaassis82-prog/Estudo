try:
    a = int(input("numerador : "))
    b = int(input("denominador : "))
    d = a / b

except ZeroDivisionError:
    print("Não é possivel dividir por zero. ")

else:
    print(f"o resultado é: {d}")

finally:
    print("seu programa foi executado. ")
     