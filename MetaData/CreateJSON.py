from MiniAODSamples_H4G import *
from os import walk
from os import listdir
from os.path import isfile, join
from ROOT import *

inputlist = samples

location = "/tmp/rateixei/eos/cms/store/user/rateixei/H4G/MicroAOD/SigH4G_80X_v1/rel808/"

outFile = open('H4G_datasets.json', 'w')
outFile.write("{\n")
for j,s in enumerate(samples):
    print s
    datasetName = s.split("/")[1]
    subdirs = [x[0] for x in walk(location+datasetName)]
    files = []
    for sub in subdirs:
#       print sub
       if 'fail' in sub:
          continue
       theseFiles = [f for f in listdir(sub) if isfile(join(sub, f))]
       for f in theseFiles:
          fname = sub+"/"+f
          rfile = TFile(fname, "READ")
          tree = rfile.Get("Events")
          entries = tree.GetEntries()
          rfile.Close()
          fnameFinal = fname.replace("/tmp/rateixei/eos/cms", "")
          print fnameFinal, entries
          files.append([fnameFinal,entries])
    if len(files) > 0:
       outFile.write('\t "'+s+'": {\n')
       outFile.write('\t \t "files" : [\n')
       for i,f in enumerate(files):
          outFile.write('\t \t \t {\n')
          outFile.write('\t \t \t "name": "'+f[0]+'",\n')
          outFile.write('\t \t \t "nevents": '+str(f[1])+'\n')
          if i < len(files) - 1: outFile.write('\t \t \t },\n')
          if i == len(files) - 1: outFile.write('\t \t \t }\n')
       outFile.write('\t \t ]\n')
       if j < len(samples) - 1: outFile.write('\t },\n')
       if j == len(samples) - 1: outFile.write('\t }\n')

outFile.write("}")
outFile.close()
