class Node():
    def __init__(self,name,info):
        self.name=name
        self.info=info
    def __str__(self):
        return str(self.name)

def converter_info_structure(replace_lst,lst_obj):
    return_lst=[]
    for rp_el in replace_lst:
        case=rp_el
        for item in lst_obj:
            if item.name==rp_el:
                item_to_lst=item.info
                case='('+str(item_to_lst[0][1]) + ':'+str(item_to_lst[0][0]) + ',' + str(item_to_lst[1][1])+':'+str(item_to_lst[1][0])+ ')'
                return_lst.append(case)
        if rp_el == case:
            return_lst.append(case)
    return return_lst


def converter_NJ_tree_to_plot(NJ_output):
    item_objected_lst=[]
    for item in NJ_output:
        elements_of_item=item
        info_elements_of_item=item[2::]
        if len(elements_of_item)==4:
            A=Node(elements_of_item[0],info_elements_of_item)
            item_objected_lst.append(A)

        elif len(elements_of_item)==3:
            A=Node('ROOT',elements_of_item)
            item_objected_lst.append(A)

    last_case_item=item_objected_lst[-1].info
    last_case_item_dist=float(last_case_item[1])/2
    last_case='(' + last_case_item[0] + ':' + str(last_case_item_dist) + ',' + last_case_item[2]+':'+str(last_case_item_dist)+ '):' +'1'
    case,replace_lst=last_case,[]
    bcase=case
    while not bcase.islower():
        #bcase=case
        case=bcase.split(':')
        for i in case:
            if not ( i[-1] == ')' or i[-1] == '1'):
                replace_lst.append(i[-1])
        replace_result=converter_info_structure(replace_lst,item_objected_lst)
        for i in range(len(replace_result)):
            bcase=bcase.replace(str(replace_lst[i]),str(replace_result[i]))
    return bcase

def exchange_w_names(path_late,names):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    for i in range(len(names)):
        path_late=path_late.replace(str(letters[i])+":",names[i]+':')
    return path_late

###

def pair_letter_w_names(direction_lst,names):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    direction_lst_w_names=[]
    for info in direction_lst:
        info_N=[]
        for element in info:
            if element in letters:
                indx=letters.index(element)
                name_of_element=names[indx]
                info_N.append(name_of_element)
            else:
                info_N.append(element)
        direction_lst_w_names.append(info_N)

    return direction_lst_w_names

def direction_NJ(Pathways_naked,names):
    direction_lst=[]
    for item in Pathways_naked:
        try:
            name_of_itm,name_comp_of_itmA,name_comp_of_itmB=item[0],item[2][1],item[3][1]
            direction_component=(name_comp_of_itmA,name_comp_of_itmB, name_of_itm)
            direction_lst.append(direction_component)
        except:
            name_itmA, name_itmB , root = item[0], item[2], 'ROOT'
            direction_component=(name_itmA, name_itmB , root)
            direction_lst.append(direction_component)
    direction_lst_w_names=pair_letter_w_names(direction_lst,names)
    return direction_lst_w_names


'''
pathyways=(('H', 17.0, (9.9, 'a'), (7.1, 'b')),
('M', 14.0, (5.0625, 'c'), (8.9375, 'd')),
('U', 5.75, (2.041666666666667, 'M'), (3.708333333333333, 'H')),
('O', 11.125, (2.0, 'U'), (9.125, 'f')),
('R', 11.0, (1.375, 'O'), (9.625, 'e')),
('R', '6.375', 'g'))
names=['HSap','Neanderttal','c','d','e','f','g']
print(direction_NJ(pathyways,names))
'''
'''
if __name__=="__main__":
    NJ_output = [('H', 17.0, (9.9, 'a'), (7.1, 'b')), ('P', 14.0, (5.0625, 'c'), (8.9375, 'd')), ('C', 5.75, (2.041666666666667, 'P'), (3.708333333333333, 'H')), ('O', 11.125, (2.0, 'C'), (9.125, 'f')), ('X', 11.0, (1.375, 'O'), (9.625, 'e')), ('X', '6.375', 'g')]
    bcase=converter_NJ_tree_to_plot(NJ_output)
    print(exchange_w_names(bcase,['12432','13452','2344','2211','4674','235534','42322']))
'''

