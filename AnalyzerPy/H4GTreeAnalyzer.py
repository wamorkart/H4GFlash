#!/usr/bin/python

from ROOT import *
import sys, getopt
from array import array

def main(argv):
   inputfiles = ''
   outputfile = 'output.root'
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["inputFiles=","outputFile="])
   except getopt.GetoptError:
      print 'H4GTreeAnalyzer.py -i <inputfile1,inputfile2,inputfile3...> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile1,inputfile2,inputfile3...> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--inputFiles"):
         inputfiles = arg
      elif opt in ("-o", "--outputFile"):
         outputfile = arg

   listOfFiles = inputfiles.split(",")
   print "Number of input files: ", len(listOfFiles)

   tree = TChain("h4gflash/H4GTree")
   for f in listOfFiles:
      print "\t Adding file:", f
      tree.AddFile(f)
   print "Total number of events to be analyzed:", tree.GetEntries()

   outRoot = TFile(outputfile, "RECREATE")

   h_p1_pt = TH1F("h_p1_pt", "p_{T} of 1st photon; p_{T}(#gamma_{1}) [GeV];Events", 100, 0, 150)
   h_p2_pt = TH1F("h_p2_pt", "p_{T} of 2nd photon; p_{T}(#gamma_{2}) [GeV];Events", 100, 0, 150)
   h_p3_pt = TH1F("h_p3_pt", "p_{T} of 3rd photon; p_{T}(#gamma_{3}) [GeV];Events", 100, 0, 150)
   h_p4_pt = TH1F("h_p4_pt", "p_{T} of 4th photon; p_{T}(#gamma_{4}) [GeV];Events", 100, 0, 150)
   h_mggPP1 = TH1F("h_mggPP1", "DiPhoton Invariant Mass with 1st and 2nd photons; M(#gamma#gamma) [GeV];Events", 100, 0, 160)
   h_mggPP2 = TH1F("h_mggPP2", "DiPhoton Invariant Mass with 1st and 2nd photons; M(#gamma#gamma) [GeV];Events", 100, 0, 160)
   h_mgg12 = TH1F("h_mgg12", "DiPhoton Invariant Mass with 1st and 2nd photons; M(#gamma#gamma) [GeV];Events", 100, 0, 160)
   h_mgg13 = TH1F("h_mgg13", "DiPhoton Invariant Mass with 1rd and 3rd photons; M(#gamma#gamma) [GeV];Events", 100, 0, 160)
   h_mgg14 = TH1F("h_mgg14", "DiPhoton Invariant Mass with 1rd and 4th photons; M(#gamma#gamma) [GeV];Events", 100, 0, 160)
   h_mgg23 = TH1F("h_mgg23", "DiPhoton Invariant Mass with 2nd and 3rd photons; M(#gamma#gamma) [GeV];Events", 100, 0, 160)
   h_mgg24 = TH1F("h_mgg24", "DiPhoton Invariant Mass with 2nd and 4th photons; M(#gamma#gamma) [GeV];Events", 100, 0, 160)
   h_mgg34 = TH1F("h_mgg34", "DiPhoton Invariant Mass with 3rd and 4th photons; M(#gamma#gamma) [GeV];Events", 100, 0, 160)
   h_mgggg = TH1F("h_mgggg", "TetraPhoton Invariant mass; M(#gamma#gamma#gamma#gamma) [Gev]; Events", 100, 0, 160)
   h_n_pho = TH1F("h_n_pho", "Number of photons; Number of Photons; Events", 10, 0, 10)
   h_n_pho_clean = TH1F("h_n_pho_clean", "Number of photons; Number of Photons; Events", 10, 0, 10)

   h_mgg12_gen = TH1F("h_mgg12_gen", "DiPhoton Invariant Mass with 1st and 2nd photons; M(#gamma#gamma) [GeV];Events", 100, 0, 160)
   h_mgg13_gen = TH1F("h_mgg13_gen", "DiPhoton Invariant Mass with 1rd and 3rd photons; M(#gamma#gamma) [GeV];Events", 100, 0, 160)
   h_mgg14_gen = TH1F("h_mgg14_gen", "DiPhoton Invariant Mass with 1rd and 4th photons; M(#gamma#gamma) [GeV];Events", 100, 0, 160)
   h_mgg23_gen = TH1F("h_mgg23_gen", "DiPhoton Invariant Mass with 2nd and 3rd photons; M(#gamma#gamma) [GeV];Events", 100, 0, 160)
   h_mgg24_gen = TH1F("h_mgg24_gen", "DiPhoton Invariant Mass with 2nd and 4th photons; M(#gamma#gamma) [GeV];Events", 100, 0, 160)
   h_mgg34_gen = TH1F("h_mgg34_gen", "DiPhoton Invariant Mass with 3rd and 4th photons; M(#gamma#gamma) [GeV];Events", 100, 0, 160)

   triggers = {}
   triggerNames = []
   fraction = []
   
   evtCounter = 0
   #Tree Loop:
   for evt in range(0, tree.GetEntries()):
      if evt%1000 == 0: print "## Analyzing event ", evt
      tree.GetEntry(evt)

      Phos = []

      for p in range(0, tree.n_pho):
#        print "photon #", p, " pt:",tree.v_pho_pt[p]
        p4 = TLorentzVector(0,0,0,0)
        p4.SetPtEtaPhiE( tree.v_pho_pt[p], tree.v_pho_eta[p], tree.v_pho_phi[p], tree.v_pho_e[p])
        minDR = 999
        for Pho in Phos:
           dr = Pho.DeltaR(p4)
           if dr < minDR:
              minDR = dr
        if minDR > 0.0:
           Phos.append(p4)

