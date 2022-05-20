def found_iterator_name(key,fam):
    if key=='gene' or key=='CDS':
        include=fam[key]
        name_list=[]
        for iterator1 in include:
            name_list.append(iterator1[2])
    else:
        include = fam[key]
        name_list = []
        for iterator1 in include:
            name_list.append(iterator1[1])

    return name_list

def categorizer(key,fam):
    if key=='misc_RNA' or key=='precursor_RNA' or key=='mRNA' or key=='regulatory':
        includes = fam[key]
        for iterator1 in includes:
            contemp = [
                {'geneID': iterator1[0], 'name': iterator1[1], 'position': iterator1[2], 'location': iterator1[3],'sequence': iterator1[4]}]
            print('GeneID of Element ||  ' + str(iterator1[0]))
            print("Name of Element's ||  " + str(iterator1[1]))
            print("Presence Position ||  " + str(iterator1[2]))
            print("Located on the DNA ||  " + str(iterator1[3]))
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
            print(' ------------------------- NEXT ELEMENT------------------------- ')


    elif key=='gene':
            includes=fam[key]
            for iterator1 in includes:
                contemp=[{'geneID':iterator1[0], 'synonyms':iterator1[1] ,'name': iterator1[2], 'position': iterator1[3], 'location': iterator1[4], 'sequence': iterator1[5]}]
                print('GeneID of Element ||  ' + str(iterator1[0]))
                print('Synonyms of Gene  ||'  + str(iterator1[1]))
                print("Name of Element's ||  " + str(iterator1[2]))
                print("Presence Position ||  " + str(iterator1[3]))
                print("Located on the DNA ||  " + str(iterator1[4]))
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
                print(' ------------------------- NEXT ELEMENT------------------------- ')

    elif key=='CDS':
        includes = fam[key]
        for iterator1 in includes:
            contemp = [{'AA':iterator1[0],'geneID': iterator1[1], 'name': iterator1[2], 'position': iterator1[3],'location': iterator1[4], 'sequence': iterator1[5]}]
            print('AminoAcid of Protien  ||')
            for iterator3 in range(0,len(iterator1[0]),40):
                print(iterator1[0][iterator3:iterator3+40])

            print('GeneID of Element ||  ' + str(iterator1[1]))
            print("Name of Element's ||  " + str(iterator1[2]))
            print("Presence Position ||  " + str(iterator1[3]))
            print("Located on the DNA ||  " + str(iterator1[4]))
            print("Sequene of Element ::  ")

            cont=input('Show Sequence? (Y/N)')
            scrpirt = iterator1[5][0]
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
            print(' ------------------------- NEXT ELEMENT------------------------- ')


    elif key=='ncRNA':
        includes = fam[key]
        for iterator1 in includes:
            contemp=[{'geneID':iterator1[0], 'synonyms':iterator1[1] ,'name': iterator1[2], 'position': iterator1[3], 'location': iterator1[4], 'sequence': iterator1[5]}]
            print('GeneID of Element ||  ' + str(iterator1[0]))
            print("Name of Element's ||  " + str(iterator1[1]))
            print("Category of Element ||  " + str(iterator1[2]))
            print("Presence Position ||  " + str(iterator1[3]))
            print("Located on the DNA ||  " + str(iterator1[4]))
            print("Sequene of Element ::  ")
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
            print(' ------------------------- NEXT ELEMENT------------------------- ')


