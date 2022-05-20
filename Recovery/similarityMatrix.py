from Toolbar.Aligners.generator_matrix_global_alignment_NA import *

def score(res):
    res = res.split("\n")
    del res[1]
    match = 0
    for i in range(len(res[1])):
        if res[0][i] == res[1][i]:
            match += 1
    return (match/len(res[0]))

def where_is_maximum(matrix):
    max_of_matrix=np.max(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if max_of_matrix==matrix[i][j]:
                loc=[i,j]

    return loc

def start_point_Glob(matrix):
    return [len(matrix)-1, len(matrix[0])-1]

def matrix_path(seqx, seqy, matrix, y, x):
    way = [[matrix[y][x], "start"]]
    seq1 = ''
    seq2 = ''
    while matrix[y][x] != 0:
        up = matrix[y-1][x]
        left = matrix[y][x-1]
        cross = matrix[y-1][x-1]
        if cross == 0:
            way.insert(0, [cross, "cross"])
            x = x - 1
            y = y - 1
            seq1 = seqx[x] + seq1
            seq2 = seqy[y] + seq2


        elif max(up, left, cross) == cross:
            way.insert(0, [cross, "cross"])
            x = x - 1
            y = y - 1
            seq1 = seqx[x] + seq1
            seq2 = seqy[y] + seq2

        elif max(up, left, cross) == left:
            way.insert(0, [left, "left"])
            x = x - 1
            seq1 = seqx[x] + seq1
            seq2 = '-' + seq2

        elif max(up, left, cross) == up:
            way.insert(0, [up, "up"])
            y = y - 1
            seq1 = '-' + seq1
            seq2 = seqy[y] + seq2
    compare = ''
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            compare += '|'
        else:
            compare += ' '
    res = seq1 + '\n' + compare + '\n' + seq2


    return res

def matrix_path_global(seqx, seqy, matrix, y, x):
    way = [[matrix[y][x], "start"]]
    seq1 = ''
    seq2 = ''
    while x != 0 and y != 0:
        up = matrix[y-1][x]
        left = matrix[y][x-1]
        cross = matrix[y-1][x-1]


        if max(up, left, cross) == cross:
            way.insert(0, [cross, "cross"])
            x = x - 1
            y = y - 1
            seq1 = seqx[x] + seq1
            seq2 = seqy[y] + seq2

        elif max(up, left, cross) == left:
            way.insert(0, [left, "left"])
            x = x - 1
            seq1 = seqx[x] + seq1
            seq2 = '-' + seq2

        elif max(up, left, cross) == up:
            way.insert(0, [up, "up"])
            y = y - 1
            seq1 = '-' + seq1
            seq2 = seqy[y] + seq2
    compare = ''
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            compare += '|'
        else:
            compare += ' '
    res = seq1 + '\n' + compare + '\n' + seq2


    return res


seqx1 = 'ATAGGC'
seqy1 = 'ATGTGC'

matrix = globAlignment(seqy1, seqx1,1,1,1)
matrix=globAlignment(seqy1,seqx1,4,4,4)
#print(where_is_maximum(matrix))
start = start_point_Glob(matrix)
#print(matrix_path(seqx1, seqy1, matrix, where_is_maximum(matrix)[0], where_is_maximum(matrix)[1]))
a = matrix_path_global(seqy1,seqx1,matrix, start[0], start[1])
print(a)
