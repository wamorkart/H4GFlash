from ROOT import *
from array import array

files = [
#"eff_1gev.root",
"eff_10gev.root",
"eff_15gev.root",
"eff_20gev.root",
"eff_25gev.root",
"eff_35gev.root",
"eff_40gev.root",
"eff_45gev.root",
"eff_50gev.root",
"eff_55gev.root",
"eff_60gev.root"
]

#masses = [1, 10, 15, 20, 25, 35, 40, 45, 50, 55, 60]
masses = [10, 15, 20, 25, 35, 40, 45, 50, 55, 60]

cuts = [
["cut0==1", [] ],
["cut1==1", [] ],
["cut2==1", [] ],
["cut3==1", [] ],
["cut4==1", [] ],
["cut5==1", [] ],
["cut6==1", [] ],
["cut7==1", [] ],
["cut8==1", [] ]
]

for i,m in enumerate(masses):
   for c in cuts:
      tch = TChain("H4GEff")
      tch.AddFile(files[i])
      totevs = tch.Draw("totevs", "1>0")
      thiscut = tch.Draw("totevs", c[0])
      thiseff = float(thiscut)/float(totevs)
      c[1].append(thiseff)


cols = [1, 2, 4, 6, kGreen+3, kOrange+2, 9, 30, 49]
styls = [24, 25, 26, 27, 28, 30, 32, 31, 33, 34]
cutNames = [">0#gamma", ">1#gamma", ">2#gamma", ">3#gamma", ">0#gamma-id", ">1#gamma-id", ">2#gamma-id", ">3#gamma-id", ">3#gamma-id + Trigger"]
c0 = TCanvas('a', 'a', 1000, 600)
c0.SetLogy()
c0.SetGrid()
leg = TLegend(0.72, 0.1012, 0.8992, 0.8985)
leg.SetHeader("Selection Steps")
#leg.SetFillStyle(0)
leg.SetBorderSize(0)
for i,c in enumerate(cuts):
   gr = TGraph(len(masses), array('d', masses), array('d', c[1]))
   c.append(gr)
   leg.AddEntry(c[2], cutNames[i], "lp")
   c[2].SetLineColor(cols[i])
   c[2].SetMarkerColor(cols[i])
   c[2].SetMarkerStyle(styls[i])
   c[2].SetMarkerSize(2)
   if( i == 0 ): 
      c[2].Draw("APL")
      c[2].SetMaximum(1.0)
      c[2].SetMinimum(0.01)
      c[2].GetXaxis().SetLimits(5, 80)
      c[2].GetYaxis().SetTitle("Selection Efficiencies")
      c[2].GetXaxis().SetTitle("Scalar Mass [GeV]")
      c[2].SetTitle()
      c0.Update()
   if( i > 0 ): c[2].Draw("PL")
leg.Draw()
c0.SaveAs("eff_mva2.pdf")
