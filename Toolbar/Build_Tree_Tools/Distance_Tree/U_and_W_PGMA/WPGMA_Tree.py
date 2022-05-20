import numpy as np
'''
Matrix=[['x','a','b','c','d','e'],
        ['a',0,3,4,5,6],
        ['b',3,0,6,8,11],
        ['c',4,6,0,7,6],
        ['d',5,8,7,0,4],
        ['e',6,11,6,4,0]]
Matrix = [['x','ba','c','d','e'],
        ['ba' ,0, 5.0 ,6.5, 8.5],
        ['c' ,5.0, 0, 7 ,6],
        ['d' ,6.5 ,7 ,0 ,4],
        ['e', 8.5, 6, 4, 0]]
Matrix = [['x','ed','ba','c'],
        ['ed' ,0 ,7.5, 6.5],
        ['ba' ,7.5 ,0 ,5.0],
        ['c' ,6.5, 5.0, 0]]
Matrix = [['x','cba','ed'],
        ['cba', 0 ,7.0],
        ['ed' ,7.0, 0]]
'''

def zeros(A):
    zero_Matrix=[]
    for i in range(A[0]):
        rows=[]
        for j in range(A[1]):
            rows.append(0)
        zero_Matrix.append(rows)
    return zero_Matrix

def find_location(element1, element2, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[0][j]== element1 and matrix[i][0] == element2:
                loc=(matrix[i][j], i, j)

    return loc

def find_min(Matrix):
    minn=1000
    loc_min=0
    for i in range(len(Matrix)):
        for j in range(len(Matrix[i])):
            try:
                a=float(Matrix[i][j])
                if a <= minn and a !=0:
                    minn=Matrix[i][j]
                    loc_min= i,j
            except:
                continue

    return minn, loc_min[0], loc_min[1]
def transfer_Matrix(Matrix):
    Matrix_rec = []
    for i in Matrix:
        lst = []
        for j in i:
            lst.append(j)
        Matrix_rec.append(lst)
    return Matrix_rec


def calculate_distances(Matrix):
    Matrix_rec=transfer_Matrix(Matrix)
    #Generate New Node
    min_of_matrix, min_i, min_j = find_min(Matrix)
    nod=(Matrix[min_i][0], min_of_matrix/2, Matrix[0][min_j])
    will_express=(Matrix[min_i][0]+ Matrix[0][min_j],Matrix[min_i][0], min_of_matrix/2, Matrix[0][min_j])
    #print(will_express)

    #RECALCULATE DISTANCES

    #Create Empty Matrix
    size_of_New_Matrix=len(Matrix), len(Matrix[0])
    zero_Matrix=zeros([size_of_New_Matrix[0]-1, size_of_New_Matrix[1]-1])

    #Manipulate Sides

    names=Matrix[0]
    names.remove(nod[0])
    names.remove(nod[2])
    names.insert(1,nod[0]+nod[2])
    for i in range(len(zero_Matrix)):
        for j in range(len(zero_Matrix[0])):
            if i==0:
                zero_Matrix[i][j] = names[j]
            elif i !=0 and j==0:
                zero_Matrix[i][j] = names[i]
    #Manipulute Inside late
    for i in range(len(zero_Matrix)):
        for j in range(len(zero_Matrix[0])):
            if i !=0 and j !=0:
                if i!=j:
                    if zero_Matrix[i][0]==nod[0]+nod[2] or zero_Matrix[0][j]==nod[0]+nod[2]:
                        if zero_Matrix[i][0]==nod[0]+nod[2]:
                            p1 = find_location(zero_Matrix[0][j],nod[0], Matrix_rec)
                            p2 = find_location(zero_Matrix[0][j], nod[2], Matrix_rec)
                            zero_Matrix[i][j]=(p1[0] + p2[0])/2
                        if zero_Matrix[0][j]==nod[0]+nod[2]:
                            p1 = find_location(zero_Matrix[i][0], nod[0], Matrix_rec)
                            p2 = find_location(zero_Matrix[i][0], nod[2], Matrix_rec)
                            zero_Matrix[i][j] = (p1[0] + p2[0]) / 2
                    else:
                        el= find_location(zero_Matrix[i][0],zero_Matrix[0][j], Matrix_rec)
                        zero_Matrix[i][j]=el[0]
    return zero_Matrix, will_express

def generate_route_list_of_WPGMA_Tree(Matrix):
    counter=0
    route_list=[]

    for i in range(len(Matrix)):
        for j in range(len(Matrix[0])):
            if i == j and i != 0 and j !=0:
                Matrix[i][j]=0

    while True:
        try:
            if counter==0:
                counter +=1
                a, b=calculate_distances(Matrix)
                route_list.append(b)
            else:
                a, b=calculate_distances(a)
                route_list.append(b)
        except:
            break

    return route_list
'''
Matrix = [['x', 'H.Spiens', 'P.Paniscus', 'R.Rattus', 'G.Gallus', 'Sus.Scrofa'],
          ['H.Spiens', 0, 17, 21, 31, 23],
          ['P.Paniscus', 17, 0, 30, 34, 21],
          ['R.Rattus', 21, 30, 0, 28, 39],
          ['G.Gallus', 31, 34, 28, 0, 43],
          ['Sus.Scrofa', 23, 21, 39, 43, 0]]
result=generate_WPGMA_Tree(Matrix)
'''

def pair_name(late,new,sample):
    #late = ['a', 'b', 'c', 'd']
    #new = ['Hsap', 'HNean', 'PanP', 'Gallus']
    #sample=[('da', 'd', 1.2987012987012987, 'a'), ('bda', 'b', 2.1028390214436725, 'da'), ('cbda', 'c', 16.241975242564, 'bda')]

    f_list=[]
    for i in range(len(late)):
        f_list.append([late[i],new[i]])
    new_sample=[]

    for info in sample:
        node = []
        for name_or_dist in info:
            try:
                name_total =''
                for let in name_or_dist:
                    name_total += exchange_letter_to_name(let,f_list)
            except:
                name_total=name_or_dist

            node.append(name_total)
        noden=(node[0],node[1],node[2],node[3])


        new_sample.append(noden)
    return new_sample

def exchange_letter_to_name(let,lst):
    for i in lst:
        if i[0]==let:
            return i[1]

