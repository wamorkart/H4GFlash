// -*- C++ -*-
//
// Package:    H4G/H4GFlash
// Class:      H4GFlash
// 
/**\class H4GFlash H4GFlash.cc H4G/H4GFlash/plugins/H4GFlash.cc
 Description: [one line class summary]
 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Rafael Teixeira De Lima
//         Created:  Sat, 26 Mar 2016 16:30:02 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

//my includes
#include <memory>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <utility>
#include <cmath>
#include "TTree.h"
#include "TFile.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/PatCandidates/interface/PackedGenParticle.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "DataFormats/EgammaCandidates/interface/Photon.h"
#include "DataFormats/PatCandidates/interface/Photon.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/Math/interface/deltaR.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

//FLASHgg files
#include "flashgg/DataFormats/interface/DiPhotonCandidate.h"
#include "flashgg/DataFormats/interface/SinglePhotonView.h"
#include "flashgg/DataFormats/interface/Photon.h"
#include "flashgg/DataFormats/interface/Jet.h"
#include "flashgg/Taggers/interface/GlobalVariablesDumper.h"


#ifdef _CINT_
#pragma link C++ class std::vector<std::map<std::string,float>>;
#pragma link C++ class std::vector<std::map<std::string,int>>;
//#pragma link C++ struct H4GFlash::H4GDiPhoton;
#endif

//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<> and also remove the line from
// constructor "usesResource("TFileService");"
// This will improve performance in multithreaded jobs.

class H4GFlash : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
   public:
      explicit H4GFlash(const edm::ParameterSet&);
      ~H4GFlash();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

      //Selector elements:
      typedef math::XYZTLorentzVector LorentzVector;
      edm::EDGetTokenT<edm::View<flashgg::DiPhotonCandidate> > diphotonsToken_;
      edm::EDGetTokenT<edm::View<pat::PackedGenParticle> > genPhotonsToken_;

//      struct H4GDiPhoton{
//	LorentzVector p4;
//	int p1;
//	int p2;
//      };

      //Out tree elements:
      TTree* outTree;
      int n_pho, run, lumi, evtnum;
      std::vector<LorentzVector> v_pho_p4;
      std::vector<LorentzVector> v_genpho_p4;
      std::vector<int> v_genpho_motherpdgid;
      std::vector<float> v_pho_pt;
      std::vector<float> v_pho_eta;
      std::vector<float> v_pho_phi;
      std::vector<float> v_pho_e;
      std::vector<std::vector<float>> v_pho_dr;
      std::vector<std::vector<float>> v_pho_dphi;
      std::vector<std::vector<float>> v_pho_deta;
      std::vector<std::map<std::string, int>> v_pho_cutid;
      std::vector<float> v_pho_mva;

   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      // ----------member data ---------------------------
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
H4GFlash::H4GFlash(const edm::ParameterSet& iConfig):
diphotonsToken_( consumes<edm::View<flashgg::DiPhotonCandidate> >( iConfig.getUntrackedParameter<edm::InputTag> ( "diphotons", edm::InputTag( "flashggDiPhotons" ) ) ) ),
genPhotonsToken_( consumes<edm::View<pat::PackedGenParticle> >( iConfig.getUntrackedParameter<edm::InputTag>( "genphotons", edm::InputTag( "prunedGenParticles" ) ) ) )
{
   //now do what ever initialization is needed
   usesResource("TFileService");
   edm::Service<TFileService> fs;
   outTree = fs->make<TTree> ("H4GTree", "Tree for h->4g analysis");
   outTree->Branch("run", &run, "run/I");
   outTree->Branch("lumi", &lumi, "lumi/I");
   outTree->Branch("evtnum", &evtnum, "evtnum/I");

   outTree->Branch("n_pho", &n_pho, "n_pho/I");
   outTree->Branch("v_pho_p4", &v_pho_p4);
   outTree->Branch("v_genpho_p4", &v_genpho_p4);
   outTree->Branch("v_genpho_motherpdgid", &v_genpho_motherpdgid);
   outTree->Branch("v_pho_pt", &v_pho_pt);
   outTree->Branch("v_pho_eta", &v_pho_eta);
   outTree->Branch("v_pho_phi", &v_pho_phi);
   outTree->Branch("v_pho_e", &v_pho_e);
   outTree->Branch("v_pho_dr", &v_pho_dr);
   outTree->Branch("v_pho_dphi", &v_pho_dphi);
   outTree->Branch("v_pho_deta", &v_pho_deta);
   outTree->Branch("v_pho_cutid", &v_pho_cutid);
   outTree->Branch("v_pho_mva", &v_pho_mva);

}


H4GFlash::~H4GFlash()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
H4GFlash::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

   run = iEvent.id().run();
   lumi = iEvent.id().luminosityBlock();
   evtnum = iEvent.id().event();

   edm::Handle<edm::View<flashgg::DiPhotonCandidate> > diphotons;
   iEvent.getByToken(diphotonsToken_, diphotons);
   Handle<edm::View<pat::PackedGenParticle> > genPhotons;
   iEvent.getByToken(genPhotonsToken_,genPhotons);

   //Initialize tree variables
   n_pho = 0;
   v_pho_p4.clear();
   v_genpho_p4.clear();
   v_pho_pt.clear();
   v_pho_eta.clear();
   v_pho_phi.clear();
   v_pho_e.clear();
   v_pho_dr.clear();
   v_pho_dphi.clear();
   v_pho_deta.clear();
   v_pho_cutid.clear();
   v_pho_mva.clear();

   std::vector<const flashgg::Photon*> phosTemp;

   // Loop over diphotons
   for (size_t i = 0; i < diphotons->size(); ++i){
     edm::Ptr<flashgg::DiPhotonCandidate> dipho = diphotons->ptrAt(i);

     const flashgg::Photon * pho1 = dipho->leadingPhoton();
     const flashgg::Photon * pho2 = dipho->subLeadingPhoton();

     // Kinematics
     if( pho1->pt() < 15 || pho2->pt() < 15) 
       continue;
     if( fabs(pho1->superCluster()->eta()) > 2.5 || fabs(pho2->superCluster()->eta()) > 2.5 )
       continue;

     if ( phosTemp.size() == 0 ){
	phosTemp.push_back(pho1);
	phosTemp.push_back(pho2);
	n_pho+=2;
	continue;
     } else {
       float minDR1 = 999, minDR2 = 999;
       for ( size_t p = 0; p < phosTemp.size(); p++){
	 float deltar1 = deltaR(phosTemp[p]->p4(), pho1->p4());
         if(deltar1 < minDR1) minDR1 = deltar1;

	 float deltar2 = deltaR(phosTemp[p]->p4(), pho2->p4());
	 if(deltar2 < minDR2) minDR2 = deltar2; 
       }

       if ( minDR1 > 0.0001){
	 n_pho++;
	 phosTemp.push_back(pho1);
       }

       if ( minDR2 > 0.0001){
	 n_pho++;
	 phosTemp.push_back(pho2);
       }
     }

   }

   for ( size_t i = 0; i < phosTemp.size(); ++i)
   {
     const flashgg::Photon * pho = phosTemp[i];

     //
     // Save photon kinematics
     //
     v_pho_pt.push_back( pho->pt() );
     v_pho_eta.push_back( pho->superCluster()->eta() );
     v_pho_phi.push_back( pho->superCluster()->phi() );
     v_pho_e.push_back( pho->energy() );
     math::PtEtaPhiELorentzVectorD tmpVec;
     tmpVec.SetPt( pho->pt() );
     tmpVec.SetEta( pho->superCluster()->eta() );
     tmpVec.SetPhi( pho->superCluster()->phi() );
     tmpVec.SetE( pho->energy() );
     LorentzVector thisPhoV4( tmpVec );
     v_pho_p4.push_back( thisPhoV4 );
     v_pho_mva.push_back( pho->userFloat("PhotonMVAEstimatorRun2Spring15NonTrig25nsV2p1Values") );
 
   }

   // Save delta r between selected photons
   for( size_t p = 0; p < v_pho_p4.size(); p++) {
      LorentzVector pho = v_pho_p4[p];
      std::vector<float> vecDR;
      std::vector<float> vecDPhi;
      std::vector<float> vecDEta;
      for ( size_t p2 = 0; p < v_pho_p4.size(); p++) {
         LorentzVector pho2 = v_pho_p4[p];
         float deltar = 0;
         float deltaphi = 0;
         float deltaeta = 0;
         if( p2 == p ) {
            deltar = -999;
            deltaphi = -999;
            deltaeta = -999;
         }
         if( p2 != p ) {
            deltar = deltaR(pho, pho2);
            deltaphi = deltaPhi(pho.phi(), pho2.phi());
            deltar = fabs(pho.eta() - pho2.eta());
         }
         vecDR.push_back(deltar);
         vecDPhi.push_back(deltaphi);
         vecDEta.push_back(deltaeta);
      }
      v_pho_dr.push_back(vecDR);
      v_pho_dphi.push_back(vecDPhi);
      v_pho_deta.push_back(vecDEta);
   }

   // Save prompt photon gen information
   for( size_t g = 0; g < genPhotons->size(); g++) {
      const auto gen = genPhotons->ptrAt(g);

      //Only save gen information of prompt+final state photons (this includes FSR/ISR)
      if( gen->isPromptFinalState() == 0 ) continue;

      //Only save photons
      if( gen->pdgId() != 22 ) continue;

      v_genpho_p4.push_back( gen->p4() );

//      int motherPDGID = -999;
//      if( gen->mother() ) motherPDGID = gen->mother()->pdgId();
//      v_genpho_motherpdgid.push_back(motherPDGID);

   }
   
   // Save the info
   outTree->Fill();

}


// ------------ method called once each job just before starting event loop  ------------
void 
H4GFlash::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
H4GFlash::endJob() 
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
H4GFlash::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(H4GFlash);
