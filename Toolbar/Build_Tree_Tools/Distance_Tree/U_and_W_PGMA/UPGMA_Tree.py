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

def dist(A,B,Matrix):
    sum =0
    counter=0
    for i in A:
        for j in B:
            counter +=1
            element = find_location(i,j,Matrix)
            sum += element[0]
    return sum/counter


def calculate_distances(Matrix, first_Matrix):
    Matrix_rec=transfer_Matrix(first_Matrix)
    #Generate New Node
    min_of_matrix, min_i, min_j = find_min(Matrix)
    nod=(Matrix[min_i][0], min_of_matrix/2, Matrix[0][min_j])
    will_express=(Matrix[min_i][0]+ Matrix[0][min_j],Matrix[min_i][0], min_of_matrix/2, Matrix[0][min_j])

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
                    zero_Matrix[i][j]=dist(zero_Matrix[i][0], zero_Matrix[0][j],Matrix_rec) #### ERROR
    #for i in zero_Matrix: print(i)
    return zero_Matrix, will_express
def Matrix_Copy(Matrix):
    NMat=[]
    for i in Matrix:
        row_lst=[]
        for j in i:
            row_lst.append(j)
        NMat.append(row_lst)
    return NMat

def UPGMA_Tree(Matrix):
    counter=0
    route_list = []
    for i in range(len(Matrix)):
        for j in range(len(Matrix[0])):
            if i == j and i != 0 and j !=0:
                Matrix[i][j]=0
    Matrix_Rec = Matrix_Copy(Matrix)

    while True:
        try:
            if counter==0:
                counter +=1

                a,b=calculate_distances(Matrix, Matrix)
                route_list.append(b)
            else:
                Matrix = Matrix_Rec
                a, b=calculate_distances(a, Matrix)
                route_list.append(b)
        except:
            break

    return route_list

'''
Matrix = [[0, 'a', 'b', 'c', 'd', 'e', 'f'],
                          ['a', 0, 19, 27, 8, 33, 18],
                          ['b', 19, 0, 31, 18, 36, 1],
                          ['c', 27, 31, 0, 26, 41, 32],
                          ['d', 8, 18, 26, 0, 31, 17],
                          ['e', 33, 36, 41, 31, 0, 35],
                          ['f', 18, 1, 32, 17, 35, 0]]


Matrix = [[0, 'a', 'b', 'c', 'd'],
          ['a', 0, 2.5974025974025976, 3.0303030303030304, 3.463203463203463],
          ['b', 2.5974025974025976, 0, 88.60759493670886, 5.813953488372093],
          ['c', 3.463203463203463, 88.60759493670886, 0, 5.813953488372093],
          ['d', 2.5974025974025976, 5.813953488372093, 5.813953488372093, 0]]

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
'''
result=UPGMA_Tree(Matrix)
print(pair_name(['a','b','c','d'],['A||C','A||C','A||C','A||C'],result))
'''
'''
result=UPGMA_Tree(Matrix)

print(result)
'''