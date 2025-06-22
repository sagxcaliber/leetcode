s = [4, 2, 0, 2, 5]


# def trap(height):
#     stack = []
#     water = 0
#
#     for i in range(len(height)):
#         # While current height is greater than height of top of stack
#         while stack and height[i] > height[stack[-1]]:
#             bottom = stack.pop()
#
#             if not stack:
#                 break  # No left wall to trap water
#
#             left = stack[-1]
#             width = i - left - 1
#             bounded_height = min(height[left], height[i]) - height[bottom]
#             water += width * bounded_height
#
#         stack.append(i)
#
#     return water


def trap(height):
    stack = []
    water = 0

    for i in range(len(height)):

        while stack and height[i] > height[stack[-1]]:

            bottom = stack.pop()

            if not stack:
                break

            left = stack[-1]
            width = i - left - 1
            bottom_height = min(height[left], height[i]) - height[bottom]
            water += bottom_height* width

        stack.append(i)
    return water
trap([4,2,0,2,5])