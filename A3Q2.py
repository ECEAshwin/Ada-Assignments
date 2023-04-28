def permute(S, op):
    if len(S) == 0:
        print(op, end=" ")
        return
    ch = S[0].lower()
    ch2 = S[0].upper()
    S = S[1:]
    permute(S, op+ch)
    permute(S, op+ch2)

S = input("Enter String : ")
permute(S, "")