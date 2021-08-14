import hashlib
from os import path
from math import ceil

def checksum(filepath, preSum, algo, q):
    preSum = preSum.lower()

    #calculate the checksum
    if algo == 'sha1':
        fileHash = hashlib.sha1()
    elif algo == 'sha256':
         fileHash = hashlib.sha256()
    elif algo == 'md5':
        fileHash = hashlib.md5()
    else:
        return('invalid algo')

    #read the file chunk by chunk
    with open(filepath,'rb') as f:
        numOfReads = ceil(path.getsize(filepath) / 1024)
        q.put(numOfReads)

        #only send i if queue is empty
        for i in range(0,numOfReads):
            fileHash.update(f.read(1024))

            if q.empty():
                q.put(i)
            else:
            # check if stop is sent then replace value
                i = q.get()
                if i == 'stop':
                    quit()
                else:
                    q.put(i)
        fileHash = fileHash.hexdigest()
    
    #check if checksum matches the presum
    if preSum == '' or preSum == ' ' or preSum == 'invalid algo':
        q.put(fileHash)
    elif fileHash == preSum:
        q.put('match')
    else:
        q.put('not match')

def getico():
    from glob import glob
    print(glob('./assets/logo.ico'))