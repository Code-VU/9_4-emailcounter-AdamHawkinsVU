def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)

    lst = list()

    for line in handle:
        if not line.startswith("From:"): continue
        line = line.split()
        lst.append(line[1])

    counts = dict()
    for word in lst:
        counts[word] = counts.get(word,0) +1

    bigcount = None
    bigword = None
    
    for word,count in counts.items():
        if bigcount is None or count > bigcount:
            bigcount=count
            bigword = word 
    
    print (bigword,bigcount)
        
## if you want to test locally before you try to sync
## uncomment countEmail() and run > python counter.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#countEmail()
