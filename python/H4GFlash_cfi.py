import FWCore.ParameterSet.Config as cms

h4gflash = cms.EDAnalyzer('H4GFlash',

	diphotons = cms.untracked.InputTag("flashggDiPhotons"),
	genphotons = cms.untracked.InputTag("flashggGenPhotons"),
	myTriggers = cms.untracked.vstring("HLT_Photon36_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon22_AND_HE10_R9Id65_Eta2_Mass15",
					   "HLT_Photon42_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon25_AND_HE10_R9Id65_Eta2_Mass15",
					   "HLT_Diphoton"),
	triggerTag = cms.InputTag("TriggerResults", "", "HLT")
)
