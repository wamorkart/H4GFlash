#!/usr/bin/python
import numpy as n
from ROOT import *
import sys, getopt
from array import array
from H4GSkimTools import *

def main(argv):
   inputfiles = ''
   outputfile = 'output.root'
   maxEvts = -1
   nfakes = 0
   ntotpho = 4
   try:
      opts, args = getopt.getopt(argv,"hi:o:m:p:f:",["inputFiles=","outputFile=","maxEvents=","nphotons=","nfakes="])
   except getopt.GetoptError:
      print 'H4GTreeAnalyzer.py -i <inputfile1,inputfile2,inputfile3...> -o <outputfile> -m <maxEvts> -p <nphos> -f <nfakes>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile1,inputfile2,inputfile3...> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--inputFiles"):
         inputfiles = arg
      elif opt in ("-o", "--outputFile"):
         outputfile = arg
      elif opt in ("-m", "--maxEvents"):
         maxEvts = long(arg)
      elif opt in ("-p", "--nphotons"):
         ntotpho = int(arg)
      elif opt in ("-f", "--nfakes"):
         nfakes = int(arg)

   listOfFiles = inputfiles.split(",")
   print "Number of input files: ", len(listOfFiles)

   tree = TChain("h4gflash/H4GTree")
   for f in listOfFiles:
      print "\t Adding file:", f
      tree.AddFile(f)
   print "Total number of events to be analyzed:", tree.GetEntries()

   outRoot = TFile(outputfile, "RECREATE")

   treeSkimmer = SkimmedTreeTools()
   outTree = treeSkimmer.MakeSkimmedTree()

   triggers = {}
   triggerNames = []
   fraction = []

   evtCounter = 0
   treeSkimmer.initialEvents[0] = tree.GetEntries()
   eventsToRun = min(maxEvts, tree.GetEntries())
   if maxEvts < 0:
      eventsToRun = tree.GetEntries()
   #Tree Loop:
   for evt in range(0, eventsToRun):
      if evt%1000 == 0: print "## Analyzing event ", evt
      tree.GetEntry(evt)

      treeSkimmer.event[0] = tree.event
      treeSkimmer.run[0] = tree.run
      treeSkimmer.lumi[0] = tree.lumi
      treeSkimmer.nvtx[0] = tree.nvtx
      treeSkimmer.npu[0] = tree.npu

      Phos = []
      Phos_id = []

      for p in range(0, tree.n_pho):
        p4 = TLorentzVector(0,0,0,0)
        p4.SetPtEtaPhiM( tree.v_pho_pt[p], tree.v_pho_eta[p], tree.v_pho_phi[p], 0 )
        minDR = 999
        for Pho in Phos:
           dr = Pho.DeltaR(p4)
           if dr < minDR:
              minDR = dr
        if minDR > 0.001:
           Phos.append(p4)
           Phos_id.append(p)


      #Make photon selection first because the triggered photons *must* be selected
      sPhos,sPhos_id = treeSkimmer.MakePhotonSelection(Phos, Phos_id, tree.v_pho_mva, tree.v_pho_passElectronVeto)

      if nfakes > 0 :
         fPhos, fPhos_id = treeSkimmer.SelectWithFakes(Phos, Phos_id, tree.v_pho_mva, tree.v_pho_passElectronVeto)
         if len(fPhos) < nfakes:
            continue
         if len(sPhos) < ntotpho - nfakes:
            continue
         phomatrix = [[x,y] for x,y in zip(sPhos, sPhos_id)]
         fakematrix = [[x,y] for x,y in zip(fPhos, fPhos_id)]
         phomatrixreduced = phomatrix[:(ntotpho-nfakes)]
         fakematrixreduced = fakematrix[:(nfakes)]
         totmatrix = phomatrixreduced+fakematrixreduced
         totmatrix.sort(key=lambda x: x[0].Pt(), reverse=True)
         sPhos = [x[0] for x in totmatrix]
         sPhos_id = [x[1] for x in totmatrix]

      if len(sPhos) < ntotpho: continue # ntotpho, i.e total number of photons should always be =4

      #R9, CHIso, HoE, PSeed
      triggeredDipho = treeSkimmer.MakeTriggerSelection(sPhos, sPhos_id, tree.v_pho_full5x5_r9, tree.v_pho_chargedHadronIso, tree.v_pho_hadronicOverEm, tree.v_pho_hasPixelSeed)

      if triggeredDipho == 0: #no diphoton triggered
        continue
      
      

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

      treeSkimmer.p1_mva[0] = tree.v_pho_mva[sPhos_id[0]]
      treeSkimmer.p2_mva[0] = tree.v_pho_mva[sPhos_id[1]]
      treeSkimmer.p3_mva[0] = tree.v_pho_mva[sPhos_id[2]]
      treeSkimmer.p4_mva[0] = tree.v_pho_mva[sPhos_id[3]]

      treeSkimmer.p_mindr[0] = min( sPhos[0].DeltaR(sPhos[1]), sPhos[0].DeltaR(sPhos[2]), sPhos[0].DeltaR(sPhos[3]), sPhos[1].DeltaR(sPhos[2]), sPhos[1].DeltaR(sPhos[3]), sPhos[2].DeltaR(sPhos[3]) )
      
      P12 = sPhos[0] + sPhos[1]
      treeSkimmer.dphigh_mass[0] = P12.M()

      pairedDiphos = treeSkimmer.MakePairing(sPhos)
      #arr = [[Dipho1, P1, iP1, P2, iP2], [Dipho2, P3, iP3, P4, iP4]
      PP1 = pairedDiphos[0][0]
      PP2 = pairedDiphos[1][0]
      
      treeSkimmer.dp1_p1i[0] = pairedDiphos[0][2]
      treeSkimmer.dp1_p2i[0] = pairedDiphos[0][4]
      treeSkimmer.dp2_p1i[0] = pairedDiphos[1][2]
      treeSkimmer.dp2_p2i[0] = pairedDiphos[1][4]

      if(DEBUG): print pairedDiphos
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

      evtCounter += 1

      outTree.Fill()
   #end of event loop!

   outRoot.cd()
   outTree.Write()
   outRoot.Close()

	

if __name__ == "__main__":
   main(sys.argv[1:])


