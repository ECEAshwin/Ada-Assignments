x = input("Enter String : ")
w = ""
for i in x:
    w = i + w
    print(w)
if (x == w):
    print("Yes")
else:
    print("No")

# Time Complexity = O(n)
# Space Complexcity = O(n)