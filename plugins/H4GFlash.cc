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
#include "TLorentzVector.h"
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
#include "flashgg/H4GFlash/interface/H4GTools.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

//FLASHgg files
#include "flashgg/DataFormats/interface/DiPhotonCandidate.h"
#include "flashgg/DataFormats/interface/SinglePhotonView.h"
#include "flashgg/DataFormats/interface/Photon.h"
#include "flashgg/DataFormats/interface/Jet.h"
#include "flashgg/Taggers/interface/GlobalVariablesDumper.h"

bool DEBUG = 0;

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
      edm::EDGetTokenT<edm::TriggerResults> triggerToken_;
      long int counter;

      //Out tree elements:
      TTree* outTree;
      int n_pho, run, lumi, evtnum, passTrigger;
      std::vector<H4GTools::H4G_DiPhoton> v_h4g_diphos;
      std::vector<H4GTools::H4G_TetraPhoton> v_h4g_tetraphos;
      std::vector<LorentzVector> v_pho_p4;
      std::vector<LorentzVector> v_genpho_p4;
      std::vector<int> v_genpho_motherpdgid;
      std::vector<float> v_pho_pt;
      std::vector<float> v_pho_eta;
      std::vector<float> v_pho_phi;
      std::vector<float> v_pho_e;
      
      //---- Inputs defined here:
      //     http://cmslxr.fnal.gov/lxr/source/DataFormats/PatCandidates/interface/Photon.h
      //     http://cmslxr.fnal.gov/lxr/source/DataFormats/PatCandidates/src/Photon.cc
      // photon ids and cluster variables
      std::vector<float> v_pho_hadronicOverEm;  
      std::vector<float> v_pho_chargedHadronIso; 
      std::vector<float> v_pho_neutralHadronIso; 
      std::vector<float> v_pho_photonIso; 
      std::vector<float> v_pho_passElectronVeto; 
      std::vector<float> v_pho_hasPixelSeed; 
      std::vector<float> v_pho_ecalPFClusterIso; 
      std::vector<float> v_pho_hcalPFClusterIso; 
      std::vector<float> v_pho_eMax; 
      std::vector<float> v_pho_e3x3; 
      std::vector<float> v_pho_subClusRawE1; 
      std::vector<float> v_pho_subClusDPhi1; 
      std::vector<float> v_pho_subClusDEta1; 
      std::vector<float> v_pho_subClusRawE2; 
      std::vector<float> v_pho_subClusDPhi2; 
      std::vector<float> v_pho_subClusDEta2; 
      std::vector<float> v_pho_subClusRawE3; 
      std::vector<float> v_pho_subClusDPhi3; 
      std::vector<float> v_pho_subClusDEta3; 
      std::vector<float> v_pho_iPhi; 
      std::vector<float> v_pho_iEta; 
            
      
      std::vector<std::vector<float>> v_pho_dr;
      std::vector<std::vector<float>> v_pho_dphi;
      std::vector<std::vector<float>> v_pho_deta;
      std::vector<std::map<std::string, int>> v_pho_cutid;
      std::vector<float> v_pho_mva;
      std::map<std::string, int> myTriggerResults;

      //Parameters
      std::vector<std::string> myTriggers;

      std::map<std::string, int> triggerStats;

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

   outTree->Branch("passTrigger", &passTrigger, "passTrigger/I");
   outTree->Branch("v_h4g_diphos", &v_h4g_diphos);
   outTree->Branch("v_h4g_tetraphos", &v_h4g_tetraphos);
   outTree->Branch("n_pho", &n_pho, "n_pho/I");
   outTree->Branch("v_pho_p4", &v_pho_p4);
   outTree->Branch("v_genpho_p4", &v_genpho_p4);
   outTree->Branch("v_genpho_motherpdgid", &v_genpho_motherpdgid);
   outTree->Branch("v_pho_pt", &v_pho_pt);
   outTree->Branch("v_pho_eta", &v_pho_eta);
   outTree->Branch("v_pho_phi", &v_pho_phi);
   outTree->Branch("v_pho_e", &v_pho_e);
   
   outTree->Branch("v_pho_hadronicOverEm",   &v_pho_hadronicOverEm  );
   outTree->Branch("v_pho_chargedHadronIso", &v_pho_chargedHadronIso);
   outTree->Branch("v_pho_neutralHadronIso", &v_pho_neutralHadronIso);
   outTree->Branch("v_pho_photonIso",        &v_pho_photonIso );
   outTree->Branch("v_pho_passElectronVeto", &v_pho_passElectronVeto);
   outTree->Branch("v_pho_hasPixelSeed",     &v_pho_hasPixelSeed );
   outTree->Branch("v_pho_ecalPFClusterIso", &v_pho_ecalPFClusterIso);
   outTree->Branch("v_pho_hcalPFClusterIso", &v_pho_hcalPFClusterIso);
   outTree->Branch("v_pho_eMax",             &v_pho_eMax );
   outTree->Branch("v_pho_e3x3",             &v_pho_e3x3 );
   outTree->Branch("v_pho_subClusRawE1",     &v_pho_subClusRawE1 );
   outTree->Branch("v_pho_subClusDPhi1",     &v_pho_subClusDPhi1 );
   outTree->Branch("v_pho_subClusDEta1",     &v_pho_subClusDEta1 );
   outTree->Branch("v_pho_subClusRawE2",     &v_pho_subClusRawE2 );
   outTree->Branch("v_pho_subClusDPhi2",     &v_pho_subClusDPhi2 );
   outTree->Branch("v_pho_subClusDEta2",     &v_pho_subClusDEta2 );
   outTree->Branch("v_pho_subClusRawE3",     &v_pho_subClusRawE3 );
   outTree->Branch("v_pho_subClusDPhi3",     &v_pho_subClusDPhi3 );
   outTree->Branch("v_pho_subClusDEta3",     &v_pho_subClusDEta3 );
   outTree->Branch("v_pho_iPhi",             &v_pho_iPhi );
   outTree->Branch("v_pho_iEta",             &v_pho_iEta );
    
   outTree->Branch("v_pho_dr", &v_pho_dr);
   outTree->Branch("v_pho_dphi", &v_pho_dphi);
   outTree->Branch("v_pho_deta", &v_pho_deta);
   outTree->Branch("v_pho_cutid", &v_pho_cutid);
   outTree->Branch("v_pho_mva", &v_pho_mva);
   outTree->Branch("myTriggerResults", &myTriggerResults);

   counter = 0;

   //Get parameters
   std::vector<std::string> def_myTriggers;
   triggerToken_ = consumes<edm::TriggerResults>( iConfig.getParameter<edm::InputTag>( "triggerTag" ) );
   myTriggers = iConfig.getUntrackedParameter<std::vector<std::string> >("myTriggers", def_myTriggers);
   std::cout << "Analyzing events with the following triggers:" << std::endl;
   for ( size_t i = 0; i < myTriggers.size(); i++)
      std::cout << "\t" << myTriggers[i] << std::endl;
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

   if(counter%1000 == 0) std::cout << "[H4GFlash::analyzer] Analyzing event #" << counter << std::endl;
   counter++;

   using namespace edm;

   run = iEvent.id().run();
   lumi = iEvent.id().luminosityBlock();
   evtnum = iEvent.id().event();

   edm::Handle<edm::View<flashgg::DiPhotonCandidate> > diphotons;
   iEvent.getByToken(diphotonsToken_, diphotons);
   Handle<edm::View<pat::PackedGenParticle> > genPhotons;
   iEvent.getByToken(genPhotonsToken_,genPhotons);

    //Trigger
    myTriggerResults.clear();
    if(myTriggers.size() > 0){
        Handle<edm::TriggerResults> trigResults;
        iEvent.getByToken(triggerToken_, trigResults);
        const edm::TriggerNames &names = iEvent.triggerNames(*trigResults);
        myTriggerResults = H4GTools::TriggerSelection(myTriggers, names, trigResults);
    }

    int acceptedTriggers = 0;
    for(std::map<std::string, int>::iterator it = myTriggerResults.begin(); it != myTriggerResults.end(); it++){
      if(DEBUG) std::cout << "Trigger name: " << it->first << "\n \t Decision: " << it->second << std::endl;
      if(it->second) acceptedTriggers++;
      std::map<std::string, int>::iterator finder;
      finder = triggerStats.find(it->first);
      if( finder != triggerStats.end() )
         triggerStats[it->first] += it->second;
      if( finder == triggerStats.end() )
	 triggerStats[it->first] =  it->second;
    }

    if(acceptedTriggers) passTrigger = 1;
    if(!acceptedTriggers) passTrigger = 0;

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
   v_h4g_diphos.clear();
   v_h4g_tetraphos.clear();
 
   v_pho_hadronicOverEm.clear();  
   v_pho_chargedHadronIso.clear(); 
   v_pho_neutralHadronIso.clear(); 
   v_pho_photonIso.clear(); 
   v_pho_passElectronVeto.clear(); 
   v_pho_hasPixelSeed.clear(); 
   v_pho_ecalPFClusterIso.clear(); 
   v_pho_hcalPFClusterIso.clear(); 
   v_pho_eMax.clear(); 
   v_pho_e3x3.clear(); 
   v_pho_subClusRawE1.clear(); 
   v_pho_subClusDPhi1.clear(); 
   v_pho_subClusDEta1.clear(); 
   v_pho_subClusRawE2.clear(); 
   v_pho_subClusDPhi2.clear(); 
   v_pho_subClusDEta2.clear(); 
   v_pho_subClusRawE3.clear(); 
   v_pho_subClusDPhi3.clear(); 
   v_pho_subClusDEta3.clear(); 
   v_pho_iPhi.clear(); 
   v_pho_iEta.clear(); 
   
   
   
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
 
     v_pho_hadronicOverEm.push_back    ( pho->hadronicOverEm() );  
     v_pho_chargedHadronIso.push_back  ( pho->chargedHadronIso() ); 
     v_pho_neutralHadronIso.push_back  ( pho->neutralHadronIso() ); 
     v_pho_photonIso.push_back         ( pho->photonIso() ); 
     v_pho_passElectronVeto.push_back  ( pho->passElectronVeto() ); 
     v_pho_hasPixelSeed.push_back      ( pho->hasPixelSeed() ); 
     v_pho_ecalPFClusterIso.push_back  ( pho->ecalPFClusterIso() ); 
     v_pho_hcalPFClusterIso.push_back  ( pho->hcalPFClusterIso() ); 
     v_pho_eMax.push_back              ( pho->eMax() ); 
     v_pho_e3x3.push_back              ( pho->e3x3() ); 
     v_pho_subClusRawE1.push_back      ( pho->subClusRawE1() ); 
     v_pho_subClusDPhi1.push_back      ( pho->subClusDPhi1() ); 
     v_pho_subClusDEta1.push_back      ( pho->subClusDEta1() ); 
     v_pho_subClusRawE2.push_back      ( pho->subClusRawE2() ); 
     v_pho_subClusDPhi2.push_back      ( pho->subClusDPhi2() ); 
     v_pho_subClusDEta2.push_back      ( pho->subClusDEta2() ); 
     v_pho_subClusRawE3.push_back      ( pho->subClusRawE3() ); 
     v_pho_subClusDPhi3.push_back      ( pho->subClusDPhi3() ); 
     v_pho_subClusDEta3.push_back      ( pho->subClusDEta3() ); 
     v_pho_iPhi.push_back              ( pho->iPhi() ); 
     v_pho_iEta.push_back              ( pho->iEta() ); 
     
     
   }

   // Save delta r between selected photons
   for( size_t p = 0; p < v_pho_p4.size(); p++) {
      LorentzVector pho = v_pho_p4[p];
      std::vector<float> vecDR;
      std::vector<float> vecDPhi;
      std::vector<float> vecDEta;
      for ( size_t p2 = 0; p2 < v_pho_p4.size(); p2++) {
         LorentzVector pho2 = v_pho_p4[p2];
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

	 if( p2 > p ){
            H4GTools::H4G_DiPhoton thisH4GDipho;
	    LorentzVector Sum = pho+pho2;
            thisH4GDipho.p4 = Sum;
            thisH4GDipho.ip1 = p;
            thisH4GDipho.ip2 = p2;
	    thisH4GDipho.SumPt = pho.pt() + pho2.pt();
            if( pho.pt() < pho2.pt()){   
               thisH4GDipho.ip1 = p2;
               thisH4GDipho.ip2 = p;
            }
	    v_h4g_diphos.push_back(thisH4GDipho);
         }
         vecDR.push_back(deltar);
         vecDPhi.push_back(deltaphi);
         vecDEta.push_back(deltaeta);

      }
      v_pho_dr.push_back(vecDR);
      v_pho_dphi.push_back(vecDPhi);
      v_pho_deta.push_back(vecDEta);
   }

   //Make tetraphotons
   for( size_t q1 = 0; q1 < v_h4g_diphos.size(); q1++) {
      H4GTools::H4G_DiPhoton Dipho1 = v_h4g_diphos[q1];
         for( size_t q2 = q1+1; q2 < v_h4g_diphos.size(); q2++) {
            H4GTools::H4G_DiPhoton Dipho2 = v_h4g_diphos[q2];
	    if ( Dipho1.ip1 == Dipho2.ip1
		 || Dipho1.ip1 == Dipho2.ip2
		 || Dipho1.ip2 == Dipho2.ip1
		 || Dipho1.ip2 == Dipho2.ip2 ) continue;

	    H4GTools::H4G_TetraPhoton thisTetra;
	    thisTetra.p4 = Dipho1.p4 + Dipho2.p4;
            thisTetra.idp1 = q1;
            thisTetra.idp2 = q2;
	    thisTetra.ip1 = Dipho1.ip1;
	    thisTetra.ip2 = Dipho1.ip2;
	    thisTetra.ip3 = Dipho2.ip1;
	    thisTetra.ip4 = Dipho2.ip2;
	    thisTetra.SumPt = Dipho1.SumPt + Dipho2.SumPt;
	    if( Dipho1.p4.pt() < Dipho2.p4.pt()) {
               thisTetra.idp1 = q2;
               thisTetra.idp2 = q1;
	       thisTetra.ip1 = Dipho2.ip1;
	       thisTetra.ip2 = Dipho2.ip2;
	       thisTetra.ip3 = Dipho1.ip1;
	       thisTetra.ip4 = Dipho1.ip2;
	    }

	    v_h4g_tetraphos.push_back(thisTetra);
         }

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

   std::cout << "============== Job stats ==============" << std::endl;
   std::cout << "\t Total number of events: " << counter << std::endl;
   std::cout << "\t Trigger stats: " << std::endl;
   for( std::map<std::string, int>::iterator it = triggerStats.begin(); it != triggerStats.end(); it++)
	std::cout << "\t  - " << it->first << " \t - Accepted events: " << it->second << std::endl;
   std::cout << "============== End stats ==============" << std::endl;

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
