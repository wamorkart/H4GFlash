from PlotterTools2D import *
from ROOT import *

gStyle.SetOptStat(0)
for v in Vars:
   hists = []
   leg = TLegend(0.6, 0.7, 0.89, 0.89)
   leg.SetBorderSize(0)
   Max = -0.
   for fi,f in enumerate(Files):
      ch = TChain('H4GSel')
      ch.Add(f[0])
      hname = v[1]+'_'+str(fi)
      h = TH2F(hname, v[2], v[3], v[4], v[5], v[6], v[7], v[8])
      ch.Draw(v[0]+'>>'+hname, TCut(Cuts))
      h.SetLineColor(f[2])
      h.SetFillColor(f[3])
      hists.append([h,ch,f[1]])
   c0 = TCanvas('a', 'a', 800, 600)
   for fi,hh in enumerate(hists):
      leg.AddEntry(hh[0], hh[2], 'lf')
      if fi == 0:
         print f
         hh[0].Draw('COLZ')
      if fi > 0:
         hh[0].Draw('CONT2 same')
   leg.Draw('same')
   c0.SaveAs(outputLoc+'2D_'+v[1]+'.pdf')
   c0.SaveAs(outputLoc+'2D_'+v[1]+'.png')
