I = int(input("Enter no of Brricks : "))
p = 1
while I <= 10000:
    m = p*2
    z = p+m
    
    if I > p and I <= z :
        print("m won")
        break
    if I <= p:
        print("p won")
        break

    else:
        p = p+1
        I = I-z
if I > 10000:
    print("Too Heavy")