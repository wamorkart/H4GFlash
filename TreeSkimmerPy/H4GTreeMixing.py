#!/usr/bin/python
import numpy as n
from ROOT import *
import sys, getopt
from array import array
from H4GSkimTools import *



from optparse import OptionParser




if __name__ == '__main__':

    
  parser = OptionParser()
  parser.add_option(   "-i", "--inputFile",   dest="inputFile",    default="input.root",       type="string",  help="Input file" )
  parser.add_option(   "-o", "--outputFile",  dest="outputFile",   default="output.root",      type="string",  help="Output file")
  
  
  #/afs/cern.ch/user/a/amassiro/public/H4G/signal_m_50.root                      
  
  (options, args) = parser.parse_args()
 
  itree = TChain("H4GSel")
  
  itree.AddFile(options.inputFile)
  
   
  print "Total number of events to be analyzed:", itree.GetEntries()
  
  outRoot = TFile(options.outputFile, "RECREATE")
  
  treeSkimmer = SkimmedTreeTools()
  otree = treeSkimmer.MakeSkimmedTree()


  #for b in itree.GetListOfBranches():
    #b.SetStatus(0)
  
  #otree = itree.CloneTree(0)
  ## BUT keep all branches "active" in the old tree
  #itree.SetBranchStatus('*'  ,1)
  
  
  # prepare for the loop ...
  eventsToRun = itree.GetEntries()
   
  print " itree.GetListOfBranches = ", itree.GetListOfBranches
  
  # and loop
  for evt in range(0, eventsToRun-1):
    if evt%1000 == 0: print "## Analyzing event ", evt
    itree.GetEntry(evt)
  
    treeSkimmer.FillEvent(itree)

    itree.GetEntry(evt+1)
    
    # (1) and (2) from the next one
    ObjList = [key.GetName() for key in  itree.GetListOfBranches()]  
    #for branch in ObjList:
      #if branch.startswith("p1_")  or  branch.startswith("p2_") :
        #getattr(treeSkimmer, branch)[0] = getattr(itree, branch)
    for branch in ObjList:
      nameToSearch1 = "p" + dp1_p1i + "_"
      nameToSearch1.replace(' ', '')
      nameToSearch2 = "p" + dp2_p1i + "_"
      nameToSearch2.replace(' ', '')
      if branch.startswith(nameToSearch1)  or  branch.startswith(nameToSearch2) :
        getattr(treeSkimmer, branch)[0] = getattr(itree, branch)
        
            
      




    
    otree.Fill()
    
    
  
  outRoot.cd()
  otree.Write()
  outRoot.Close()
  
 