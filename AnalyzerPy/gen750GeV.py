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
    
 

  
   h_p1_pt = TH1F("h_p1_pt", "p_{T} of Photons; p_{T}(#gamma) [GeV];Events", 100, 0, 650)
   h_p2_pt = TH1F("h_p2_pt", "p_{T} of 2nd photon; p_{T}(#gamma_{2}) [GeV];Events", 100, 0, 650)
   h_p3_pt = TH1F("h_p3_pt", "p_{T} of 3rd photon; p_{T}(#gamma_{3}) [GeV];Events", 100, 0, 650)
   h_p4_pt = TH1F("h_p4_pt", "p_{T} of Photons; p_{T}(#gamma) [GeV];Events", 100, 0, 650)
   h_gen_mggPP1=TH1F("h_gen_mggPP1", "a1 and a2 :Mass; M(#gamma#gamma) [GeV];Events", 100, 0, 1000)
   h_gen_mggPP2=TH1F("h_gen_mggPP2", " gen a1 and a2 :Mass; M(#gamma#gamma) [GeV];Events", 100, 0, 1000)
   h_mggPP1 = TH1F("h_mggPP1", "a1 and a2 :Mass; M(#gamma#gamma) [GeV];Events", 100, 200, 500)
   h_mggPP2 = TH1F("h_mggPP2", "a1 and a2: Mass; M(#gamma#gamma) [GeV];Events", 100, 200, 500) 
   h_deltam = TH1F("h_deltam","a1 and a2 mass difference; #Delta m [GeV];Events",100,-700,700)
   h_gen_deltam = TH1F("h_gen_deltam","gen a1 and a2 mass difference; #Delta m [GeV];Events",100,-700,700)
   h_mggPP1pt = TH1F("h_mggPP1pt","p_{T} of a1; p_{T}(a_{1}) [GeV];Events",100,0,650)
   h_mggPP2pt = TH1F("h_mggPP2pt","a1 and a2 : p_{T}; p_{T} [GeV];Events",100,0,650)
   h_gen_mggPP1pt = TH1F("h_gen_mggPP1pt"," gen a1 and a2 :p_{T};p_{T} [GeV];Events",100,0,650)
   h_gen_mggPP2pt = TH1F("h_gen_mggPP2pt"," gen a1 and a2 :p_{T};p_{T} [GeV];Events",100,0,650)
   h_mggPP1pz = TH1F("h_mggPP1pz","a1 pz; p_{z} [GeV];Events",100,-300,300)
   h_mggPP2pz = TH1F("h_mggPP2pz","a1 and a2: p_{z}; p_{z} [GeV];Events",100,-300,300)
   h_gen_mggPP1pz = TH1F("h_gen_mggPP1pz","a1 pz; p_{z} [GeV];Events",100,-900,900)
   h_gen_mggPP2pz = TH1F("h_gen_mggPP2pz","gen a1 and a2: p_{z}; p_{z} [GeV];Events",100,-900,900)


   h_mgg12 = TH1F("h_mgg12", "DiPhoton Invariant Mass with 1st and 2nd photons; M(#gamma#gamma) [GeV];Events", 100, 0, 160)
   h_mgg13 = TH1F("h_mgg13", "DiPhoton Invariant Mass with 1rd and 3rd photons; M(#gamma#gamma) [GeV];Events", 100, 0, 160)
   h_mgg14 = TH1F("h_mgg14", "DiPhoton Invariant Mass with 1rd and 4th photons; M(#gamma#gamma) [GeV];Events", 100, 0, 160)
   h_mgg23 = TH1F("h_mgg23", "DiPhoton Invariant Mass with 2nd and 3rd photons; M(#gamma#gamma) [GeV];Events", 100, 0, 160)
   h_mgg24 = TH1F("h_mgg24", "DiPhoton Invariant Mass with 2nd and 4th photons; M(#gamma#gamma) [GeV];Events", 100, 0, 160)
   h_mgg34 = TH1F("h_mgg34", "DiPhoton Invariant Mass with 3rd and 4th photons; M(#gamma#gamma) [GeV];Events", 100, 0, 160)
   h_mgggg = TH1F("h_mgggg", "TetraPhoton Invariant mass; M(#gamma#gamma#gamma#gamma) [Gev]; Events", 100, 300,1200)
   h_gen_mgggg = TH1F("h_gen_mgggg", "gen TetraPhoton Invariant mass; M(#gamma#gamma#gamma#gamma) [Gev]; Events", 100, 300,1200)
   
   h_n_pho = TH1F("h_n_pho", "Number of photons; Number of Photons; Events", 10, 0, 10)
   h_n_pho_clean = TH1F("h_n_pho_clean", "Number of photons; Number of Photons; Events", 10, 0, 10)
   h_dr = TH1F("h_dr", "dr values; dr; Events",100,0,150)
   h_dr_12=TH1F("h_dr_12","12 dr values;dr12;Events",100,0,6)
   h_dr_13=TH1F("h_dr_13","13 dr values;dr13;Events",100,0,6)
   h_dr_14=TH1F("h_dr_14","14 dr values;dr14;Events",100,0,6)
   h_dr_23=TH1F("h_dr_23","23 dr values;dr23;Events",100,0,6)
   h_dr_24=TH1F("h_dr_24","24 dr values;dr24;Events",100,0,6)
   h_dr_34=TH1F("h_dr_34","34 dr values;dr34;Events",100,0,6)
   h_dr_1=TH1F("h_dr_1","1 dr values;dr1;Events",100,0,150)
   h_dr_2=TH1F("h_dr_2","2 dr values;dr2;Events",100,0,150)
   h_drPdr1=TH1F("h_dr1","1 dr values;dr1;Events",100,0,150)
   h_drPdr2=TH1F("h_dr2","2 dr values;dr2;Events",100,0,150)
   h_gen_dr_a1=TH1F("h_gen_dr_a1","gena1dr; gena1 dr;Events",100,0,6)
   h_gen_dr_a2=TH1F("h_gen_dr_a2","gen a1 and a2 : #Delta r; #Delta r;Events",100,0,6)
   h_mindr=TH1F("h_mindr","Minimum #Delta r;#Delta r;Events",100,0,3)
   h_gen_mindr=TH1F("h_gen_mindr","Gen Minimum #Delta r;#Delta r;Events",100,0,3)
   h_mgg12_gen = TH1F("h_mgg12_gen", "DiPhoton Invariant Mass with 1st and 2nd photons; M(#gamma#gamma) [GeV];Events", 100, 0, 700)
   h_mgg13_gen = TH1F("h_mgg13_gen", "DiPhoton Invariant Mass with 1rd and 3rd photons; M(#gamma#gamma) [GeV];Events", 100, 0, 700)
   h_mgg14_gen = TH1F("h_mgg14_gen", "DiPhoton Invariant Mass with 1rd and 4th photons; M(#gamma#gamma) [GeV];Events", 100, 0, 700)
   h_mgg23_gen = TH1F("h_mgg23_gen", "DiPhoton Invariant Mass with 2nd and 3rd photons; M(#gamma#gamma) [GeV];Events", 100, 0, 700)
   h_mgg24_gen = TH1F("h_mgg24_gen", "DiPhoton Invariant Mass with 2nd and 4th photons; M(#gamma#gamma) [GeV];Events", 100, 0, 700)
   h_mgg34_gen = TH1F("h_mgg34_gen", "DiPhoton Invariant Mass with 3rd and 4th photons; M(#gamma#gamma) [GeV];Events", 100, 0, 700)
   h_gen1_eta = TH1F("h_gen1_eta","gen1 eta;#eta;Events",100,-2.5,2.5)
   h_gen2_eta = TH1F("h_gen2_eta","gen2 eta;#eta;Events",100,-2.5,2.5)
   h_gen3_eta = TH1F("h_gen3_eta","gen3 eta;#eta;Events",100,-2.5,2.5)
   h_gen4_eta = TH1F("h_gen4_eta","gen #gamma eta;#eta;Events",100,-2.5,2.5)
   h_gen1_phi = TH1F("h_gen1_phi","gen #gamma phi;""#phi;Events",100,-4,4)
   h_gen2_phi = TH1F("h_gen2_phi","gen #gamma phi;""#phi;Events",100,-4,4)
   h_gen3_phi = TH1F("h_gen3_phi","gen #gamma phi;""#phi;Events",100,-4,4)
   h_gen4_phi = TH1F("h_gen4_phi","gen #gamma phi;""#phi;Events",100,-4,4)
   h_p1_phi = TH1F("h_p1_phi","#phi of photons; #phi(#gamma);Events",100,-4,4)
   h_p2_phi = TH1F("h_p2_phi","#eta of 2nd photon; #eta(#gamma_{2}));Events",100,-4,4)
   h_p3_phi = TH1F("h_p3_phi","#eta of 3rd photon; #eta(#gamma_{3}));Events",100,-4,4)
   h_p4_phi = TH1F("h_p4_phi","#phi of photons; #phi(#gamma);Events",100,-4,4)
   h_p1_eta = TH1F("h_p1_eta","#eta of photons; #eta(#gamma);Events",100,-2.5,2.5)
   h_p2_eta = TH1F("h_p2_eta","#eta of 2nd photon; #eta(#gamma_{2}));Events",100,-2.5,2.5)
   h_p3_eta = TH1F("h_p3_eta","#eta of 3rd photon; #eta(#gamma_{3}));Events",100,-2.5,2.5)
   h_p4_eta = TH1F("h_p4_eta","#eta of photons; #eta(#gamma);Events",100,-2.5,2.5)
   h_dr_a1 = TH1F("h_dr_a1","#Delta R1 (for a1); #Deltar a_{1};Events",100,0,6)
   h_dr_a2 = TH1F("h_dr_a2","a1 and a2 : #Delta r ; #Deltar;Events",100,0,6)
   h_gen_dphi_a1 = TH1F("h_gen_dphi_a1","gen a1 and a2 : #Delta #phi ; #Delta #phi; Events", 100,-4,4)
   h_gen_dphi_a2 = TH1F("h_gen_dphi_a2","gen a1 and a2 :#Delta #phi;#Delta #phi; Events",100,-4,4)
   h_gen_deta_a1 = TH1F("h_gen_deta_a1","gen a1 and a2 : #Delta #eta; #Delta #eta; Events", 100,-4,4)
   h_gen_deta_a2 = TH1F("h_gen_deta_a2","gen a1 and a2 :#Delta #eta;#delta #eta; Events",100,-4,4)
   h_dphi_a1 = TH1F("h_dphi_a1","gen a1 and a2 : #Delta #phi ; #Delta #phi; Events", 100,-4,4)
   h_dphi_a2 = TH1F("h_dphi_a2"," a1 and a2 : #Delta #phi ;#Delta #phi; Events",100,-4,4)
   h_deta_a1 = TH1F("h_deta_a1","gen a1 and a2 : #Delta #eta; #Delta #eta; Events", 100,-4,4)
   h_deta_a2 = TH1F("h_deta_a2","a1 and a2 :#Delta #eta;#Delta #eta; Events",100,-4,4)
   h_gen1_pt = TH1F("h_gen1_pt","gen1 p_{t}; p_{t};Events",100,0,650)
   h_gen2_pt = TH1F("h_gen2_pt","gen2 p_{t}; p_{t};Events",100,0,650)
   h_gen3_pt = TH1F("h_gen3_pt","gen3 p_{t}; p_{t};Events",100,0,650)
   h_gen4_pt = TH1F("h_pt","gen #gamma p_{t}; p_{t} [GeV];Events",100,0,650)
   
   

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
 #       print "photon #", p, " pt:",tree.v_pho_pt[p]
        p4 = TLorentzVector(0,0,0,0)
        p4.SetPtEtaPhiE( tree.v_pho_pt[p], tree.v_pho_eta[p], tree.v_pho_phi[p], tree.v_pho_e[p])
        minDR = 999
        for Pho in Phos:
           dr = Pho.DeltaR(p4)
           if dr < minDR:
              minDR = dr
        if minDR > 0.01:
           Phos.append(p4)
           

