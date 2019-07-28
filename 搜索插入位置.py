list1=[1,3,5,6]
num=5

# def searchInsert(nums, target):
#     while
#     mid=len(target)>>1
#     nums=nums

def search(left,right):

    mid=(left+right)>>1
    if list1[mid]==num:
        return mid
    if left==right-1:
        return right
    if num>list1[mid]:
        search(mid,right)
    else:
        search(left,mid)
res=search(0,len(list1)-1)
print(res)