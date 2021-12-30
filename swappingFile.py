def swapFileData():
    fileName=input("Enter The File Name:-")

    with open(sample1,'r') as a:
        data_a = a.read()

    with open(sample2,'r') as a:
        data_b = a.read()   

    with open(sample1,'w') as a:
        a.write(data_b)

    with open(sample2,'w') as a:
        a.write(data_a)

swapFileData();        
    