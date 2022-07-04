import array as ar
import sys
sys.setrecursionlimit(10**6);
def Merge(left,right,mid):
    left_size = mid - left + 1;
    Left=[0]*(left_size + 1);
    right_size = right - mid;
    Right=[0]*(right_size + 1);

    for i in range(0,left_size):
        Left[i]=arr[i+left];

    for i in range(0,right_size):
        Right[i]=arr[i+mid+1];

        Left[left_size]=Right[right_size]=sys.maxsize;
        left_index=0;
        right_index=0;

    for j in range(left,right+1):
            if(Left[left_index] <= Right[right_index]):
                arr[j]=Left[left_index];
                left_index+=1;      #left_index+1;
            else:
                arr[j]=Right[right_index];
                right_index+=1;     #right_index+1;
def MergeSort(left,right):
    mid = int((left + right)/2);
    if(left==right):
        return;
    MergeSort(left,mid);
    MergeSort(mid+1,right);
    Merge(left,right,mid);
global arr;
arr=ar.array('i',[]);
n=int(input("Enter the number of elements"));

for i in range(n):
    x=int(input("Enter the number"));
    arr.append(x);
print(arr);
MergeSort(0,n-1);
print("Sorted array is:");
print(arr);
