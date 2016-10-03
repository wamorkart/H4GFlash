import os
from os import listdir
from os.path import isfile, join
import time

mypath = '/tmp/rateixei/eos/cms/store/user/rateixei/H4G/FlatTrees/data/'
rootpath = 'root://eoscms//eos/cms/store/user/rateixei/H4G/FlatTrees/data/'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

outtxt = '''
#!/bin/bash

cd /afs/cern.ch/work/r/rateixei/work/NEU_H4G/Flashgg/Aug24/CMSSW_8_0_8_patch1/src/flashgg/H4GFlash/TreeSkimmerPy
eval `scramv1 runtime -sh`

python H4GTreeSkimmer.py -i INFILE -o root/OUTFILE -p 4 -f 0
'''

counter = 0
for f in onlyfiles:
   ffull = rootpath+f
   bfile = 'runner_'+str(counter)+'.sh'
   outfile = open(bfile, 'w')
   outtxt1 = outtxt.replace('INFILE', ffull)
   outtxt2 = outtxt1.replace('OUTFILE', f.replace('.root', '_SEL_SignalRegion.root'))
   outfile.write(outtxt2)
   outfile.close()
   os.system('chmod a+rwx '+bfile)
   os.system('bsub -J runner'+str(counter)+' -q 8nh < '+bfile)
#   time.sleep(1)
   os.system('rm '+bfile)
   counter += 1
