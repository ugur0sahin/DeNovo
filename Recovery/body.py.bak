from Interface_And_File_Manipulating import found_NAME_toshow as name, load_main_dictionary as load_dict, \
    manuel_search as manuel

'''
#Tüm kromozomlar uygun konumlandırılıdgında düzenle

All_or_Choosen = input('All or Choosen:')
if All_or_Choosen==All:
    files = os.listdir('./Modal_Organism_Databases')
    for i in files:
        if i != '.DS_Store':
            print(i)
    chosen_organism=input('Input Organism you Interest: ')
    files = os.listdir('./Modal_Organism_Databases'+'/'+chosen_organism)
    for iterator_chromsome in files:
        ##Sum all dictionaries
else:
    org, chr =choose_show.file_show_and_choose()
    dict3rd=load_dict.read_orginized_data_Advanced(org,chr)
'''

dict3rd=load_dict.read_orginized_data()

initiate_search_type=input('Input Element Search Type: ')

if initiate_search_type=='Index or GeneID':
    Ind_OR_GeneID=input('GeneID or Index what will you search:')
    if Ind_OR_GeneID=='Index': #Index Block
        index_name = input('Input the Index name ')
        for iterator1 in dict3rd.values():
            for iterator2 in iterator1.values():
                #if iterator2[0][1] == index_name or iterator2[0][2] == index_name:
                 if index_name in iterator2[0]:
                        found = 1
                        found_geneFam = iterator1
                        print(found_geneFam)


    elif Ind_OR_GeneID=='Manuel': # Manuel Block
        search_type=input('The type which will you search?')
        if search_type=='location':
            search_object=int(input('Enter the Objection'))
        else:
            search_object=str(input('Enter the Objection'))

        manuel_found_list, found =manuel.manuel_search(search_object,search_type,dict3rd)
        found_geneFam=dict3rd[manuel_found_list[0]]
        '''
        if found_check==1:
            print(str(manuel_found_list) + 'Founded GeneID Famil(ies).')
            found=1
        else:
            print('There is no Gene Family in range you provided')
        '''


    else: #GeneID block
        show_All=input('Show All Gene Family or not? (Y/N)')
        if show_All=='Y':
            for i in dict3rd:
                print(i)

        geneID=input('What is the GeneID of Interest?:')
        try:
            found_geneFam=(dict3rd[int(geneID)])
            found=1
        except:
            print ('There is no key value in this dictionary')
    ##General Continue

    try:
        if found == 1:
            print('The Gene You Interest has chosen !')
            print('Choose the element you interest:')
            for iterator1 in found_geneFam.keys():
                names = name.found_iterator_name(iterator1, found_geneFam)
                print(iterator1+ ' -- ' +str(names))
            chosen_catalog_name = input('Which element will be chosen to put the progress:')
            chosen_element = found_geneFam[chosen_catalog_name]
            #print(chosen_element)
            #print(found_geneFam)
            print('----------------------------------------------------')
            '''
            # print(chosen_element_by_Index[1])
            # Feature show block to show sequence continue ?
            
            checkpoint_to_show_sequence = len(chosen_element)
            counter_to_show_sequence = 0
            for iterator1 in chosen_element:
                counter_to_show_sequence += 1
                print(iterator1)
                #if counter_to_show_sequence < checkpoint_to_show_sequence:
                #    print(iterator1)
                #else:
                #    continue_to_show_sequence = input('Show Sequence? (Y/N)')
                #    if continue_to_show_sequence == 'Y':
                #        print(iterator1)
            '''
            name.categorizer(chosen_catalog_name, found_geneFam)
            '''
            checkpoint_to_show_sequence = len(chosen_element)
            counter_to_show_sequence = 0
            for iterator1 in chosen_element:
                counter_to_show_sequence += 1
                print(iterator1)
            '''
    except:
       print('Gene did not found !')

'''
elif initiate_search_type=='ShowAll':
    for i in dict3rd:
        print (i)
    chosen_numb=input('Enter which geneID of family you will interest')
    chosen_fam_n=dict3rd[int(chosen_numb)]
    for iterator1 in chosen_fam_n.keys():
        print(iterator1)
    chosen_catalog_name=input('Enter which type of element you will interest in family  ' + str(chosen_numb)) #chosen_elemrnt='mRNA'
    chosen_element_n=chosen_fam_n[chosen_catalog_name]
    print('----------------------------------------------------')
    checkpoint_to_show_sequence = len(chosen_element_n)
    counter_to_show_sequence = 0
    for iterator1 in chosen_element_n:
        counter_to_show_sequence += 1
        if counter_to_show_sequence < checkpoint_to_show_sequence:
            print(iterator1)
        else:
            continue_to_show_sequence = input('Show Sequence? (Y/N)')
            if continue_to_show_sequence == 'Y':
                print(iterator1)
'''


