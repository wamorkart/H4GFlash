from ROOT import *
import numpy as n

DEBUG = 0

class SkimmedTreeTools:
   def __init__(self):
      self.p1_pt = n.zeros(1, dtype=float)
      self.p2_pt = n.zeros(1, dtype=float)
      self.p3_pt = n.zeros(1, dtype=float)
      self.p4_pt = n.zeros(1, dtype=float)
      self.p1_eta = n.zeros(1, dtype=float)
      self.p2_eta = n.zeros(1, dtype=float)
      self.p3_eta = n.zeros(1, dtype=float)
      self.p4_eta = n.zeros(1, dtype=float)
      self.p1_phi = n.zeros(1, dtype=float)
      self.p2_phi = n.zeros(1, dtype=float)
      self.p3_phi = n.zeros(1, dtype=float)
      self.p4_phi = n.zeros(1, dtype=float)
      self.p1_mva = n.zeros(1, dtype=float)
      self.p2_mva = n.zeros(1, dtype=float)
      self.p3_mva = n.zeros(1, dtype=float)
      self.p4_mva = n.zeros(1, dtype=float)
      self.p_mindr = n.zeros(1, dtype=float)
      self.dp1_pt = n.zeros(1, dtype=float)
      self.dp1_eta = n.zeros(1, dtype=float)
      self.dp1_phi = n.zeros(1, dtype=float)
      self.dp1_mass = n.zeros(1, dtype=float)
      self.dp1_p1i = n.zeros(1, dtype=float)
      self.dp1_p2i = n.zeros(1, dtype=float)
      self.dp2_pt = n.zeros(1, dtype=float)
      self.dp2_eta = n.zeros(1, dtype=float)
      self.dp2_phi = n.zeros(1, dtype=float)
      self.dp2_mass = n.zeros(1, dtype=float)
      self.dp2_p1i = n.zeros(1, dtype=float)
      self.dp2_p2i = n.zeros(1, dtype=float)
      self.dp1_dr = n.zeros(1, dtype=float)
      self.dp2_dr = n.zeros(1, dtype=float)
      self.tp_pt = n.zeros(1, dtype=float)
      self.tp_eta = n.zeros(1, dtype=float)
      self.tp_phi = n.zeros(1, dtype=float)
      self.tp_mass = n.zeros(1, dtype=float)
      self.dphigh_mass = n.zeros(1, dtype=float)
      self.initialEvents = n.zeros(1, dtype=float)
      self.evtnumber = n.zeros(1,dtype=int)
      self.runnumber = n.zeros(1,dtype=int)
      self.luminumber = n.zeros(1,dtype=int)
      self.nvtx = n.zeros(1,dtype=int)
      self.npu = n.zeros(1,dtype=float)

   def MakeSkimmedTree(self):
      outTree = TTree("H4GSel", "H4G Selected Events")
      SetOwnership(outTree,0)

      outTree.Branch('p1_pt', self.p1_pt, 'p1_pt/D')
      outTree.Branch('p2_pt', self.p2_pt, 'p2_pt/D')
      outTree.Branch('p3_pt', self.p3_pt, 'p3_pt/D')
      outTree.Branch('p4_pt', self.p4_pt, 'p4_pt/D')
      outTree.Branch('p1_eta', self.p1_eta, 'p1_eta/D')
      outTree.Branch('p2_eta', self.p2_eta, 'p2_eta/D')
      outTree.Branch('p3_eta', self.p3_eta, 'p3_eta/D')
      outTree.Branch('p4_eta', self.p4_eta, 'p4_eta/D')
      outTree.Branch('p1_phi', self.p1_phi, 'p1_phi/D')
      outTree.Branch('p2_phi', self.p2_phi, 'p2_phi/D')
      outTree.Branch('p3_phi', self.p3_phi, 'p3_phi/D')
      outTree.Branch('p4_phi', self.p4_phi, 'p4_phi/D')
      outTree.Branch('p1_mva', self.p1_mva, 'p1_mva/D')
      outTree.Branch('p2_mva', self.p2_mva, 'p2_mva/D')
      outTree.Branch('p3_mva', self.p3_mva, 'p3_mva/D')
      outTree.Branch('p4_mva', self.p4_mva, 'p4_mva/D')
      outTree.Branch('p_mindr', self.p_mindr, 'p_mindr/D')
      outTree.Branch('dp1_pt', self.dp1_pt, 'dp1_pt/D')
      outTree.Branch('dp1_eta', self.dp1_eta, 'dp1_eta/D')
      outTree.Branch('dp1_phi', self.dp1_phi, 'dp1_phi/D')
      outTree.Branch('dp1_mass', self.dp1_mass, 'dp1_mass/D')
      outTree.Branch('dp1_p1i', self.dp1_p1i, 'dp1_p1i/I')
      outTree.Branch('dp1_p2i', self.dp1_p2i, 'dp1_p2i/I')
      outTree.Branch('dp2_pt', self.dp2_pt, 'dp2_pt/D')
      outTree.Branch('dp2_eta', self.dp2_eta, 'dp2_eta/D')
      outTree.Branch('dp2_phi', self.dp2_phi, 'dp2_phi/D')
      outTree.Branch('dp2_mass', self.dp2_mass, 'dp2_mass/D')
      outTree.Branch('dp2_p1i', self.dp2_p1i, 'dp2_p1i/I')
      outTree.Branch('dp2_p2i', self.dp2_p2i, 'dp2_p2i/I')
      outTree.Branch('dp1_dr', self.dp1_dr, 'dp1_dr/D')
      outTree.Branch('dp2_dr', self.dp2_dr, 'dp2_dr/D')
      outTree.Branch('tp_pt', self.tp_pt, 'tp_pt/D')
      outTree.Branch('tp_eta', self.tp_eta, 'tp_eta/D')
      outTree.Branch('tp_phi', self.tp_phi, 'tp_phi/D')
      outTree.Branch('tp_mass', self.tp_mass, 'tp_mass/D')
      outTree.Branch('dphigh_mass', self.dphigh_mass, 'tphigh_mass/D')
      outTree.Branch('initialEvents', self.initialEvents, 'initialEvents/D')
      outTree.Branch('event', self.evtnumber, 'event/I')
      outTree.Branch('run', self.runnumber, 'run/I')
      outTree.Branch('lumi', self.luminumber, 'lumi/I')
      outTree.Branch('nvtx', self.nvtx, 'nvtx/I')
      outTree.Branch('npu', self.npu, 'npu/D')

      return outTree

   def MakePhotonSelection(self, Phos, Phos_id, MVA):
      sPhos = []
      sPhos_id = []
      for i,pho in enumerate(Phos):
         if pho.Pt() < 15: continue
         if abs(pho.Eta()) > 2.5: continue
         if abs(pho.Eta()) < 1.5 and MVA[Phos_id[i]] < 0.295: continue
         if abs(pho.Eta()) > 1.5 and MVA[Phos_id[i]] < 0.458: continue

         sPhos.append(pho)
         sPhos_id.append(Phos_id[i])

      return sPhos, sPhos_id

   def SelectWithFakes(self, Phos, Phos_id, MVA):
      fPhos = []
      fPhos_id = []
      for i,pho in enumerate(Phos):
         if pho.Pt() < 15: continue
         if abs(pho.Eta()) > 2.5: continue
         if abs(pho.Eta()) < 1.5 and MVA[Phos_id[i]] > 0.295: continue
         if abs(pho.Eta()) > 1.5 and MVA[Phos_id[i]] > 0.458: continue

         fPhos.append(pho)
         fPhos_id.append(Phos_id[i])

      return fPhos, fPhos_id

   def MakeTriggerSelection(self, Phos, Phos_id, R9, CHIso, HoE, PSeed):
      #based on trigger: HLT_Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55
      pho1 = 0
      pho1_id = -99
      pho2 = 0
      pho2_id = -99
      for i1,p1 in enumerate(Phos):
         if p1.Pt() < 30: continue
         if R9[Phos_id[i1]] < 0.8: continue
         if CHIso[Phos_id[i1]] > 20 and CHIso[Phos_id[i1]]/p1.Pt() > 0.3: continue
         if HoE[Phos_id[i1]] > 0.08: continue
         if PSeed[Phos_id[i1]] == 1: continue
         if abs(p1.Eta()) > 1.4442 and abs(p1.Eta()) < 1.566: continue

         for i2,p2 in enumerate(Phos):
            if(i2 <= i1): continue
            if p2.Pt() < 20: continue
            if R9[Phos_id[i2]] < 0.8: continue
            if CHIso[Phos_id[i2]] > 20 and CHIso[Phos_id[i2]]/p2.Pt() > 0.3: continue
            if HoE[Phos_id[i2]] > 0.08: continue
            if PSeed[Phos_id[i2]] == 1: continue
            if abs(p2.Eta()) > 1.4442 and abs(p2.Eta()) < 1.566: continue
            thisDipho = p1+p2
            if thisDipho.M() < 55: continue
            
            pho1 = p1
            pho1_id = Phos_id[i1]
            pho2 = p2
            pho2_id = Phos_id[i2]
            break
         if pho1 !=0 and pho2 != 0: break

      dipho = pho1+pho2
      if dipho == 0: return 0
      else: return [dipho, pho1, pho1_id, pho2, pho2_id]

   def MakePairing(self, Phos):
      minDM = 100000
      P1 = 0
      iP1 = -99
      P2 = 0
      iP2 = -99
      P3 = 0
      iP3 = -99
      P4 = 0
      iP4 = -99
      Dipho1 = 0
      Dipho2 = 0
      for i1,p1 in enumerate(Phos):
         for i2,p2 in enumerate(Phos):
            if i2 <= i1: continue
            for i3,p3 in enumerate(Phos):
               if i3 == i2 or i3 == i1: continue
               for i4,p4 in enumerate(Phos):
                  if i4 <= i3: continue
                  if i4==i1 or i4==i2: continue
                  dipho1 = p1+p2
                  dipho2 = p3+p4
                  deltaM = abs(dipho1.M() - dipho2.M())
                  if(DEBUG): print deltaM, i1, i2, i3, i4
                  if deltaM < minDM:
                     minDM = deltaM
                     P1 = p1
                     iP1 = i1
                     P2 = p2
                     iP2 = i2
                     P3 = p3
                     iP3 = i3
                     P4 = p4
                     iP4 = i4
                     Dipho1 = dipho1 if ((p1.Pt() + p2.Pt()) > (p3.Pt() + p4.Pt())) else dipho2
                     Dipho2 = dipho2 if ((p1.Pt() + p2.Pt()) > (p3.Pt() + p4.Pt())) else dipho1
      if(DEBUG): print 'minDr:', abs(Dipho1.M() - Dipho2.M()), iP1, iP2, iP3, iP4
      arr = [[Dipho1, P1, iP1, P2, iP2], [Dipho2, P3, iP3, P4, iP4]]
      return arr

