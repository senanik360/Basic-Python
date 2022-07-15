matrix = [[10,20,30], [20,30,40], [40,50,60]]

print(matrix) #print full matrix

print(matrix[2][1]) #print specific index

matrix[2][1]=70  #change the value of specific index

print(matrix)

for row in matrix :
    print("\n")
    for col in row :
        print(col, end = " ")   #  printing full matrix using loop