import FWCore.ParameterSet.Config as cms

h4gflash = cms.EDAnalyzer('H4GFlash',

	diphotons = cms.untracked.InputTag("flashggDiPhotons"),
	genphotons = cms.untracked.InputTag("flashggGenPhotons")
)