#      print "Number of photons:", tree.n_pho
      if len(Phos) < 4:
         continue
#      if tree.passTrigger == 0:
#         continue

      #gen1 = TLorentzVector(0,0,0,0)
      #gen2 = TLorentzVector(0,0,0,0)
      #gen3 = TLorentzVector(0,0,0,0)
      #gen4 = TLorentzVector(0,0,0,0)
      #if tree.v_genpho_p4.size() > 0:
       #  gen1.SetPtEtaPhiE(tree.v_genpho_p4[0].pt(), tree.v_genpho_p4[0].eta(), tree.v_genpho_p4[0].phi(), tree.v_genpho_p4[0].e())
      #if tree.v_genpho_p4.size() > 1:
       #  gen2.SetPtEtaPhiE(tree.v_genpho_p4[1].pt(), tree.v_genpho_p4[1].eta(), tree.v_genpho_p4[1].phi(), tree.v_genpho_p4[1].e())
      #if tree.v_genpho_p4.size() > 2:
       #  gen3.SetPtEtaPhiE(tree.v_genpho_p4[2].pt(), tree.v_genpho_p4[2].eta(), tree.v_genpho_p4[2].phi(), tree.v_genpho_p4[2].e())
      #if tree.v_genpho_p4.size() > 3:
       #  gen4.SetPtEtaPhiE(tree.v_genpho_p4[3].pt(), tree.v_genpho_p4[3].eta(), tree.v_genpho_p4[3].phi(), tree.v_genpho_p4[3].e())

     


      #gen12 = gen1+gen2
      #gen13 = gen1+gen3
      #gen14 = gen1+gen4
      #gen23 = gen2+gen3
      #gen24 = gen2+gen4
      #gen34 = gen3+gen4
      #h_mgg12_gen.Fill(gen12.M())
      #h_mgg13_gen.Fill(gen13.M())
      #h_mgg14_gen.Fill(gen14.M())
      #h_mgg23_gen.Fill(gen23.M())
      #h_mgg24_gen.Fill(gen24.M())
      #h_mgg34_gen.Fill(gen34.M())
      
      
         
      
      
     

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
      h_dr.Fill(dr)

      h_p1_eta.Fill(P1.Eta())
      h_p2_eta.Fill(P2.Eta())
      h_p3_eta.Fill(P3.Eta())
      h_p4_eta.Fill(P4.Eta())
      h_p1_phi.Fill(P1.Phi())
      h_p2_phi.Fill(P2.Phi())
      h_p3_phi.Fill(P3.Phi())
      h_p4_phi.Fill(P4.Phi())

      P12 = P1 + P2
      h_mgg12.Fill(P12.M())
      h_dr_12.Fill(P1.DeltaR(P2))
      P13 = P1 + P3
      h_dr_13.Fill(P1.DeltaR(P3))
      h_mgg13.Fill(P13.M())
      P14 = P1 + P4
      h_mgg14.Fill(P14.M())
      h_dr_14.Fill(P1.DeltaR(P4))
      P23 = P2 + P3
      h_mgg23.Fill(P23.M())
      h_dr_23.Fill(P2.DeltaR(P3))
      P24 = P2 + P4
      h_mgg24.Fill(P24.M())
      h_dr_24.Fill(P2.DeltaR(P4))
      P34 = P3 + P4
      h_mgg34.Fill(P34.M())
      h_dr_34.Fill(P3.DeltaR(P4))

      diff_12_34 = abs(P12.M() - P34.M())
      diff_13_24 = abs(P13.M() - P24.M())
      diff_14_23 = abs(P14.M() - P23.M())
      
      PP1 = ""
      PP2 = ""
      if diff_12_34 < diff_13_24 and diff_12_34 < diff_14_23:
         PP1 = P12
         PP2 = P34
         h_dr_a1.Fill(P1.DeltaR(P2))
         h_dr_a2.Fill(P3.DeltaR(P4))
         h_dphi_a1.Fill(P1.DeltaPhi(P2))
         h_dphi_a2.Fill(P3.DeltaPhi(P4))
         h_deta_a1.Fill(P1.Eta()-P2.Eta())
         h_deta_a2.Fill(P3.Eta()-P4.Eta())
        
      if diff_13_24 < diff_12_34 and diff_13_24 < diff_14_23:
         PP1 = P13
         PP2 = P24
         h_dr_a1.Fill(P1.DeltaR(P3))
         h_dr_a2.Fill(P2.DeltaR(P4))
         h_dphi_a1.Fill(P1.DeltaPhi(P3))
         h_dphi_a2.Fill(P2.DeltaPhi(P4))
         h_deta_a1.Fill(P1.Eta()-P3.Eta())
         h_deta_a2.Fill(P2.Eta()-P4.Eta()) 

      if diff_14_23 < diff_12_34 and diff_14_23 < diff_13_24:
         PP1 = P14
         PP2 = P23
         h_dr_a1.Fill(P1.DeltaR(P4))
         h_dr_a2.Fill(P2.DeltaR(P3))
         h_dphi_a1.Fill(P1.DeltaPhi(P4))
         h_dphi_a2.Fill(P2.DeltaPhi(P3))
         h_deta_a1.Fill(P1.Eta()-P4.Eta())
         h_deta_a2.Fill(P2.Eta()-P3.Eta())

    
      h_mindr.Fill(min(P1.DeltaR(P2), P1.DeltaR(P3), P1.DeltaR(P4), P2.DeltaR(P3), P2.DeltaR(P4), P3.DeltaR(P4)))

      
      
      

      h_mggPP1.Fill(PP1.M())
      h_mggPP2.Fill(PP2.M())
      h_deltam.Fill(PP1.M()-PP2.M())
      h_mggPP1pt.Fill(PP1.Pt())
      h_mggPP2pt.Fill(PP2.Pt())
      h_mggPP1pz.Fill(PP1.Pz())
      h_mggPP2pz.Fill(PP2.Pz())
    
     

      Pgggg = P1 + P2 + P3 + P4
      h_mgggg.Fill(Pgggg.M())

      for g in range(0,tree.v_genpho_p4.size()):

         if tree.v_genpho_p4.size() < 4:
            continue

         gen1 = TLorentzVector(0,0,0,0)
         gen2 = TLorentzVector(0,0,0,0)
         gen3 = TLorentzVector(0,0,0,0)
         gen4 = TLorentzVector(0,0,0,0)
         

