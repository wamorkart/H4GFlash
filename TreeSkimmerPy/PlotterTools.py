from ROOT import *

## Cuts to selection
Cuts = 'tp_mass > 100 && tp_mass < 200'

## Plots output location
outputLoc = '/afs/cern.ch/user/r/rateixei/www/H4G/ComparePlots/'

##Variables to be plotted
#[ name of tree branch, name of pdf file, name of variable, number of bins, min bin, max bin]
Vars = []
Vars.append([ 'p1_pt', 'p1_pt', ';E_{T}(#gamma-1) [GeV];Events', 100, 25, 125])
Vars.append([ 'p2_pt', 'p2_pt', ';E_{T}(#gamma-2) [GeV];Events', 100, 10, 110])
Vars.append([ 'p3_pt', 'p3_pt', ';E_{T}(#gamma-3) [GeV];Events', 100, 10, 110])
Vars.append([ 'p4_pt', 'p4_pt', ';E_{T}(#gamma-4) [GeV];Events', 100, 10, 45])
Vars.append([ 'p1_eta', 'p1_eta', ';#eta(#gamma-1);Events', 100, -3, 3])
Vars.append([ 'p2_eta', 'p2_eta', ';#eta(#gamma-2);Events', 100, -3, 3])
Vars.append([ 'p3_eta', 'p3_eta', ';#eta(#gamma-3);Events', 100, -3, 3])
Vars.append([ 'p4_eta', 'p4_eta', ';#eta(#gamma-4);Events', 100, -3, 3])
Vars.append([ 'tp_mass', 'tp_mass', ';M(#gamma#gamma#gamma#gamma) [GeV];Events', 100, 100, 200])
Vars.append([ 'dp1_mass', 'dp1_mass', ';M(#gamma#gamma-1) [GeV];Events', 100, 0, 200])
Vars.append([ 'dp2_mass', 'dp2_mass', ';M(#gamma#gamma-2) [GeV];Events', 100, 0, 200])

##Files to be plotted
#[ file name, legend, line color, fill color, normalization]
Files = []
Files.append(['/afs/cern.ch/work/r/rateixei/work/NEU_H4G/Flashgg/Aug24/CMSSW_8_0_8_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/root/DiPhoJets.root', 'DiPhoton+Jets (jj#gamma#gamma)', 33, 33, 1])
Files.append(['/afs/cern.ch/work/r/rateixei/work/NEU_H4G/Flashgg/Aug24/CMSSW_8_0_8_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/root/signal_m_10.root', 'm(A) = 10 GeV', kRed, 0, 1])
Files.append(['/afs/cern.ch/work/r/rateixei/work/NEU_H4G/Flashgg/Aug24/CMSSW_8_0_8_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/root/signal_m_25.root', 'm(A) = 25 GeV', kBlue, 0, 1])
Files.append(['/afs/cern.ch/work/r/rateixei/work/NEU_H4G/Flashgg/Aug24/CMSSW_8_0_8_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/root/signal_m_45.root', 'm(A) = 45 GeV', kGreen+3, 0, 1])
Files.append(['/afs/cern.ch/work/r/rateixei/work/NEU_H4G/Flashgg/Aug24/CMSSW_8_0_8_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/root/signal_m_60.root', 'm(A) = 60 GeV', kOrange, 0, 1])
