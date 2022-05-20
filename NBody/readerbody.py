import generate_Class_for_elements as Objection

def find_gene_element(lines_of_element):
    gene, geneID, gene_synonyms, location = None, None, None, None

    location=get_location_and_type(lines_of_element)
    ct=-1
    for line in lines_of_element:
        ct+=1
        if '/db_xref="GeneID:' in line:
            line_of_interest=line.rstrip('\n')
            geneID=line_of_interest[38:-1]
        if '/gene=' in line:
            gene = get_interval_in_segment(lines_of_element[ct:-1])

        if '/gene_synonym=' in line:
            gene_synonyms = get_interval_in_segment(lines_of_element[ct:-1])
    return gene, int(geneID), gene_synonyms, location

def find_CDS_element(lines_of_element):
    product, geneID, AA_seq ,location = None, None, None, None

    location=get_location_and_type(lines_of_element)
    ct=-1

    for line in lines_of_element:
        ct+=1
        if '/db_xref="GeneID:' in line:
            line_of_interest=line.rstrip('\n')
            geneID=line_of_interest[38:-1]
        if '/product=' in line:
            product = get_interval_in_segment(lines_of_element[ct:-1])

        if '/translation=' in line:
            AA_seq = get_interval_in_segment(lines_of_element[ct:],exps1='                     /translation="',exps2='"')
            AA_seq = AA_seq.replace('\n','')
            AA_seq = AA_seq.replace(' ','')
    return product, geneID, AA_seq, location

### ABOVE THIS ROW ELEMENT NAMES WILL BE PREPARED TO SPECIFY

def get_interval_in_segment(list,exps1='"', exps2='"'):
    string_return,ct='',0
    indx=list[0].index(exps1)
    string_return += list[0][indx+len(exps1):-1]

    if exps2 in list[0][indx+len(exps1):-1]:
        ps2=list[0][indx+len(exps1):-1].index(exps2)
    else:
        while True:
            ct +=1
            try:
                A=list[ct].index(exps2)
                line=list[ct][:A]
                string_return += line
                break
            except:
                line=list[ct]
                string_return += line
    string_return=string_return.replace(exps1,'')
    string_return=string_return.replace(exps2,'')
    string_return=string_return.replace('  ','')
    return string_return


def get_location_and_type(lines_of_element_lst):

    interval = None

    for i in range(len(lines_of_element_lst)):
        if 'complement(join(' in lines_of_element_lst[i]:
            interval = get_interval_in_segment(lines_of_element_lst,exps1="complement(join(", exps2="))")
            interval = interval.replace(' ', '')
            interval = interval.replace('\n', '')
            interval = interval,"C/J"
        elif 'complement(' in lines_of_element_lst[i]:
            interval = get_interval_in_segment(lines_of_element_lst, exps1="complement(", exps2=")")
            interval = interval.replace(' ', '')
            interval = interval.replace('\n', '')
            interval = interval,"C/Only"
        elif 'join(' in lines_of_element_lst[i]:
            interval = get_interval_in_segment(lines_of_element_lst, exps1="join(", exps2=")")
            interval = interval.replace(' ', '')
            interval = interval.replace('\n', '')
            interval = interval, "J/Only"
        elif 'join(complement(' in lines_of_element_lst[i]:
            interval = get_interval_in_segment(lines_of_element_lst, exps1="join(complement(", exps2="))")
            interval = interval.replace(' ','')
            interval = interval.replace('\n','')
            interval = interval, 'J/C'
        else:
            interval = lines_of_element_lst[0][16:-1]
            interval = interval.rstrip('\n')
            interval = interval, "N"
        break

    return interval

def generate_all_element_list(text_path):

    All_element_lst=[]

    with open(text_path, 'r') as file1:
        converted_txt = file1.readlines()
    ctr=0
    found_start, found_end=False,False
    start,end="didn't found start", "didn't found end"
    for line in converted_txt:
        ctr +=1
        if '    gene     ' in line and found_start==False:
            start = ctr
            found_start=True
        elif 'ORIGIN' in line and found_end==False:
            found_end=True
            end=ctr
            break

    for i in range(start, end):
        line= converted_txt[i].rstrip('\n')
        if '    gene    ' in line: #In order to get gene
            lines_of_element=[]
            ct=1                                                    # PROBLEM!!
            lines_of_element.append(converted_txt[i])
            while converted_txt[i+ct][2:10] == '        ':     #
                lines_of_element.append(converted_txt[i+ct])
                ct += 1

            # find elements for gene by get_gene_elements_function

            gene, geneID, gene_synonyms, location=find_gene_element(lines_of_element)
            a_gene = Objection.gene(gene, geneID, gene_synonyms, location)
            All_element_lst.append(a_gene)

        if '    CDS    ' in line:
            lines_of_element=[]
            ct=1
            lines_of_element.append(converted_txt[i])
            while converted_txt[i+ct][2:10] == '        ':
                lines_of_element.append(converted_txt[i+ct])
                ct +=1

            product, geneID, AA_seq, location = find_CDS_element(lines_of_element)
            a_CDS = Objection.CDS(product, geneID, AA_seq, location)
            All_element_lst.append(a_CDS)

        '''
        if 'mRNA'
        if 'ncRNA'
        if 'exon'
        '''


    return All_element_lst


