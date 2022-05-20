from Toolbar.Aligners import tracker_global_alignment_Matrix_NA as globALingnment


def manuel_search(objection,type,main_dict):
    found_list=[]
    if type=='AminoAcid':
        for iterator in main_dict.values():
            list_of_All_CDS_of_gene_ID=iterator['CDS']
            for iterator_2 in list_of_All_CDS_of_gene_ID:
                result=globALingnment.globAlignment(iterator_2[0],objection,3,2,1)
                if result > 96:
                    found_list.append(iterator_2[1])

    elif type=='Interval':
        objection=objection.split(', ')
        objection=[int(objection[0]),int(objection[1])]
        for iterator in main_dict.values():
            list_of_gene=iterator['gene']
            location_of_gene=list_of_gene[0][-2][0]
            if location_of_gene[0] >= objection[0] and location_of_gene[1]<=objection[1]:
                found_gene_ID=list_of_gene[0]
                found_list.append(found_gene_ID)
                break

    elif type=='Nucleotide':
        print('It will long time...')
        print('COMING SOON :)')
    found_check=1
    if found_list==[]:
        found_check=0

    return found_list, found_check










