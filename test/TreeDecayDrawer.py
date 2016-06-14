import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing ('analysis')

# add a list of strings for events to process
#options.register ('isMiniAod',
                  #True,
                  #VarParsing.multiplicity.singleton,
                  #VarParsing.varType.bool,
                  #"is miniAod? (default = False). It changes the collection names")
#options.register ('debug',
                  #False,
                  #VarParsing.multiplicity.singleton,
                  #VarParsing.varType.bool,
                  #"debug? (default = False).")



options.parseArguments()

process = cms.Process("TreePrinter")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root',' with the source file you want to use
    fileNames = cms.untracked.vstring (options.inputFiles),
)

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")

process.printTree = cms.EDAnalyzer("ParticleTreeDrawer",
       src = cms.InputTag("flashggPrunedGenParticles"),     # microAOD    
       #src = cms.InputTag("prunedGenParticles"),  # -> to run on miniAod
       #src = cms.InputTag("prunedGenParticles"),  # -> to run on AOD
       printP4 = cms.untracked.bool(False),
       printPtEtaPhi = cms.untracked.bool(False),
       printVertex = cms.untracked.bool(False),
       printStatus = cms.untracked.bool(True),
       printIndex = cms.untracked.bool(True),
       #status = cms.untracked.vint32( 3 )
     )

process.p = cms.Path(process.printTree)