#         print "hello ", tree.v_genpho_p4.size(), " ", evt
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
         
         diffgen_12_34 = abs(gen12.M() - gen34.M())
         diffgen_13_24 = abs(gen13.M() - gen24.M())
         diffgen_14_23 = abs(gen14.M() - gen23.M())

         genPP1 = ""
         genPP2 = ""

         
         if diffgen_12_34 < diffgen_13_24 and diffgen_12_34 < diffgen_14_23:
            genPP1 = gen12
            genPP2 = gen34
            h_gen_dr_a1.Fill(gen1.DeltaR(gen2))
            h_gen_dr_a2.Fill(gen3.DeltaR(gen4))
            h_gen_dphi_a1.Fill(gen1.DeltaPhi(gen2))
            h_gen_dphi_a2.Fill(gen3.DeltaPhi(gen4))
            h_gen_deta_a1.Fill(gen1.Eta()-gen2.Eta())
            h_gen_deta_a2.Fill(gen3.Eta()-gen4.Eta())
         
         if diffgen_13_24 < diffgen_12_34 and diffgen_13_24 < diffgen_14_23:
            genPP1 = gen13
            genPP2 = gen24
            h_gen_dr_a1.Fill(gen1.DeltaR(gen3))
            h_gen_dr_a2.Fill(gen2.DeltaR(gen4))
            h_gen_dphi_a1.Fill(gen1.DeltaPhi(gen3))
            h_gen_dphi_a2.Fill(gen2.DeltaPhi(gen4))
            h_gen_deta_a1.Fill(gen1.Eta()-gen3.Eta())
            h_gen_deta_a2.Fill(gen2.Eta()-gen4.Eta()) 
         
         if diffgen_14_23 < diffgen_12_34 and diffgen_14_23 < diffgen_13_24:
            genPP1 = gen14
            genPP2 = gen23
            h_gen_dr_a1.Fill(gen1.DeltaR(gen4))
            h_gen_dr_a2.Fill(gen2.DeltaR(gen3))
            h_gen_dphi_a1.Fill(gen1.DeltaPhi(gen4))
            h_gen_dphi_a2.Fill(gen2.DeltaPhi(gen3))
            h_gen_deta_a1.Fill(gen1.Eta()-gen4.Eta())
            h_gen_deta_a2.Fill(gen2.Eta()-gen3.Eta())
         
