from Toolbar.Aligners.Two_Dim_Alignment.Protein_Alignment.generate_aligned_bisequence_wscore import *
import numpy as np
import random
import string
import Toolbar.Aligners.PAM_and_BLOSOM_Matrices.prepare_PAM as PAM
from Toolbar.Build_Tree_Tools.Distance_Matrix.generator_distance_matrix import *
#warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)

PAMMatrix=PAM.import_PAM_Matrix()

def zeros(A):
    zero_Matrix=[]
    for i in range(A[0]):
        rows=[]
        for j in range(A[1]):
            rows.append(0)
        zero_Matrix.append(rows)
    return zero_Matrix

def add_row(add_element_list, Matrix):
    Matrix.insert(0,add_element_list)
    return Matrix

def add_column(add_element_list, Matrix):
    for i in range(len(Matrix)):
        Matrix[i].insert(0,add_element_list[i])
    return Matrix

def Substract_Names(Distance_Matrix):
    Distance_Matrix_without_names = []
    for i in range(len(Distance_Matrix)):
        if not i == 0:
            Distance_Matrix_without_names.append(Distance_Matrix[i][1:])
    return Distance_Matrix_without_names


def Joining(Distance_Matrix):
    names=Distance_Matrix[0]
    Distance_Matrix_without_names = Substract_Names(Distance_Matrix)
    zero_Matrix=zeros([len(Distance_Matrix_without_names),len(Distance_Matrix_without_names[0])])

    for i in range(len(Distance_Matrix_without_names)):
        for j in range(len(Distance_Matrix_without_names[i])):
            #if not i==j:
            if i<j:
                #The step Q(a,b)=(n-2)d - sum(d(a,k) - sum(d(b,k))
                sum_for_j=0 ; sum_for_i=0
                for iterator_for_j in range(len(Distance_Matrix_without_names)): sum_for_j += float(Distance_Matrix_without_names[j][iterator_for_j])
                for iterator_for_i in range(len(Distance_Matrix_without_names)): sum_for_i += float(Distance_Matrix_without_names[iterator_for_i][i])

                changed_element=((len(Distance_Matrix_without_names)-2)* float(Distance_Matrix_without_names[i][j])) - sum_for_j -sum_for_i
                zero_Matrix[i][j] = changed_element
                zero_Matrix[j][i] = changed_element
    zero_Matrix_wo_name=np.matrix(zero_Matrix)
    add_row(names[1:],zero_Matrix)
    add_column(names,zero_Matrix)
    zero_Matrix_Q=np.matrix(zero_Matrix)

    return zero_Matrix_Q, zero_Matrix_wo_name


def Find_Min_in_Matrix(Q_Matrix):
    min=np.min(Q_Matrix)
    x=[]
    for i in range(len(Q_Matrix)):
        for j in range(len(Q_Matrix)):
            if Q_Matrix[i,j]==min:
                x=[i,j]
                break
        if x !=[]:
            break
    return x[0],x[1]

#ind_i,ind_j=Find_Min_in_Matrix(result1)


