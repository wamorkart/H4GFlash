import FWCore.ParameterSet.Config as cms
import flashgg.Taggers.flashggTags_cff as flashggTags

##### Arguments
#import flashgg.bbggTools.VarParsing as opts
#options = opts.VarParsing('analysis')
#------- Add extra option
#options.register('doSelection',
#					False,
#					opts.VarParsing.multiplicity.singleton,
#					opts.VarParsing.varType.bool,
#					'False: Make tree before selection; True: Make tree after selection')
#options.register('doDoubleCountingMitigation',
#					False,
#					opts.VarParsing.multiplicity.singleton,
#					opts.VarParsing.varType.bool,
#					'False: Do not remove double counted photons from QCD/GJet/DiPhotonJets; True: Remove double counted photons from QCD/GJet/DiPhotonJets')
#options.register('nPromptPhotons',
#					0,
#					opts.VarParsing.multiplicity.singleton,
#					opts.VarParsing.varType.int,
#					'Number of prompt photons to be selected - to use this, set doDoubleCountingMitigation=1')
#
#-------
#
#options.parseArguments()

#maxEvents = 5
#if options.maxEvents:
#        maxEvents = int(options.maxEvents)

#inputFile = "/store/user/rateixei/flashgg/RunIISpring15-50ns/Spring15BetaV2/GluGluToRadionToHHTo2B2G_M-650_narrow_13TeV-madgraph/RunIISpring15-50ns-Spring15BetaV2-v0-RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/150804_164203/0000/myMicroAODOutputFile_1.root" #RadFiles['650']
#if options.inputFiles:
#        inputFile = options.inputFiles

#outputFile = "rest_rad700.root"
#if options.outputFile:
#        outputFile = options.outputFile
######
process = cms.Process("h4gflash")
process.load("flashgg.H4GFlash.H4GFlash_cfi")

process.h4gflash.rho = cms.InputTag('fixedGridRhoAll')
process.h4gflash.vertexes = cms.InputTag("offlineSlimmedPrimaryVertices")
process.h4gflash.puInfo=cms.InputTag("slimmedAddPileupInfo")

process.h4gflash.lumiWeight = cms.double(1.0)
process.h4gflash.intLumi = cms.double(1.0)
process.h4gflash.puReWeight=cms.bool(True)

process.h4gflash.puBins=cms.vdouble()
process.h4gflash.dataPu=cms.vdouble()
process.h4gflash.mcPu=cms.vdouble()

print "I'M HERE 1"

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring("test.root")
)

process.TFileService = cms.Service("TFileService",
      fileName = cms.string("out.root"),
      closeFileFast = cms.untracked.bool(True)
  )

process.load("FWCore.MessageService.MessageLogger_cfi")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32( 2000 )

# import flashgg customization
from flashgg.MetaData.JobConfig import customize
import FWCore.ParameterSet.VarParsing as VarParsing
# set default options if needed
customize.setDefault("maxEvents",-1)
customize.setDefault("targetLumi",2.58e+3)

customize.register('PURW',
				1,
				VarParsing.VarParsing.multiplicity.singleton,
				VarParsing.VarParsing.varType.bool,
				"Do PU reweighting? Doesn't work on 76X")


# call the customization
customize(process)

process.h4gflash.puReWeight=cms.bool( customize.PURW )
if customize.PURW == False:
	process.h4gflash.puTarget = cms.vdouble()
print "I'M HERE 2"

maxEvents = 5
if customize.maxEvents:
        maxEvents = int(customize.maxEvents)

if customize.inputFiles:
        inputFile = customize.inputFiles

if customize.outputFile:
        outputFile = customize.outputFile

#print customize.inputFiles, customize.outputFile, customize.maxEvents, customize.doSelection, customize.doDoubleCountingMitigation, customize.nPromptPhotons


#process.load("FWCore.MessageService.MessageLogger_cfi")

#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(maxEvents) )
#process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32( 2000 )

## Available mass points:
# RadFiles: 320, 340, 350, 400, 600, 650, 700
# GravFiles: 260, 270, 280, 320, 350, 500, 550
#NonResPhys14 = 'file:/afs/cern.ch/work/r/rateixei/work/DiHiggs/FLASHggPreSel/CMSSW_7_4_0_pre9/src/flashgg/MicroAOD/test/hhbbgg_hggVtx.root'

#process.source = cms.Source("PoolSource",
#    # replace 'myfile.root' with the source file you want to use
#    fileNames = cms.untracked.vstring(
#        customize.inputFiles
#    )
#)

print "I'M HERE 3"

#process.load("flashgg.bbggTools.bbggTree_cfi")
process.load("flashgg.Taggers.flashggTags_cff")
process.h4gflash.OutFileName = cms.untracked.string(outputFile)

#process.p = cms.Path(process.h4gflash)

process.p = cms.Path(flashggTags.flashggUnpackedJets*process.h4gflash)
