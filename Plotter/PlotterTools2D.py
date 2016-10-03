from ROOT import *

## Cuts to selection
#Cuts = 'dp1_mass < 63 && dp2_mass < 63'
Cuts = ''
## Plots output location
outputLoc = '/afs/cern.ch/user/r/rateixei/www/H4G/ComparePlots/'

##Variables to be plotted
#[ name of tree branch, name of pdf file, name of variable, number of bins, min bin, max bin]
Vars = []
Vars.append([ 'p2_pt:p1_pt', 'p1_pt_p2_pt', ';E_{T}(#gamma-1) [GeV];E_{T}(#gamma-2) [GeV];', 100, 0, 200, 100, 0, 200])
Vars.append([ 'dp1_mass:tp_mass', 'tp_mass_dp1_mass', ';M(#gamma#gamma#gamma#gamma) [GeV];M(#gamma#gamma-1) [GeV]', 100, 100, 180, 100, 0, 80])
Vars.append([ '(dp1_pt/tp_mass):tp_mass', 'tp_mass_dp1_massOvertp_mass', ';M(#gamma#gamma#gamma#gamma) [GeV];E_{T}(#gamma#gamma-1)/M(#gamma#gamma#gamma#gamma) [GeV]', 100, 100, 180, 100, 0, 2])
Vars.append([ 'dp2_mass:tp_mass', 'tp_mass_dp2_mass', ';M(#gamma#gamma#gamma#gamma) [GeV];M(#gamma#gamma-2) [GeV]', 100, 100, 180,100, 0, 80])
Vars.append([ 'dp2_mass:dp1_mass', 'dp1_mass_dp2_mass', ';M(#gamma#gamma-1) [GeV];M(#gamma#gamma-2) [GeV]', 100, 0, 150, 100, 0, 150])
Vars.append([ 'dp1_pt:tp_mass', 'tp_mass_dp1_pt', ';M(#gamma#gamma#gamma#gamma) [GeV];E_{T}(#gamma#gamma-1) [GeV]', 100, 100, 180,100, 10, 200])
Vars.append([ 'dp2_pt:tp_mass', 'tp_mass_dp2_pt', ';M(#gamma#gamma#gamma#gamma) [GeV];E_{T}(#gamma#gamma-2) [GeV]', 100, 100, 180,100, 10, 200])

##Files to be plotted
#[ file name, legend, line color, fill color, normalization]
Files = []
Files.append(['/afs/cern.ch/work/r/rateixei/work/NEU_H4G/Flashgg/Aug24/CMSSW_8_0_8_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/root/Hadd/All2016.root', 'Data (jj#gamma#gamma)', 33, 33, 1])
Files.append(['/afs/cern.ch/work/r/rateixei/work/NEU_H4G/Flashgg/Aug24/CMSSW_8_0_8_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/root/signal_m_10.root', 'm(A) = 10 GeV', kRed, 0, 1])
Files.append(['/afs/cern.ch/work/r/rateixei/work/NEU_H4G/Flashgg/Aug24/CMSSW_8_0_8_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/root/signal_m_25.root', 'm(A) = 25 GeV', kBlue, 0, 1])
Files.append(['/afs/cern.ch/work/r/rateixei/work/NEU_H4G/Flashgg/Aug24/CMSSW_8_0_8_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/root/signal_m_45.root', 'm(A) = 45 GeV', kGreen+3, 0, 1])
Files.append(['/afs/cern.ch/work/r/rateixei/work/NEU_H4G/Flashgg/Aug24/CMSSW_8_0_8_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/root/signal_m_60.root', 'm(A) = 60 GeV', kOrange, 0, 1])
