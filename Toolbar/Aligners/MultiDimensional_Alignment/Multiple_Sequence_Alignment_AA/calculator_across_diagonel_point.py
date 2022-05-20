from Toolbar.Aligners.PAM_and_BLOSOM_Matrices.prepare_PAM import *


# This (diagonal) function compare one to one segments of profiles
# row and colon values sorted in terms of PAM Matrix AA range 0 == A, 1 == R through int_to_ID
# diagonal point calculate profile compare output
# find_PAM_Value find proper pair in matrix of AAs

def diagonal_point(row,colon):
    np.array(row); np.array(colon)
    zero_Matrix=np.zeros([len(row),len(colon)])
    PAM_tble=import_PAM_Matrix()
    Gap_inserted_PAM=insert_Gap_score(PAM_tble)
    for i in range(len(row)):
        for j in range(len(colon)):
            if i>=j:
                ID1, ID2=int_to_ID(i,Gap_inserted_PAM),int_to_ID(j,Gap_inserted_PAM)
                PAM_val=int(find_PAM_Value(ID1,ID2,PAM_tble))
                coefficient=(float(row[i])*float(colon[j]))*(PAM_val)
                if coefficient == -0:
                    coefficient=0
                zero_Matrix[i,j]=coefficient
    diagonal_result=sum(zero_Matrix)
    diagonal_result=sum(diagonal_result)
    return diagonal_result
'''
if __name__ == '__main__':
    pM_lst=import_PAM_Matrix()
    rst=insert_Gap_score(pM_lst)
    #print(pM_lst)
    #row=[0,0.25,0.25,0.5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]; colon=[0,0.5,0,0.5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #print(len(row),len(colon))
    #diagonal_result=diagonal_point(row,colon)
    #print(diagonal_result)
'''
