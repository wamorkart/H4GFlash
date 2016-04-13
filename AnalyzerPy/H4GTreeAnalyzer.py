#!/usr/bin/python

from ROOT import *
import sys, getopt

def main(argv):
   inputfiles = ''
   outputfile = 'output.root'
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["inputFiles=","outputFile="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile1,inputfile2,inputfile3...> -o <outputfile>'
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

   #Tree Loop:
   for evt in range(0, tree.GetEntries()):
      if evt%1000 == 0: print "## Analyzing event ", evt
      tree.GetEntry(evt)

      print "Number of photons:", tree.n_pho
      if tree.n_pho < 1:
         continue


      for p in range(0, tree.n_pho):
        print "photon #", p, " pt:",tree.v_pho_pt[p]
        if p == 0:
           h_p1_pt.Fill(tree.v_pho_pt[p])
        if p == 1:
           h_p2_pt.Fill(tree.v_pho_pt[p])

   outRoot.cd()
   h_p1_pt.Write()
   h_p2_pt.Write()
   outRoot.Close()

	

if __name__ == "__main__":
   main(sys.argv[1:])

