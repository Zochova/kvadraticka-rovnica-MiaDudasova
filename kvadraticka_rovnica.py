a = int(input("Zadaj hodnotu a: "))
b = int(input("Zadaj hodnotu b: "))
c = int(input("Zadaj hodnotu c: "))

if a == 0:
    print("Toto nie je kvadratická rovnica.")
else:
    d = (b*b)-(4*a*c)
    if d > 0:
        d = d**(1/2)
        x1 = (-b + d)/(2*a)
        x2 = (-b - d)/(2*a)
        print("Korene kvadratickej rovnice sú:", int(x1), ",", int(x2))
    elif d == 0:
        x1 = (-b + d)/(2*a)
        x2 = (-b - d)/(2*a)
        print("Koreň kvadratickej rovnice je:", int(x1), ",", int(x2))
    elif d < 0:
        print("Rovnica má dve rôzne komplexné korene.")
    else:
        print("Error!")
