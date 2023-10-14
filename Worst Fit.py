processSize = [212, 417, 112, 426]
blockSize = [100, 500, 200, 300, 600]

copyBlockSize = blockSize.copy()
copyBlockSize.sort(reverse = True)#[25,35,82]

blockNumber = [0]*len(processSize)
def indexfinder(n,arr):
    tem = n
    for i in range(len(arr)):
        if arr[i] == n:
            return i+1
            
            

for i in range(len(processSize)):
    for j in range(len(copyBlockSize)):
        if processSize[i]<=copyBlockSize[j]:
            B_num = indexfinder(copyBlockSize[j],blockSize)
            blockNumber[i] = B_num
            blockSize[B_num-1] = blockSize[B_num-1]-processSize[i]
            copyBlockSize[j]= copyBlockSize[j]-processSize[i]
            break
            
        if processSize[i]>=copyBlockSize[j]:
            B_num = indexfinder(copyBlockSize[j],blockSize)
            blockNumber[i] = 'not allocated'
            
            
            
print('process          ','Process Size             ','Block Number')
for i in range(len(processSize)):
    print('     ',i+1,'              ',processSize[i],'                     ',blockNumber[i])