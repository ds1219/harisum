import sys
import threading
from queue import Queue
from tqdm import tqdm
from libhs import checksum

def colourPrint(text, colour):
    colours = {
        'no-match-red' : '\033[91m',
        'match-green' : '\033[92m',
        'error-yellow' : '\033[93m',
        'regular-cyan' : '\033[96m'
    }

    print(colours[colour] + text + '\033[0m' )

if (len(sys.argv) <=2):
    print('Not enough arguments')
    quit()

file = sys.argv[1]
algo = sys.argv[2].lower()
 
if ( len(sys.argv) >= 4):
     preSum = sys.argv[3]
else:
     preSum = ''

q = Queue()
t1 = threading.Thread(target = checksum, args=(file, preSum, algo, q))
t1.start()

numofReads = q.get()

with tqdm(total=numofReads) as pgbar:
    i = 0 #current value
    j = 0 #previous value
    while i < numofReads:
        i = q.get()
        try:
            i = int(i)
            pgbar.update(i-j)
            j = i
        except:
            result = i
            break
t1.join()

if result == 'match':
    colourPrint("[✓] The checksum matches!", 'match-green')

elif result == 'not match':
    colourPrint("[✗] The checksum does not match!", 'no-match-red')

elif result == 'invalid algo':
    colourPrint("[✗] cannot recognise algorithm", "error-yellow")

else:
    colourPrint(result, "regular-cyan")
