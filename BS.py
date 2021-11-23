arr = sorted([63,3,21,25,55,681,812,116,7467,963,211,613,455,8598,1253,52])
def BS(arr,start,end,x) :
    if end>=start :
        mid = start +(end-start)//2
        if(arr[mid] == x) :
            return f"A result was found at the element {mid+1}"
        elif(arr[mid] < x) :
            return BS(arr,mid+1,end,x)
        elif(arr[mid] > x) :
            return BS(arr,start,mid-1,x)
    else :
        return "No matching results found."


x = int(input("Enter an item to search for  : "))
start = 0
end = len(arr)-1
result = BS(arr,start,end,x)
print(result)
