import multiprocessing as mp, os

def process_wrapper(chunkStart, chunkSize):
   with open("input.txt") as f:
       f.seek(chunkStart)
       lines = f.read(chunkSize).splitlines()
       for line in lines:
           process(line)

def chunkify(fname,size=1024*1024):
   fileEnd = os.path.getsize(fname)
   with open(fname,'r') as f:
       chunkEnd = f.tell()
   while True:
       chunkStart = chunkEnd
       f.seek(size,1)
       f.readline()
       chunkEnd = f.tell()
       yield chunkStart, chunkEnd - chunkStart
       if chunkEnd > fileEnd:
           break

pool = mp.Pool(cores)
jobs = []

for chunkStart,chunkSize in chunkify("input.txt"):
   jobs.append( pool.apply_async(process_wrapper,(chunkStart,chunkSize)) )

for job in jobs:
   job.get()

pool.close()