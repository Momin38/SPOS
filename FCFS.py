def sortedArray(pro, arrTime, burTime):
    ziped_list = zip(pro, arrTime, burTime)
    sorted_ziped_list = sorted(ziped_list, key=lambda x: x[1])
    sorted_Pro, sorted_arrTime, sorted_burTime = zip(*sorted_ziped_list)
    return list(sorted_Pro), list(sorted_arrTime), list(sorted_burTime)

    

def FCFS(processes,arrivalTime,burstTime):
    complitionTime = []
    counter = 0
    for i in range(len(processes)):
        arT = arrivalTime[i]
        buT = burstTime[i]
        
        if arT<= counter:
            counter = counter +buT
            complitionTime.append(counter)
        if arT>= counter:
            while (counter<arT):
                counter = counter+1
            counter = counter + buT
            complitionTime.append(counter)
    return complitionTime
    

def turnArround_Time(complition,arrTime): #how much time will process stay in the CPU
    trun_arround_time = []
    for i in range(len(Compile_time)):
        tem = complition[i]-arrTime[i]
        trun_arround_time.append(tem)
    return trun_arround_time
    
def waitimg_time(burstTime,TAT): #how many time process was waited for processing
    waitimg_time = []
    for i in range(len(burstTime)):
        tem = TAT[i]-burstTime[i]
        waitimg_time.append(tem)
    return waitimg_time


#driver code    
pro = ['p1','p2','p3','p4']
arrivalTime = [0,1,5,6,]
burstTime = [2,2,3,4]

#complie time
sorted_pro,sorted_arrTime,sorted_burstTime = sortedArray(pro,arrivalTime,burstTime)
Compile_time = FCFS(sorted_pro,sorted_arrTime,sorted_burstTime)

#turn Aroumd time
TAT = turnArround_Time(Compile_time,sorted_arrTime)


#waiting Time 
Wt = waitimg_time(burstTime,TAT)




print('Process','           ','Arival Time ','          ','Burst Time0','           ','complition Time ','          ','Turn Aound Time','           ','Waiting Time')
for i in range(len(pro)):
    print(sorted_pro[i],'                     ',sorted_arrTime[i],'                  ',sorted_burstTime[i],'                     ',Compile_time[i],'                              ',TAT[i],'                     ',Wt[i])

        
