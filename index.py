# array = [10, 5, 4, 8, 9, 14, 7, 5, 10, 11, 8]
# counter = 1
# direction = 0
# temp = 0
# start = array[1]
# # print(start)
# for i in range(len(array)):
#     # i += 1
#     if counter == 3:
#         result = array[i]
#         x = i
#         print(result)
#         print(x)
#         break
#     # else:
#     if start >= array[i]:
#         direction = 0
#     else:
#         counter += 1
#         direction = 1
#     # else:
#     #     if start <= array[i]:
#     #         direction = 1
#     #         counter += 1
#     #     else:
#     #         direction = 0
#     start = array[i]

#     # if counter == 3:
#     # print(counter)
#     # break
#     # print(direction)
#     # print(counter)
#     # print(start)
#     # print(array[i])
# # print(start)


# from array import *

# xyz = array('i', [5, 4, 3, 4, 3, 4])

# print(xyz[1:])

# counter = 1
# direction = 0

# for i in range(len(xyz[1:])):
#     print(i)
#     if xyz[i] > xyz[i+1]:
#         direction = 0
#     else:
#         direction = 1
#     if direction == 1:
#         counter += 1
#     if counter == 3:
#         print(i)

# from array import *

ar = []

ar = [int(item) for item in input("List of space seprated values : ").split()]

direction = True
tempDir = True
counter = 0

arLength = len(ar)

if arLength > 0:
    for i in range(arLength):
        # if i < len(a):
        if counter == 3:
            result = ar[i]
            # print(result)
            print("Minimum", i + 1,
                  "Cut Down Required to achive Zig Zag Patter in this array.")
            break
        else:
            try:
                if ar[i] < ar[i+1]:
                    tempDir = True
                elif ar[i] > ar[i+1]:
                    tempDir = False
                else:
                    continue

            except IndexError as IE:
                print("Zig Zag pattern in this array is not possible")

        if direction != tempDir:
            counter += 1
            direction = tempDir

        if counter == 0:
            counter = 1