#         print "hello "
         if genPP1 == "":
            print "BLAH genPP1 is not assigned! ", diffgen_12_34, " ", diffgen_13_24, " ", diffgen_14_23, " ", tree.v_genpho_p4.size(), " ", evt
         if genPP2 == "":
            print "BLAH genPP2 is not assigned! ", diffgen_12_34, " ", diffgen_13_24, " ", diffgen_14_23, " ", tree.v_genpho_p4.size(), " ", evt


         h_gen_mindr.Fill(min(gen1.DeltaR(gen2), gen1.DeltaR(gen3), gen1.DeltaR(gen4), gen2.DeltaR(gen3), gen2.DeltaR(gen4), gen3.DeltaR(gen4)))
         h_gen_mggPP1.Fill(genPP1.M())
         h_gen_mggPP2.Fill(genPP2.M())
         h_gen_deltam.Fill(genPP1.M()-genPP2.M())
         h_gen_mggPP1pt.Fill(genPP1.Pt())
         h_gen_mggPP2pt.Fill(genPP2.Pt())
         h_gen_mggPP1pz.Fill(genPP1.Pz())
         h_gen_mggPP2pz.Fill(genPP2.Pz())

         genPgggg = gen1 + gen2 + gen3 + gen4
         h_gen_mgggg.Fill(genPgggg.M())
         

         h_gen1_pt.Fill(gen1.Pt())
         h_gen2_pt.Fill(gen2.Pt())
         h_gen3_pt.Fill(gen3.Pt())
         h_gen4_pt.Fill(gen4.Pt())
         h_gen1_eta.Fill(gen1.Eta())
         h_gen2_eta.Fill(gen2.Eta())
         h_gen3_eta.Fill(gen3.Eta())
         h_gen4_eta.Fill(gen4.Eta())
         h_gen1_phi.Fill(gen1.Phi())
         h_gen2_phi.Fill(gen2.Phi())
         h_gen3_phi.Fill(gen3.Phi())
         h_gen4_phi.Fill(gen4.Phi())


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
   h_gen_mggPP1.Write()
   h_gen_mggPP2.Write()
   h_gen_deltam.Write()
   h_dr.Write()
   h_dr_1.Write()
   h_dr_2.Write()
   h_drPdr1.Write()
   h_drPdr2.Write()
   h_dr_12.Write()
   h_dr_13.Write()
   h_dr_14.Write()
   h_dr_23.Write()
   h_dr_24.Write()
   h_dr_34.Write()
   h_n_pho_clean.Write()

   h_mindr.Write()
   gr.Write()
   h_mgg24_gen.Write()
   h_mgg13_gen.Write()
   h_mgg14_gen.Write()
   h_mgg23_gen.Write()
   h_mgg12_gen.Write()
   h_mgg34_gen.Write()
   h_mggPP2pt.Write()
   h_mggPP1pt.Write()
   h_mggPP1pz.Write()
   h_mggPP2pz.Write()
   h_gen_mggPP2pt.Write()
   h_gen_mggPP1pt.Write()
   h_gen_mggPP1pz.Write()
   h_gen_mggPP2pz.Write()
   h_p1_eta.Write()
   h_p2_eta.Write()
   h_p3_eta.Write()
   h_p4_eta.Write()
   h_gen1_eta.Write()
   h_gen2_eta.Write()
   h_gen3_eta.Write()
   h_gen4_eta.Write()
   h_deltam.Write()
   h_dr_a1.Write()
   h_dr_a2.Write()
   h_dphi_a1.Write()
   h_dphi_a2.Write()
   h_deta_a1.Write()
   h_deta_a2.Write()
   h_gen1_pt.Write()
   h_gen2_pt.Write()
   h_gen3_pt.Write()
   h_gen4_pt.Write()
   h_gen_dphi_a1.Write()
   h_gen_dphi_a2.Write()
   h_gen_deta_a1.Write()
   h_gen_deta_a2.Write()
   h_gen_dr_a1.Write()
   h_gen_dr_a2.Write()
   h_gen1_phi.Write()
   h_gen2_phi.Write()
   h_gen3_phi.Write()
   h_gen4_phi.Write()
   h_gen_mindr.Write()
   h_gen_mgggg.Write()
  
   
   gStyle.SetOptStat(0)
   c0 = TCanvas("c", "c", 800, 600)
   h_mggPP2.SetLineColor(4)
   h_mggPP2.GetYaxis().SetTitleOffset(1.5)
   h_mggPP2.SetLineWidth(2)
   h_mggPP2.Draw()
   h_mggPP1.SetLineColor(8)
   h_mggPP1.SetLineWidth(2)
   h_mggPP1.Draw("same")
   
   legend = TLegend(0.75,0.8,0.9,0.9)
   legend.AddEntry(h_mggPP2,"a2 mass","lp")
   legend.AddEntry(h_mggPP1,"a1 mass","lp")
   legend.Draw()
   c0.SetLogy()
   c0.SaveAs("a1a2mass.png")
  
   gStyle.SetOptStat(0)
   c1 = TCanvas("c", "c", 800, 600)
   h_mggPP2pt.SetLineColor(4)
   h_mggPP2pt.GetYaxis().SetTitleOffset(1.5)
   h_mggPP2pt.SetLineWidth(2)
   h_mggPP2pt.SetMaximum(1600)
   h_mggPP2pt.Draw()
   h_mggPP1pt.SetLineColor(8)
   h_mggPP1pt.SetLineWidth(2)
   h_mggPP1pt.Draw("same")
   
   legend = TLegend(0.75,0.8,0.9,0.9)
   legend.AddEntry(h_mggPP2pt,"a2 p_{T}","lp")
   legend.AddEntry(h_mggPP1pt,"a1 p_{T}","lp")
   legend.Draw()
   
   c1.SaveAs("newa1a2pt.png")

   gStyle.SetOptStat(0)
   c2 = TCanvas("c", "c", 800, 600)
   h_dr_a2.SetLineColor(4)
   h_dr_a2.GetYaxis().SetTitleOffset(1.5)
   h_dr_a2.SetLineWidth(2)
   h_dr_a2.Draw()
   h_dr_a1.SetLineColor(8)
   h_dr_a1.SetLineWidth(2)
   h_dr_a1.Draw("same")
   
   legend = TLegend(0.75,0.8,0.9,0.9)
   legend.AddEntry(h_dr_a2,"a2 #Delta r","lp")
   legend.AddEntry(h_dr_a1,"a1 #Delta r","lp")
   legend.Draw()
   
   c2.SaveAs("a1a2dr.png")
   
   gStyle.SetOptStat(0)
   c3 = TCanvas("c", "c", 800, 600)
   h_p4_eta.SetLineColor(4)
   h_p4_eta.GetYaxis().SetTitleOffset(1.5)
   h_p4_eta.SetMaximum(1000)
   h_p4_eta.SetLineWidth(2)
   h_p4_eta.Draw()
   h_p3_eta.SetLineColor(8)
   h_p3_eta.SetLineWidth(2)
   h_p3_eta.Draw("same")
   h_p2_eta.SetLineColor(6)
   h_p2_eta.SetLineWidth(2)
   h_p2_eta.Draw("same")
   h_p1_eta.SetLineColor(1)
   h_p1_eta.SetLineWidth(2)
   h_p1_eta.Draw("same")
   
   legend = TLegend(0.75,0.8,0.9,0.9)
   legend.AddEntry(h_p4_eta,"#gamma 4","lp")
   legend.AddEntry(h_p3_eta,"#gamma 3","lp")
   legend.AddEntry(h_p2_eta,"#gamma 2","lp")
   legend.AddEntry(h_p1_eta,"#gamma 1","lp")
   legend.Draw()
   
   c3.SaveAs("combinedeta.png")

   
   gStyle.SetOptStat(0)
   c4 = TCanvas("c", "c", 800, 600)
   h_p4_pt.SetLineColor(4)
   h_p4_pt.GetYaxis().SetTitleOffset(1.5)
   h_p4_pt.SetLineWidth(2)
   h_p4_pt.Draw()
   h_p3_pt.SetLineColor(8)
   h_p3_pt.SetLineWidth(2)
   h_p3_pt.Draw("same")
   h_p2_pt.SetLineColor(6)
   h_p2_pt.SetLineWidth(2)
   h_p2_pt.Draw("same")
   h_p1_pt.SetLineColor(1)
   h_p1_pt.SetLineWidth(2)
   h_p1_pt.Draw("same")
   
   legend = TLegend(0.75,0.8,0.9,0.9)
   legend.AddEntry(h_p4_pt,"#gamma 4","lp")
   legend.AddEntry(h_p3_pt,"#gamma 3","lp")
   legend.AddEntry(h_p2_pt,"#gamma 2","lp")
   legend.AddEntry(h_p1_pt,"#gamma 1","lp")
   legend.Draw()
   
   c4.SaveAs("combinedpt.png")
   

   gStyle.SetOptStat(0)
   c5 = TCanvas("c", "c", 800, 600)
   h_dphi_a2.SetLineColor(4)
   h_dphi_a2.GetYaxis().SetTitleOffset(1.5)
   h_dphi_a2.SetLineWidth(2)
   h_dphi_a2.Draw()
   h_dphi_a1.SetLineColor(8)
   h_dphi_a1.SetLineWidth(2)
   h_dphi_a1.Draw("same")
   
   legend = TLegend(0.85,0.8,0.7,0.9)
   legend.AddEntry(h_dphi_a2,"a2 #Delta #phi","lp")
   legend.AddEntry(h_dphi_a1,"a1 #Delta #phi","lp")
   legend.Draw()
   
   c5.SaveAs("deltaphi.png")
   
   gStyle.SetOptStat()
   c6 = TCanvas("c", "c", 800, 600)
   h_mgggg.SetLineColor(4)
   h_mgggg.GetYaxis().SetTitleOffset(1.5)
   h_mgggg.SetLineWidth(2)
   h_mgggg.Draw()
  
   c6.SetLogy()
   c6.SaveAs("newhiggsmass.png")
   
   gStyle.SetOptStat()
   c7 = TCanvas("c", "c", 800, 600)
   h_deltam.SetLineColor(4)
   h_deltam.GetYaxis().SetTitleOffset(1.5)
   h_deltam.SetLineWidth(2)
   h_deltam.Draw()
  
   c7.SetLogy()
   c7.SaveAs("a1a2massdiff.png")

   gStyle.SetOptStat()
   c8 = TCanvas("c", "c", 800, 600)
   h_mindr.SetLineColor(4)
   h_mindr.GetYaxis().SetTitleOffset(1.5)
   h_mindr.SetLineWidth(2)
   h_mindr.Draw()
  
   
   c8.SaveAs("newmindr.png")

   gStyle.SetOptStat(0)
   c9 = TCanvas("c", "c", 800, 600)
   h_deta_a2.SetLineColor(4)
   h_deta_a2.GetYaxis().SetTitleOffset(1.5)
   h_deta_a2.SetLineWidth(2)
   h_deta_a2.SetMaximum(2700)
   h_deta_a2.Draw()
   h_deta_a1.SetLineColor(8)
   h_deta_a1.SetLineWidth(2)
   h_deta_a1.Draw("same")

   legend = TLegend(0.75,0.8,0.9,0.9)
   legend.AddEntry(h_deta_a2,"a2 #Delta #eta","lp")
   legend.AddEntry(h_deta_a1,"a1 #Delta #eta","lp")
   legend.Draw()
   
   c9.SaveAs("deltaeta.png")
  
   gStyle.SetOptStat(0)
   c10 = TCanvas("c", "c", 800, 600)
   h_gen4_pt.SetLineColor(4)
   h_gen4_pt.GetYaxis().SetTitleOffset(1.5)
   h_gen4_pt.SetLineWidth(2)
   h_gen4_pt.SetMaximum(5500)
   h_gen4_pt.Draw()
   h_gen3_pt.SetLineColor(8)
   h_gen3_pt.SetLineWidth(2)
   h_gen3_pt.Draw("same")
   h_gen2_pt.SetLineColor(6)
   h_gen2_pt.SetLineWidth(2)
   h_gen2_pt.Draw("same")
   h_gen1_pt.SetLineColor(1)
   h_gen1_pt.SetLineWidth(2)
   h_gen1_pt.Draw("same")
   
   legend = TLegend(0.75,0.8,0.9,0.9)
   legend.AddEntry(h_gen4_pt,"gen#gamma 4","lp")
   legend.AddEntry(h_gen3_pt,"gen#gamma 3","lp")
   legend.AddEntry(h_gen2_pt,"gen#gamma 2","lp")
   legend.AddEntry(h_gen1_pt,"gen#gamma 1","lp")
   legend.Draw()
   
   c10.SaveAs("combinedgenpt.png")

   gStyle.SetOptStat(0)
   c11 = TCanvas("c", "c", 800, 600)
   h_mggPP2pz.SetLineColor(4)
   h_mggPP2pz.GetYaxis().SetTitleOffset(1.5)
   h_mggPP2pz.SetLineWidth(2)
   h_mggPP2pz.Draw()
   h_mggPP1pz.SetLineColor(8)
   h_mggPP1pz.SetLineWidth(2)
   h_mggPP1pz.Draw("same")
   
   legend = TLegend(0.75,0.8,0.9,0.9)
   legend.AddEntry(h_mggPP2pz,"a2 p_{z}","lp")
   legend.AddEntry(h_mggPP1pz,"a1 p_{z}","lp")
   legend.Draw()

   c11.SaveAs("a1a2pz.png")   

   gStyle.SetOptStat(0)
   c12 = TCanvas("c", "c", 800, 600)
   h_gen4_eta.SetLineColor(4)
   h_gen4_eta.GetYaxis().SetTitleOffset(1.5)
   h_gen4_eta.SetLineWidth(2)
   h_gen4_eta.Draw()
   h_gen3_eta.SetLineColor(8)
   h_gen3_eta.SetLineWidth(2)
   h_gen3_eta.Draw("same")
   h_gen2_eta.SetLineColor(6)
   h_gen2_eta.SetLineWidth(2)
   h_gen2_eta.Draw("same")
   h_gen1_eta.SetLineColor(1)
   h_gen1_eta.SetLineWidth(2)
   h_gen1_eta.Draw("same")
   
   legend = TLegend(0.75,0.8,0.9,0.9)
   legend.AddEntry(h_gen4_eta,"#gamma 4","lp")
   legend.AddEntry(h_gen3_eta,"#gamma 3","lp")
   legend.AddEntry(h_gen2_eta,"#gamma 2","lp")
   legend.AddEntry(h_gen1_eta,"#gamma 1","lp")
   legend.Draw()
   
   c12.SaveAs("gencombinedeta.png")


   gStyle.SetOptStat(0)
   c13 = TCanvas("c", "c", 800, 600)
   h_gen4_phi.SetLineColor(4)
   h_gen4_phi.GetYaxis().SetTitleOffset(1.5)
   h_gen4_phi.SetLineWidth(2)
   h_gen4_phi.SetMaximum(3000)
   h_gen4_phi.Draw()
   h_gen3_phi.SetLineColor(8)
   h_gen3_phi.SetLineWidth(2)
   h_gen3_phi.Draw("same")
   h_gen2_phi.SetLineColor(6)
   h_gen2_phi.SetLineWidth(2)
   h_gen2_phi.Draw("same")
   h_gen1_phi.SetLineColor(1)
   h_gen1_phi.SetLineWidth(2)
   h_gen1_phi.Draw("same")
   
   legend = TLegend(0.75,0.8,0.9,0.9)
   legend.AddEntry(h_gen4_phi,"#gamma 4","lp")
   legend.AddEntry(h_gen3_phi,"#gamma 3","lp")
   legend.AddEntry(h_gen2_phi,"#gamma 2","lp")
   legend.AddEntry(h_gen1_phi,"#gamma 1","lp")
   legend.Draw()
   
   c13.SaveAs("gencombinedphi.png")

   gStyle.SetOptStat(0)
   c14 = TCanvas("c", "c", 800, 600)
   h_gen_mggPP2.SetLineColor(4)
   h_gen_mggPP2.GetYaxis().SetTitleOffset(1.5)
   h_gen_mggPP2.SetLineWidth(2)
   h_gen_mggPP2.Draw()
   h_gen_mggPP1.SetLineColor(8)
   h_gen_mggPP1.SetLineWidth(2)
   h_gen_mggPP1.Draw("same")
   
   legend = TLegend(0.75,0.8,0.9,0.9)
   legend.AddEntry(h_gen_mggPP2,"a2 mass","lp")
   legend.AddEntry(h_gen_mggPP1,"a1 mass","lp")
   legend.Draw()
   c14.SetLogy()
   c14.SaveAs("gena1a2mass.png")
   

   gStyle.SetOptStat(0)
   c15 = TCanvas("c", "c", 800, 600)
   h_gen_dr_a2.SetLineColor(4)
   h_gen_dr_a2.GetYaxis().SetTitleOffset(1.5)
   h_gen_dr_a2.SetLineWidth(2)
   h_gen_dr_a2.Draw()
   h_gen_dr_a1.SetLineColor(8)
   h_gen_dr_a1.SetLineWidth(2)
   h_gen_dr_a1.Draw("same")
   
   legend = TLegend(0.75,0.8,0.9,0.9)
   legend.AddEntry(h_gen_dr_a2,"gen a2 #Delta r","lp")
   legend.AddEntry(h_gen_dr_a1,"gen a1 #Delta r","lp")
   legend.Draw()
   
   c15.SaveAs("gena1a2dr.png")

   gStyle.SetOptStat(0)
   c16 = TCanvas("c", "c", 800, 600)
   h_gen_dphi_a2.SetLineColor(4)
   h_gen_dphi_a2.GetYaxis().SetTitleOffset(1.5)
   h_gen_dphi_a2.SetLineWidth(2)
   h_gen_dphi_a2.SetMaximum(10000)
   h_gen_dphi_a2.Draw()
   h_gen_dphi_a1.SetLineColor(8)
   h_gen_dphi_a1.SetLineWidth(2)
   h_gen_dphi_a1.Draw("same")
   
   legend = TLegend(0.85,0.8,0.7,0.9)
   legend.AddEntry(h_gen_dphi_a2,"gen a2 #Delta #phi","lp")
   legend.AddEntry(h_gen_dphi_a1,"gen a1 #Delta #phi","lp")
   legend.Draw()
   
   c16.SaveAs("gendeltaphi.png")

   gStyle.SetOptStat(0)
   c17 = TCanvas("c", "c", 800, 600)
   h_gen_deta_a2.SetLineColor(4)
   h_gen_deta_a2.GetYaxis().SetTitleOffset(1.5)
   h_gen_deta_a2.SetLineWidth(2)
   h_gen_deta_a2.Draw()
   h_gen_deta_a1.SetLineColor(8)
   h_gen_deta_a1.SetLineWidth(2)
   h_gen_deta_a1.Draw("same")

   legend = TLegend(0.75,0.8,0.9,0.9)
   legend.AddEntry(h_gen_deta_a2,"gena2 #Delta #eta","lp")
   legend.AddEntry(h_gen_deta_a1,"gena1 #Delta #eta","lp")
   legend.Draw()
   
   c17.SaveAs("gendeltaeta.png")
   
   gStyle.SetOptStat()
   c18 = TCanvas("c", "c", 800, 600)
   h_gen_mindr.SetLineColor(4)
   h_gen_mindr.GetYaxis().SetTitleOffset(1.5)
   h_gen_mindr.SetLineWidth(2)
   h_gen_mindr.Draw()
  
   
   c18.SaveAs("gennewmindr.png")
   
   gStyle.SetOptStat(0)
   c19 = TCanvas("c", "c", 800, 600)
   h_gen_mggPP2pt.SetLineColor(4)
   h_gen_mggPP2pt.GetYaxis().SetTitleOffset(1.5)
   h_gen_mggPP2pt.SetLineWidth(2)
   h_gen_mggPP2pt.Draw()
   h_gen_mggPP1pt.SetLineColor(8)
   h_gen_mggPP1pt.SetLineWidth(2)
   h_gen_mggPP1pt.Draw("same")
   
   legend = TLegend(0.75,0.8,0.9,0.9)
   legend.AddEntry(h_gen_mggPP2pt,"gen a2 p_{T}","lp")
   legend.AddEntry(h_gen_mggPP1pt,"gen a1 p_{T}","lp")
   legend.Draw()
   
   c19.SaveAs("gennewa1a2pt.png")

   gStyle.SetOptStat(0)
   c20 = TCanvas("c", "c", 800, 600)
   h_gen_mggPP2pz.SetLineColor(4)
   h_gen_mggPP2pz.GetYaxis().SetTitleOffset(1.5)
   h_gen_mggPP2pz.SetLineWidth(2)
   h_gen_mggPP2pz.Draw()
   h_gen_mggPP1pz.SetLineColor(8)
   h_gen_mggPP1pz.SetLineWidth(2)
   h_gen_mggPP1pz.Draw("same")
   
   legend = TLegend(0.75,0.8,0.9,0.9)
   legend.AddEntry(h_gen_mggPP2pz,"gen a2 p_{z}","lp")
   legend.AddEntry(h_gen_mggPP1pz,"gen a1 p_{z}","lp")
   legend.Draw()

   c20.SaveAs("gena1a2pz.png")

   gStyle.SetOptStat()
   c21 = TCanvas("c","c",800,600)
   h_gen_mgggg.SetLineColor(4)
   h_gen_mgggg.GetYaxis().SetTitleOffset(1.5)
   h_gen_mgggg.SetLineWidth(2)
   h_gen_mgggg.Draw()
   c21.SetLogy()
   c21.SaveAs("gentetraphotonmass.png")

   gStyle.SetOptStat(0)
   c22 = TCanvas("c", "c", 800, 600)
   h_p4_phi.SetLineColor(4)
   h_p4_phi.GetYaxis().SetTitleOffset(1.5)
   h_p4_phi.SetLineWidth(2)
   h_p4_phi.SetMaximum(750)
   h_p4_phi.Draw()
   h_p3_phi.SetLineColor(8)
   h_p3_phi.SetLineWidth(2)
   h_p3_phi.Draw("same")
   h_p2_phi.SetLineColor(6)
   h_p2_phi.SetLineWidth(2)
   h_p2_phi.Draw("same")
   h_p1_phi.SetLineColor(1)
   h_p1_phi.SetLineWidth(2)
   h_p1_phi.Draw("same")
   
   legend = TLegend(0.85,0.8,0.9,0.9)
   legend.AddEntry(h_p4_phi,"#gamma 4","lp")
   legend.AddEntry(h_p3_phi,"#gamma 3","lp")
   legend.AddEntry(h_p2_phi,"#gamma 2","lp")
   legend.AddEntry(h_p1_phi,"#gamma 1","lp")
   legend.Draw()
   
   c22.SaveAs("combinedphi.png")
   
   gStyle.SetOptStat()
   c23 = TCanvas("c", "c", 800, 600)
   h_gen_deltam.SetLineColor(4)
   h_gen_deltam.GetYaxis().SetTitleOffset(1.5)
   h_gen_deltam.SetLineWidth(2)
   h_gen_deltam.Draw()
  
   c23.SetLogy()
   c23.SaveAs("gena1a2massdiff.png")
   
   
   
   

   outRoot.Close()
  # .! rootls -1 myfirstfile.root
	

if __name__ == "__main__":
   main(sys.argv[1:])


