processSize= [10,20,30]
blockSize = [5,10,20]
blockNumber = [0]*len(processSize)
tem = 0

for i in range(len(processSize)):
    for j in range(tem,len(blockSize)):
        if processSize[i]<=blockSize[j]:
            blockSize[j] = blockSize[j]-processSize[i]
            blockNumber[i] = j+1
            tem = j
            break
        if processSize[i]>=blockSize[j]:
            blockNumber[i] = 'not allocated'
            
            
            
print('Process','       ','Process Size','      ','Block Number')
for i in range(len(processSize)):
    print(' ',i+1,'                 ',processSize[i],'               ',blockNumber[i])
