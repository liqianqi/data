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

origin_dataset_path = '/home/liqianqi/AI/yolov7-face/datasets/train/labels' # 改成自己的label文件夹子
output_dir_path = '/home/liqianqi/AI/yolov7-face/datasets/train/labels'     # 改成自己的label文件夹子


k=20
if not os.path.exists(output_dir_path):
    os.mkdir(output_dir_path)
dataset = os.listdir(origin_dataset_path)
for file in dataset:

    inputfile = origin_dataset_path + "/" +file
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
            
            kp1 = 2.0000
            kp2 = 2.0000
            kp3 = 2.0000
            kp4 = 2.0000
            kp5 = 2.0000

            #output.write(str(line[0]))
            """_summary_
            output.write(str(line[0]) + " " + str(line[1]) + " " + str(line[2]) + " " + str(line[3]) + " " + str(line[4]))

            output.write(" " + str(line[5]))   
            output.write(" " + str(line[6]))
            output.write(" " + str(round(kp1,6))) 
            
            output.write(" " + str(line[7])) 
            output.write(" " + str(line[8])) 
            output.write(" " + str(round(kp2,6))) 
            
            output.write(" " + str(line[9]))  
            output.write(" " + str(line[10])) 
            output.write(" " + str(round(kp3,6))) 
            
            output.write(" " + str(line[11]))   
            output.write(" " + str(line[12])) 
            output.write(" " + str(round(kp4,6))) 
        
            output.write(" " + str(line[13]))
            output.write(" " + str(line[14]))
            output.write(" " + str(round(kp5,6))) 
            
            """			
            output.write(str(line[0]) + " " + str(line[1]) + " " + str(line[2]) + " " + str(line[3]) + " " + str(line[4]))
            output.write(" " + str(line[5]))   
            output.write(" " + str(line[6]))
            output.write(" " + "2.0000") 

            output.write(" " + str(line[8])) 
            output.write(" " + str(line[9])) 
            output.write(" " + "2.0000")

            output.write(" " + str(line[11])) 
            output.write(" " + str(line[12])) 
            output.write(" " + "2.0000")  

            output.write(" " + str(line[14])) 
            output.write(" " + str(line[15])) 
            output.write(" " + "2.0000") 

            output.write(" " + "0.550000") 
            output.write(" " + "0.550000") 
            output.write(" " + "2.0000") 

            output.write("\n")
        output.close()
