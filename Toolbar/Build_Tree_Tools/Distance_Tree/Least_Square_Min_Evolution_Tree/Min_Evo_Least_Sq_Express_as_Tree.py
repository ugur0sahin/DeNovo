'''
tree=(12.375, [('awyy', 2.6666666666666665), ('Pg', 2.3333333333333335), ('am', 2.875), ('Ek', 0.625), ('nm', 1.875), ('OM', 1.3333333333333333), ('eb', 0.6666666666666666)], [[['Gallus', 'Rattus'], ['awyy', 'Pg']], [['Gallus', 'SusScrofa'], ['awyy', 'am', 'Ek']], [['Gallus', 'PPan'], ['awyy', 'am', 'nm', 'OM']], [['Gallus', 'HSap'], ['awyy', 'am', 'nm', 'eb']], [['Rattus', 'SusScrofa'], ['Pg', 'am', 'Ek']], [['Rattus', 'PPan'], ['Pg', 'am', 'nm', 'OM']], [['Rattus', 'HSap'], ['Pg', 'am', 'nm', 'eb']], [['SusScrofa', 'PPan'], ['Ek', 'nm', 'OM']], [['SusScrofa', 'HSap'], ['Ek', 'nm', 'eb']], [['PPan', 'HSap'], ['OM', 'eb']]])

def find_specific_path(ref_organism, path_IDs_of_organism):
    for i in path_IDs_of_organism:
        if i[0][0]==ref_organism:
            specific_Path_ID=i[1][0]
            break
    return specific_Path_ID
choose_ref_organism='Gallus'


tree_base=''
lengths_of_path_lst=tree[1];path_IDs_of_organism=tree[2]

for i in path_IDs_of_organism:
    print(i)

counter=-1
for binarial_dist in path_IDs_of_organism:
    referred_org_path_ID=find_specific_path(choose_ref_organism, path_IDs_of_organism)
    if (referred_org_path_ID in binarial_dist[1]) and len(binarial_dist[1])==2:
        tree_base += '('                + str(binarial_dist[0][0])+':' +str(binarial_dist[1][0])+',' +  str(binarial_dist[0][1])+':' +str(binarial_dist[1][1])+                             ')'

    counter +=1

    for i in path_IDs_of_organism:
        if (referred_org_path_ID in binarial_dist[1]) and len(binarial_dist[1])==2+counter:
            tree_base='(' + tree_base
            tree_base += ":" + str(binarial_dist[1][-2]) + ", " + str(binarial_dist[0][1]) + ":" + str(binarial_dist[1][-1]) + ")"
    print(tree_base)


'''
'''
tree_smple="((((((X0:zJ, X1:Lw):Cd,X2:Pl): 'KB'), 'X3': 'DS'):'CL','X4': 'JY'): 'GD','X5':'Jr');"
print(tree_smple)
formed_tree=''
for i in tree_scrpt:
    if i== '[':
        tree_scrpt=tree_scrpt.replace("[","(",1)
print(tree_scrpt)
'''
def get_range(el1,el2,scr,ran1,ran2):
    el_ind=[]
    for i in range(ran1,ran2,-1):
        if scr[i]==el1:
            el_ind.append(i)
            break
    for a in range(el_ind[0]-1,ran2,-1):
        if scr[a]==el2:
            el_ind.append(a+1)
    return el_ind


tree_scrpt="(((['X2', 'Kt'], 'iY'), ['X3', 'Mh'], 'nl'), ['X4', 'OB'], 'LR'), "
           #"['X5', 'Mf'])"
tree_smple="((((((X0:zJ, X1:Lw):Cd,X2:Pl): 'KB'), 'X3': 'DS'):'CL','X4': 'JY'): 'GD','X5':'Jr');"


a=tree_scrpt.split(')')
for i in a:
    print(i)