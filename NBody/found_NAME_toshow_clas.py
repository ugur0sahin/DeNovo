def categorizer(aClass,searched_type):
    while True:
        nfound=True
        all_elemnts = aClass.return_all_elements()
        for i in range(len(aClass.return_all_elements())):
            if searched_type=='CDS':
                if all_elemnts[i].type == searched_type:
                    print('[' + str(i) + ']' + ' ' + str(all_elemnts[i]) + '|| ' + str(all_elemnts[i].type))
                    nfound=False
            else:
                if all_elemnts[i].type != searched_type:
                    print('[' + str(i) + ']' + ' ' + str(all_elemnts[i]) + '|| ' + str(all_elemnts[i].type))
                    nfound = False

        if nfound:
            print('There is no CDS element in this family!')
            break
        print("User can examine choosen element's family which saved to database")
        exam_element=int(input('Choose will be examined element:'))
        if exam_element==-1:
            break
        key=all_elemnts[exam_element].type
        if key=='misc_RNA' or key=='precursor_RNA' or key=='mRNA' or key=='regulatory' or key=='ncRNA':
            includes = aClass.RNA()
            for iterator1 in includes:
                print('GeneID of Element ||  ' + str(iterator1.geneID))
                print("Name of Element's ||  " + str(iterator1.name))
                print("Presence Position ||  " + str(iterator1.location_pos))
                print("Located on the DNA ||  " + str(iterator1.sequence))
                print("Sequene of Element ::  ")
                cont = input('Show Sequence? (Y/N)')
                scrpirt = iterator1[4][0]
                if cont == 'Y':
                    counter = -1
                    if len(iterator1[4]) != 1:
                        for iterator2 in iterator1[3]:
                            counter += 1
                            print(str(iterator2) + ' || ' + str(iterator1[4][counter]))
                    else:
                        scrpirt = iterator1[4][0]
                        length_of_sequence = len(scrpirt)
                        for iterator3 in range(0, length_of_sequence, 250):
                            print(scrpirt[iterator3:iterator3 + 250])



        elif key=='gene':
                includes=aClass.gene
                for iterator1 in includes:
                    contemp=[{'geneID':iterator1.geneID, 'synonyms':iterator1.synonyms ,'name': iterator1.name, 'position': iterator1.position, 'location': iterator1.location, 'sequence': iterator1.sequence}]
                    print('GeneID of Element ||  ' + str(iterator1.geneID))
                    print('Synonyms of Gene  ||'  + str(iterator1.synonyms))
                    print("Name of Element's ||  " + str(iterator1.name))
                    print("Presence Position ||  " + str(iterator1.location_pos))
                    print("Located on the DNA ||  " + str(iterator1.location))
                    print("Sequene of Element ::  " )
                    cont = input('Show Sequence? (Y/N)')
                    scrpirt = iterator1[5][0]
                    if cont == 'Y':
                        counter = -1
                        if len(iterator1[5]) != 1:
                            for iterator2 in iterator1[4]:
                                counter += 1
                                print(str(iterator2) + ' || ' + str(iterator1[5][counter]))
                        else:
                            scrpirt = iterator1[5][0]
                            length_of_sequence = len(scrpirt)
                            for iterator3 in range(0, length_of_sequence, 250):
                                print(scrpirt[iterator3:iterator3 + 250])

        elif key=='CDS':
                include = all_elemnts[exam_element]
                print('AminoAcid of Protien  ||')
                for iterator3 in range(0,len(include.AAseq),40):
                    print(include.AAseq[iterator3:iterator3+40])

                print('GeneID of Element ||  ' + str(include.geneID))
                print("Name of Element's ||  " + str(include.product))
                print("Presence Position ||  " + str(include.location_pose))
                print("Located on the DNA ||  " + str(include.location))
                print("Sequene of Element ::  ")

                cont=input('Show Sequence? (Y/N)')
                #scrpirt = iterator1[5][0]
                if cont=='Y':
                    counter=-1
                    if len(iterator1[5]) != 1:
                        for iterator2 in iterator1[4]:
                            counter += 1
                            print(str(iterator2) +' || ' + str(iterator1[5][counter]))
                    else:
                        scrpirt = iterator1[5][0]
                        length_of_sequence = len(scrpirt)
                        for iterator3 in range(0, length_of_sequence, 250):
                            print(scrpirt[iterator3:iterator3 + 250])
        cont_examine=input('Will it continue to be investigated?')
        if cont_examine=='Y':
            print(' ------------------------- NEXT ELEMENT------------------------- ')
        else:
            break


