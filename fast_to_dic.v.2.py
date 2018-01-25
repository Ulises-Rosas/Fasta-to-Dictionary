def fas_to_dic(x):
    
    ##fasta file is read
    file = open(x) 
    
    ##all lines are stored in a variable
    file_content = file.readlines()
    
    ##an empty variable is created to store lines without the
    ##newline metacharacter symbol (i.e. "\n")
    seqs_list = []
    
    ##Given this following loop:                    
    for i in file_content:
        ##newline symbol is 
        ##replaced by nothing
        seqs_list.append(i.replace("\n", "")) 
    
    ##here is where keys are going to be stored
    keys = [] 
    
    ##likewise, here is where values are going to be stored
    values = []
    
    i = 0
    ##first value for dictionary's keys
    while(">" in seqs_list[i]):
        ##if lines start with ">" character, store it
        ##on the keys list
        keys.append(seqs_list[i])
        ##add a new i value for continuing
        i += 1 
        ##here is where just a sequence will be stored
        JustOneValue = []
        ##if lines, however, don't start with ">" character,
        ##these should be sequence's lines.
        
        ##second loop for dictionary's value
        while((">" in seqs_list[i]) == False):
            ##So, store them in a list
            JustOneValue.append(seqs_list[i]) 
            ##add a new i value for continuing
            i += 1
            ##if i is equals to the current length of the total
            ##amount of lines, then you will get indexing issues.
            ##So, barely you reach that number, stop or break the 
            ##loop and substract a unit for not getting issues of 
            ##indexing on the first loop
            if(i == len(seqs_list)):
                i -= 1
                break
        ##every time you have all lines of a sequence, collapse them in
        ##a single line
        values.append("".join(JustOneValue))
	
	return dict(zip(keys, values))