arr = [63,3,21,25,55,681,812,116,7467,963,211,613,455,8598,1253]

def LS(arr,x) :
    for i in range (len(arr)) :
        if arr[i] == x :
            return f"The result you were looking for is the element {i+1}."
    return "No matching results found."
x  = int(input("Enter an item you want to search for : "))
result = LS(arr,x)
print(result)