import array as ar
arr=ar.array('i',[9,8,7,6,5,4]);
for i in range(1,len(arr)):
    temp=arr[i];
    j=i-1;
    while j>=0 and temp<arr[j]:
        arr[j + 1] = arr[j];
        j=j-1;
    arr[j + 1] = temp;
print("Sorted array is:");
for i in range(len(arr)):
    print(arr[i]," ",end=" ");
