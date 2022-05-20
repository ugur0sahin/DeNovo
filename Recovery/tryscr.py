from Toolbar.Aligners.MultiDimensional_Alignment.Multiple_Sequence_Alignment_AA.calculator_across_diagonel_point import *
'''
lst = []
for j in range(4):
    row = []
    for i in range(10):
        row.append('-')
    lst.append(row)

profile_Mat = np.matrix(lst)
profile_Mat = np.insert(profile_Mat, 1, ['a', 'a', 'a', 'a'], axis=1)
print(profile_Mat)

Mt=[['G','A','P'],['T','A','G'],['P','A','T']]
print(np.matrix(Mt))
'''

gap_clmn=np.zeros([21,1])
gap_clmn[20,0]=1
print(gap_clmn)