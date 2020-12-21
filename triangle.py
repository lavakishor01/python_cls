# Range of the triangle
size = int(input("Enter the range: /t "))

for i in range(size):
    for j in range((size-i)-1):
        print(end=" ")
    # for j in range(i+1):
    #     print("*",end=" ")
    # print()