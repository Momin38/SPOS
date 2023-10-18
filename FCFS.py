pro = ['p1','p2','p3','p4']
arrivalTime = [0,1,5,6]
burstTime = [2,2,3,4]

def listSorting(processes,arrTime,burstTime):
    combine_list = zip(processes,arrivalTime,burstTime)
    sorted_list = sorted(*combine_list,key=lambda x:x[1])
    return processes,arrivalTime,burstTime
    

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
    
    
listSorting(pro,arrivalTime,burstTime)
        
