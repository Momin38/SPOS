blockSize = [100,500,200,300,600]
processSize = [212,417,112,426]
blockNumber = [0]*len(blockSize)



for i in range(len(processSize)):
    for j in range(len(blockSize)):
        if processSize[i] <= blockSize[j]:
            blockSize[j]=blockSize[j]-processSize[i]
            blockNumber[i]=j+1
            break
        if processSize[i] >= blockSize[j]:
            blockNumber[i] = 'not allocated'
        
        
print('process','       ','process size','      ','block number')
for i in range(len(processSize)):
    print('  ',i+1,'             ',processSize[i],'               ',blockNumber[i])