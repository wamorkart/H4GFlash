#!/usr/bin/python
import numpy as n
from ROOT import *
import sys, getopt
from array import array
from H4GSkimTools import *



from optparse import OptionParser


import operator



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
  for evt in range(0, eventsToRun):
    if evt%1000 == 0: print "## Analyzing event ", evt
    itree.GetEntry(evt)
  
    treeSkimmer.FillEvent(itree)

    #dp1_p1i = itree.dp1_p1i
    #dp2_p1i = itree.dp2_p1i

    dp1_p1i = 1
    dp2_p1i = 2

 
    #print " dp2_p1i = ", dp2_p1i, "   dp1_p1i  = ", dp1_p1i, 
    
    # if it is the last event, pick the shuffled from the first event
    if evt == eventsToRun :
      itree.GetEntry(0)
    else :
      itree.GetEntry(evt+1)
    
    #print " ---> dp2_p1i = ", dp2_p1i, "   dp1_p1i  = ", dp1_p1i
    
    # (1) and (2) from the next one
    ObjList = [key.GetName() for key in  itree.GetListOfBranches()]  
    #for branch in ObjList:
      #if branch.startswith("p1_")  or  branch.startswith("p2_") :
        #getattr(treeSkimmer, branch)[0] = getattr(itree, branch)
    for branch in ObjList:
      nameToSearch1 = "p" + str(dp1_p1i) + "_"
      nameToSearch1.replace(' ', '')
      nameToSearch2 = "p" + str(dp2_p1i) + "_"
      nameToSearch2.replace(' ', '')
      if branch.startswith(nameToSearch1)  or  branch.startswith(nameToSearch2) :
        getattr(treeSkimmer, branch)[0] = getattr(itree, branch)
        
        
        
        
    order_photons = {
          1: treeSkimmer.p1_pt,
          2: treeSkimmer.p2_pt,
          3: treeSkimmer.p3_pt,
          4: treeSkimmer.p4_pt
          }
    sorted_order_photons = sorted(order_photons.items(), key=operator.itemgetter(1))
    sorted_order_photons.reverse()   # from high to low
    
    #print " sorted_order_photons = ", sorted_order_photons
    
    sPhos = []
    sPhos_mva = []
    #for iphoton in range(0, 4):  # 4 photons
    for iphoton in sorted_order_photons:
      p4 = TLorentzVector(0,0,0,0)
      name_pt  = "p" + str( int(iphoton [0] ) ) + "_pt"
      name_eta = "p" + str( int(iphoton [0] ) ) + "_eta"
      name_phi = "p" + str( int(iphoton [0] ) ) + "_phi"
      name_mva = "p" + str( int(iphoton [0] ) ) + "_mva"

      p4.SetPtEtaPhiM( getattr(treeSkimmer, name_pt),  getattr(treeSkimmer, name_eta),    getattr(treeSkimmer, name_phi) , 0 )
      sPhos.append(p4)
      sPhos_mva.append(getattr(treeSkimmer, name_mva))
      
    for iphoton in range(0, 4):  # 4 photons
      name_mva = "p" + str(iphoton+1) + "_mva"
      getattr(treeSkimmer, name_mva)[0] = sPhos_mva[iphoton]


    treeSkimmer.p1_pt[0] = sPhos[0].Pt()
    treeSkimmer.p2_pt[0] = sPhos[1].Pt()
    treeSkimmer.p3_pt[0] = sPhos[2].Pt()
    treeSkimmer.p4_pt[0] = sPhos[3].Pt()
    treeSkimmer.p1_eta[0] = sPhos[0].Eta()
    treeSkimmer.p2_eta[0] = sPhos[1].Eta()
    treeSkimmer.p3_eta[0] = sPhos[2].Eta()
    treeSkimmer.p4_eta[0] = sPhos[3].Eta()
    treeSkimmer.p1_phi[0] = sPhos[0].Phi()
    treeSkimmer.p2_phi[0] = sPhos[1].Phi()
    treeSkimmer.p3_phi[0] = sPhos[2].Phi()
    treeSkimmer.p4_phi[0] = sPhos[3].Phi()


    treeSkimmer.p_mindr[0] = min( sPhos[0].DeltaR(sPhos[1]), sPhos[0].DeltaR(sPhos[2]), sPhos[0].DeltaR(sPhos[3]), sPhos[1].DeltaR(sPhos[2]), sPhos[1].DeltaR(sPhos[3]), sPhos[2].DeltaR(sPhos[3]) )
    
    P12 = sPhos[0] + sPhos[1]
    treeSkimmer.dphigh_mass[0] = P12.M()

    pairedDiphos = treeSkimmer.MakePairing(sPhos)
    PP1 = pairedDiphos[0][0]
    PP2 = pairedDiphos[1][0]
    
    treeSkimmer.dp1_p1i[0] = pairedDiphos[0][2]
    treeSkimmer.dp1_p2i[0] = pairedDiphos[0][4]
    treeSkimmer.dp2_p1i[0] = pairedDiphos[1][2]
    treeSkimmer.dp2_p2i[0] = pairedDiphos[1][4]

    treeSkimmer.dp1_dr[0] = pairedDiphos[0][1].DeltaR(pairedDiphos[0][3])
    treeSkimmer.dp2_dr[0] = pairedDiphos[1][1].DeltaR(pairedDiphos[1][3])

    treeSkimmer.dp1_pt[0] = PP1.Pt()
    treeSkimmer.dp1_eta[0] = PP1.Eta()
    treeSkimmer.dp1_phi[0] = PP1.Phi()
    treeSkimmer.dp1_mass[0] = PP1.M()
    treeSkimmer.dp2_pt[0] = PP2.Pt()
    treeSkimmer.dp2_eta[0] = PP2.Eta()
    treeSkimmer.dp2_phi[0] = PP2.Phi()
    treeSkimmer.dp2_mass[0] = PP2.M()

    Pgggg = sPhos[0] + sPhos[1] + sPhos[2] + sPhos[3]
    treeSkimmer.tp_pt[0] = Pgggg.Pt()
    treeSkimmer.tp_eta[0] = Pgggg.Eta()
    treeSkimmer.tp_phi[0] = Pgggg.Phi()
    treeSkimmer.tp_mass[0] = Pgggg.M()


    
    otree.Fill()
    
    
  
  outRoot.cd()
  otree.Write()
  outRoot.Close()
  
 