#      print "Number of photons:", tree.n_pho
      if len(Phos) < 4:
         continue
#      if tree.passTrigger == 0:
#         continue

      gen1 = TLorentzVector(0,0,0,0)
      gen2 = TLorentzVector(0,0,0,0)
      gen3 = TLorentzVector(0,0,0,0)
      gen4 = TLorentzVector(0,0,0,0)
      if tree.v_genpho_p4.size() > 0:
         gen1.SetPtEtaPhiE(tree.v_genpho_p4[0].pt(), tree.v_genpho_p4[0].eta(), tree.v_genpho_p4[0].phi(), tree.v_genpho_p4[0].e())
      if tree.v_genpho_p4.size() > 1:
         gen2.SetPtEtaPhiE(tree.v_genpho_p4[1].pt(), tree.v_genpho_p4[1].eta(), tree.v_genpho_p4[1].phi(), tree.v_genpho_p4[1].e())
      if tree.v_genpho_p4.size() > 2:
         gen3.SetPtEtaPhiE(tree.v_genpho_p4[2].pt(), tree.v_genpho_p4[2].eta(), tree.v_genpho_p4[2].phi(), tree.v_genpho_p4[2].e())
      if tree.v_genpho_p4.size() > 3:
         gen4.SetPtEtaPhiE(tree.v_genpho_p4[3].pt(), tree.v_genpho_p4[3].eta(), tree.v_genpho_p4[3].phi(), tree.v_genpho_p4[3].e())

      gen12 = gen1+gen2
      gen13 = gen1+gen3
      gen14 = gen1+gen4
      gen23 = gen2+gen3
      gen24 = gen2+gen4
      gen34 = gen3+gen4
      h_mgg12_gen.Fill(gen12.M())
      h_mgg13_gen.Fill(gen13.M())
      h_mgg14_gen.Fill(gen14.M())
      h_mgg23_gen.Fill(gen23.M())
      h_mgg24_gen.Fill(gen24.M())
      h_mgg34_gen.Fill(gen34.M())
      

      h_n_pho.Fill(tree.n_pho)
      h_n_pho_clean.Fill(len(Phos))

      P1 = Phos[0]
      P2 = Phos[1]
      P3 = Phos[2]
      P4 = Phos[3]

      h_p1_pt.Fill(P1.Pt())
      h_p2_pt.Fill(P2.Pt())
      h_p3_pt.Fill(P3.Pt())
      h_p4_pt.Fill(P4.Pt())

      P12 = P1 + P2
      h_mgg12.Fill(P12.M())
      P13 = P1 + P3
      h_mgg13.Fill(P13.M())
      P14 = P1 + P4
      h_mgg14.Fill(P14.M())
      P23 = P2 + P3
      h_mgg23.Fill(P23.M())
      P24 = P2 + P4
      h_mgg24.Fill(P24.M())
      P34 = P3 + P4
      h_mgg34.Fill(P34.M())

      diff_12_34 = abs(P12.M() - P34.M())
      diff_13_24 = abs(P13.M() - P24.M())
      diff_14_23 = abs(P14.M() - P23.M())
      
      PP1 = ""
      PP2 = ""
      if diff_12_34 < diff_13_24 and diff_12_34 < diff_14_23:
         PP1 = P12
         PP2 = P34
      if diff_13_24 < diff_12_34 and diff_13_24 < diff_14_23:
         PP1 = P13
         PP2 = P24
      if diff_14_23 < diff_12_34 and diff_14_23 < diff_13_24:
         PP1 = P14
         PP2 = P23

      h_mggPP1.Fill(PP1.M())
      h_mggPP2.Fill(PP2.M())

      Pgggg = P1 + P2 + P3 + P4
      h_mgggg.Fill(Pgggg.M())

      for mt in tree.myTriggerResults:
#         print mt.first, mt.second
         if mt.first in triggers:
            triggers[mt.first] += mt.second
         if mt.first not in triggers:
            triggers[mt.first] = mt.second
      evtCounter += 1

   x = []
   xNames = []
   y = []
   counter = 0
   for tr in triggers:
      x.append(counter)
      y.append(float(triggers[tr])/float(evtCounter))
      xNames.append(tr)
      counter +=1

   X = array("d", x)
   Y = array("d", y)
   gr = TGraph(len(x), X, Y)
   
   grX = gr.GetXaxis()
   print len(xNames), grX.GetNbins()
   for i in x:
      grX.SetBinLabel(grX.FindBin(i), xNames[i])

   outRoot.cd()
   h_p1_pt.Write()
   h_p2_pt.Write()
   h_p3_pt.Write()
   h_p4_pt.Write()
   h_mgg12.Write()
   h_mgg13.Write()
   h_mgg14.Write()
   h_mgg23.Write()
   h_mgg24.Write()
   h_mgg34.Write()
   h_mgggg.Write()
   h_n_pho.Write()
   h_mggPP1.Write()
   h_mggPP2.Write()
   h_n_pho_clean.Write()
   gr.Write()
   h_mgg12_gen.Write()
   h_mgg13_gen.Write()
   h_mgg14_gen.Write()
   h_mgg23_gen.Write()
   h_mgg24_gen.Write()
   h_mgg34_gen.Write()

   outRoot.Close()

	

if __name__ == "__main__":
   main(sys.argv[1:])

