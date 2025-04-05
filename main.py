# def remove_element(num1,val):
#     l = len(num1)
#     while val in num1 and l>0:
#             num1.pop()
#     return len(num1)

# # Test case 1: Removing a single instance of a value (1) in the middle of the list.
# nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# val1 = 1
# print("\nRemove a single instance of value", val1, "in the middle of the list.")
# print("BEFORE:", nums1)
# new_length1 = remove_element(nums1, val1)
# print("AFTER:", nums1, "\nNew length:", new_length1)
# print("-----------------------------------")

# # Test case 2: Removing a value that's located at the end of the list.
# nums2 = [1, 2, 3, 4, 5, 6]
# val2 = 6
# print("\nRemove value", val2, "that's located at the end of the list.")
# print("BEFORE:", nums2)
# new_length2 = remove_element(nums2, val2)
# print("AFTER:", nums2, "\nNew length:", new_length2)
# print("-----------------------------------")

# # Test case 3: Removing a value that's located at the start of the list.
# nums3 = [-1, -2, -3, -4, -5]
# val3 = -1
# print("\nRemove value", val3, "that's located at the start of the list.")
# print("BEFORE:", nums3)
# new_length3 = remove_element(nums3, val3)
# print("AFTER:", nums3, "\nNew length:", new_length3)
# print("-----------------------------------")

# # Test case 4: Attempting to remove a value from an empty list.
# nums4 = []
# val4 = 1
# print("\nAttempt to remove value", val4, "from an empty list.")
# print("BEFORE:", nums4)
# new_length4 = remove_element(nums4, val4)
# print("AFTER:", nums4, "\nNew length:", new_length4)
# print("-----------------------------------")

# # Test case 5: Removing all instances of a repeated value.
# nums5 = [1, 1, 1, 1, 1]
# val5 = 1
# print("\nRemove all instances of value", val5, "from the list.")
# print("BEFORE:", nums5)
# new_length5 = remove_element(nums5, val5)
# print("AFTER:", nums5, "\nNew length:", new_length5)
# print("-----------------------------------")


#
# def func(a):
#     print('func1')
#
# def func(a,b):
#     print('func2')
#
# def func():
#     print('func3')
#
# func(2)

def func(n):
    q = n

    def rec(q):
        r = 2/q
        if r == 1:
            return False
        if q == 1 and r == 0:
            return True
        return rec(2 % q)

    print(rec(q))


# func(8)

