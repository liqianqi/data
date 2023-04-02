import os


def loadDatadet(infile,k):
    f=open(infile,'r')
    sourceInLine=f.readlines()
    dataset=[]
    for line in sourceInLine:
        temp1=line.strip('\n')
        temp2=temp1.split( )
        dataset.append(temp2)
    for i in range(0,len(dataset)):
        for j in range(k):
            dataset[i].append(float(dataset[i][j]))
        del(dataset[i][0:k])
    f.close()
    return dataset

origin_dataset_path = '/home/liqianqi/data/test/labels'
output_dir_path = '/home/liqianqi/data/test/labels1'


k=15
if not os.path.exists(output_dir_path):
    os.mkdir(output_dir_path)
dataset = os.listdir(origin_dataset_path)
for file in dataset:

    inputfile = origin_dataset_path + "/" + file
    input = open(inputfile,'r')

    if len(input.read()) == 0:
        outputfile = output_dir_path + "/" + file
        output = open(outputfile, 'w')
        output.close()

    else:
        one_file_data = loadDatadet(inputfile,k)
        outputfile = output_dir_path + "/" + file
        output = open(outputfile, 'w')

        for line in one_file_data:
            names = line[0]

            if names in [9.0,18.0,27.0]:
                names = 0.0
            if names in [10.0,19.0,28.0]:
                names = 1.0
            if names in [11.0,20.0,29.0]:
                names = 2.0
            if names in [12.0,21.0,30.0]:
                names = 3.0
            if names in [13.0,22.0,31.0]:
                names = 4.0
            if names in [14.0,23.0,32.0]:
                names = 5.0
            if names in [15.0,24.0,33.0]:
                names = 6.0
            if names in [16.0,25.0,34.0]:
                names = 7.0
            if names in [17.0,26.0,35.0]:
                names = 7.0

            output.write(str(names) + " " + str(line[1]) + " " + str(line[2]) + " " + str(line[3]) + " " + str(line[4]))
            for i in range(5,15):
                output.write(" " + str(line[i]))
            ## output.write(" " + "-1" + " " + "-1" )

            output.write("\n")
        output.close()