def Generate_Node(Distance_Matrix, Q_WOname):
    recovery_Distance_Matrix=Distance_Matrix

    ind_i, ind_j = Find_Min_in_Matrix(Q_WOname)
    #print(Distance_Matrix_WOname)

    ind_i = ind_i + 1
    ind_j = ind_j + 1

    names_will_create_nodes=(Distance_Matrix[ind_i][0], Distance_Matrix[0][ind_j])
    #print(names_will_create_nodes)

    ###Node and distance from their components generated and saved to node_info

    element1_from_all_dist_sum = 0
    element2_from_all_dist_sum = 0

    for i in range(len(Distance_Matrix)):
        for j in range(len(Distance_Matrix[i])):
            if Distance_Matrix[0][j]==names_will_create_nodes[0] and Distance_Matrix[i][0]==names_will_create_nodes[1]:
                nodes_element_distances=float(Distance_Matrix[i][j])
            if Distance_Matrix[0][j]==names_will_create_nodes[0] and i!=0:
                element1_from_all_dist_sum += float(Distance_Matrix[i][j])
            if Distance_Matrix[0][j]==names_will_create_nodes[1]and i!=0:
                element2_from_all_dist_sum += float(Distance_Matrix[i][j])

    p1_i = ((1 / 2) * nodes_element_distances)
    p2_i = (1 / (2 * ((len(Distance_Matrix)-1) - 2)) * (element1_from_all_dist_sum - element2_from_all_dist_sum))

    distance_from_generated_node_el1 = p1_i + p2_i
    distance_from_generated_node_el2 = nodes_element_distances-distance_from_generated_node_el1
    #print(distance_from_generated_node_el1,distance_from_generated_node_el2)
    a = random.choice(string.ascii_letters)
    a = a.upper()
    node_info=(a,abs(nodes_element_distances),(abs(distance_from_generated_node_el1),names_will_create_nodes[0]),(abs(distance_from_generated_node_el2),names_will_create_nodes[1]))
    #print(node_info)

    Distance_Matrix = np.matrix(Distance_Matrix)
    #print(np.where(Distance_Matrix == 'a'))


    ###Calculate of other distances add previous distances before

    zero_Matrix=zeros([len(Q_WOname)-1, len(Q_WOname)-1])
    names_colon=(recovery_Distance_Matrix[0])
    names_row=names_colon[1:]
    names_colon.remove(names_will_create_nodes[0])
    names_colon.remove(names_will_create_nodes[1])
    names_row.remove(names_will_create_nodes[0])
    names_row.remove(names_will_create_nodes[1])
    names_row.insert(0,a.upper())
    names_colon.insert(1,a.upper())
    #print(names_colon, names_row)

    add_row(names_row,zero_Matrix)
    add_column(names_colon,zero_Matrix)

    zero_Matrix=np.matrix(zero_Matrix)

    for i2 in range(len(zero_Matrix)):
        for j2 in range(len(zero_Matrix)):
            if i2 != 0 and j2 != 0:  # Except Letters
                if zero_Matrix[0,j2] == zero_Matrix[i2,0]:
                    zero_Matrix[i2,j2] = float(0)  # Diagonal zeros
                else:
                    if zero_Matrix[0,j2] == a:
                        sr1=zero_Matrix[i2,0]
                        for i in range(len(Distance_Matrix)):
                            for j in range(len(Distance_Matrix)):
                                if Distance_Matrix[i,0]==sr1 and Distance_Matrix[0,j]==names_will_create_nodes[0]:
                                    p1=Distance_Matrix[i,j]
                                if Distance_Matrix[i,0]==sr1 and Distance_Matrix[0,j]==names_will_create_nodes[1]:
                                    p2 = Distance_Matrix[i,j]
                        zero_Matrix[i2, j2] = 1 / 2 *( float(p2) + float(p1) - float(nodes_element_distances))

                    elif zero_Matrix[i2,0] == a:
                        sr1 = zero_Matrix[0, j2]
                        for i in range(len(Distance_Matrix)):
                            for j in range(len(Distance_Matrix)):
                                if Distance_Matrix[i,0] == sr1 and Distance_Matrix[0,j] == names_will_create_nodes[0]:
                                    p1 = Distance_Matrix[i,j]
                                if Distance_Matrix[i,0] == sr1 and Distance_Matrix[0,j] == names_will_create_nodes[1]:
                                    p2 = Distance_Matrix[i,j]
                        zero_Matrix[i2, j2] = 1 / 2 * (float(p2) + float(p1) - float(nodes_element_distances))
                    else:
                        get_elements_will_search = [zero_Matrix[i2,0], zero_Matrix[0,j2]]
                        A = np.where(Distance_Matrix == get_elements_will_search[0])
                        b = np.where(Distance_Matrix == get_elements_will_search[1])
                        zero_Matrix[i2,j2] = float(Distance_Matrix[A[0][1], b[1][0]])

    zero_Matrix=zero_Matrix.tolist()
    return zero_Matrix, node_info

####

def check_characters(lst):
    cp=True
    for i in lst:
        if  len(i)!=1:
            cp =False
    return cp

def change_characters(Matrix):
    letters = ['x','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    for i in range(len(Matrix)):
        for j in range(len(Matrix)):
            if not (i==0 and j==0):
                if j==0:
                    Matrix[i][0]=letters[i]
                elif i==0:
                    Matrix[0][j]=letters[j]
            else:
                Matrix[i][j]='x'
    return Matrix

def Neighboor_Joining(Matrix):
    Bool=check_characters(Matrix[0])
    if not Bool:
        Matrix=change_characters(Matrix)
    all_nodes=[]
    counter=0
    while True:
        try:
            counter+=1
            if counter==1:
                result, result1 = Joining(Matrix)
                a, node_inf=Generate_Node(Matrix, result1)
                #print(node_inf)
                all_nodes.append(node_inf)

            else:
                result, result1 = Joining(a)
                a, node_inf = Generate_Node(a, result1)
                #print(node_inf)
                all_nodes.append(node_inf)
        except:
            ty=float(a[1][2])
            if ty < 0:
                ty= -ty
            last_nodes_dist=(a[0][1],str(ty),a[0][2])
            #print(last_nodes_dist)
            all_nodes.append(last_nodes_dist)
            break
    for j in all_nodes:
        print(j)
    return all_nodes
'''
Matrix = [['x', 'hSap', 'gallus', 'rattus', 'neandartel','e','f','g'],
                          ['hSap',0, 17, 21, 27,23,21,28],
                          ['gallus',17, 0, 16, 21,28,24,17],
                          ['rattus',21, 16, 0, 14,21,18,17],
                          ['neandartel',27, 21, 14, 0,19,24,23],
                          ['e',23, 28, 21, 19,0,21,16],
                          ['f',21, 24, 18, 24,21,0,16],
                          ['g',28, 17, 17,23,16,16,0]]

naked_pathways =Neighboor_Joining(Matrix)
print(naked_pathways)
'''