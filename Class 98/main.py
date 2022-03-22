def readmyfile():
    filename=input("Enter file name..")
    file=open(filename,'r')
    numberofwords=0

    for i in file:
        words=i.split()
        numberofwords=numberofwords + len(words)

    print("Number of words= ", numberofwords)

readmyfile()