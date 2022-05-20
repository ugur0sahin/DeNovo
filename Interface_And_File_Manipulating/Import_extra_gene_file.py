def Import_file(filename, extension):
    f=open(filename,'r')
    file_content=f.readlines()

    if extension=='fasta':
        objection=[]
        for i in file_content:
            if '>' in i:
                i=i.rstrip('\n')
                info=i
            else:
                i=i.rstrip('\n')
                objection+=i
        objection = ''.join(objection)

    return [info,objection]

'''
def Import_Multiple_Content(filename, extension):
    with open(filename,'r') as f:
        line=f.readlines()
    main_list=[]
    if '>' in line:
        counter = 0
        info=line[counter]
        while '>' not in line:
            counter +=1
            subject=line[counter]
        main_list
        
        return 
'''