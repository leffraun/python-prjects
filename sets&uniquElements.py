"""3. Sets & Unique Elements
Given a list of integers, write a function unique_sum(nums) that:

Returns the sum of all unique elements.

If the list is empty, raise a ValueError.

Example Input:
[1, 2, 2, 3, 4, 4]
Output:
10"""

original_list=(input("enter your list:")).split()
original_list=[int(num) for num in original_list]
def unique_list(original_list):
    if not original_list:
        raise ValueError("list is empty")
    unique_list=[]
    sum=0
    for num in original_list:
        if num not in unique_list:
            unique_list.append(num)

    for num in unique_list:
        sum+=num
    return sum

print(unique_list(original_list))


















