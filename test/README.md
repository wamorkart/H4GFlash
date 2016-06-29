## Make Flat Trees
```
cmsRun MakeTrees.py inputFiles=/store/group/phys_higgs/cmshgg/ferriff/flashgg/RunIIFall15DR76-1_3_0-25ns_ext1/1_3_1/GluGluHToGG_M-125_13TeV_powheg_pythia8/RunIIFall15DR76-1_3_0-25ns_ext1-1_3_1-v0-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/160130_032602/0000/myMicroAODOutputFile_1.root PURW=0
```

    cd /afs/cern.ch/user/a/amassiro/work/Hgg/H4G/TestFlashGG/CMSSW_7_6_3_patch2/src/flashgg/H4GFlash/test/
    
    cmsRun MakeTrees.py inputFiles=/store/user/amassiro/H4G/microAOD/myMicroAODOutputFile_GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8.root    PURW=0   outputFile=mX_750GeV_mA_370GeV.root
    cmsRun MakeTrees.py inputFiles=/store/user/amassiro/H4G/microAOD/myMicroAODOutputFile_GluGluToXToAATo4G_mX_750GeV_mA_10GeV_Pythia8.root     PURW=0   outputFile=mX_750GeV_mA_10GeV.root

    cmsRun MakeTrees.py inputFiles=/store/user/amassiro/H4G/microAOD/FIX_2/myMicroAODOutputFile_GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8.root    PURW=0   outputFile=FIX_2_mX_750GeV_mA_370GeV.root
    cmsRun MakeTrees.py inputFiles=/store/user/amassiro/H4G/microAOD/FIX_2/myMicroAODOutputFile_GluGluToXToAATo4G_mX_750GeV_mA_10GeV_Pythia8.root     PURW=0   outputFile=FIX_2_mX_750GeV_mA_10GeV.root

    
    cd /afs/cern.ch/user/a/amassiro/work/Hgg/H4G/TestFlashGG/CMSSW_7_6_3_patch2/src/flashgg/H4GFlash/test/
    cmsenv
    cmsRun MakeTrees.py inputFiles=/store/user/amassiro/H4G/microAOD/FIX_3/myMicroAODOutputFile_GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8.root     PURW=0   outputFile=FIX_3_mX_750GeV_mA_370GeV.root

    
small test:

    r99t  output.root 
    TTree* H4GTree = (TTree*) _file0->Get("h4gflash/H4GTree");

    H4GTree->Draw("v_h4g_tetraphos.p4.M()");
    H4GTree->Draw("v_h4g_tetraphos.p4.M()","@v_h4g_tetraphos.size() == 3");
    H4GTree->Draw("v_h4g_tetraphos.p4.M()","@v_h4g_tetraphos.size() == 3 && v_h4g_tetraphos.p4.M() > 500 && v_h4g_tetraphos.p4.M() < 1000");
    H4GTree->Draw("v_h4g_tetraphos[0].p4.M()","@v_h4g_tetraphos.size() == 3 && v_h4g_tetraphos.p4.M() > 500 && v_h4g_tetraphos.p4.M() < 1000");
    
    H4GTree->Draw("v_h4g_diphos.p4.M()");
    H4GTree->Draw("v_h4g_diphos[0].p4.M()");
    H4GTree->Draw("v_h4g_diphos[0].p4.M()", "@v_h4g_tetraphos.size() == 3");
    
    H4GTree->Draw("v_h4g_diphos[0].p4.M()", "@v_h4g_tetraphos.size() == 3 && v_h4g_diphos[0].p4.M() > 100 && v_h4g_diphos[0].p4.M() < 500");
    H4GTree->Draw("v_h4g_diphos[1].p4.M()", "@v_h4g_tetraphos.size() == 3 && v_h4g_diphos[1].p4.M() > 100 && v_h4g_diphos[1].p4.M() < 500");
     
    H4GTree->Draw("v_h4g_diphos[v_h4g_tetraphos[0].ip1].p4.M()", "@v_h4g_tetraphos.size() == 3 && v_h4g_diphos[v_h4g_tetraphos[0].ip1].p4.M() > 100 && v_h4g_diphos[v_h4g_tetraphos[0].ip1].p4.M() < 500");
    H4GTree->Draw("v_h4g_diphos[v_h4g_tetraphos[0].ip2].p4.M()", "@v_h4g_tetraphos.size() == 3 && v_h4g_diphos[v_h4g_tetraphos[0].ip2].p4.M() > 100 && v_h4g_diphos[v_h4g_tetraphos[0].ip2].p4.M() < 500");
    H4GTree->Draw("v_h4g_diphos[v_h4g_tetraphos[0].ip1].p4.M():v_h4g_diphos[v_h4g_tetraphos[0].ip2].p4.M()", "@v_h4g_tetraphos.size() == 3 && v_h4g_diphos[v_h4g_tetraphos[0].ip1].p4.M() > 100 && v_h4g_diphos[v_h4g_tetraphos[0].ip1].p4.M() < 500", "colz");
     
     
    H4GTree->Draw("v_pho_chargedHadronIso");

    H4GTree->Draw("@v_genpho_p4.size()");

    
    H4GTree->Draw("v_gen_X_id");
    H4GTree->Draw("v_gen_X_mass");

    H4GTree->Draw("v_gen_a_mass");
    
    
## Run all jobs

#### 1) Only once: Create the campaign dataset in flashgg [for background samples that are default for Hgg analysis, skip this step!!]   
```
cd ${CMSSW_BASE}/src/flashgg/MetaData/data/
cmsenv
fggManageSamples.py -C <Campaign> -V <flashgg version> import #(1)
fggManageSamples.py -C <Campaign> -V <flashgg version> review #(2)
fggManageSamples.py -C <Campaign> -V <flashgg version> check #(3)
```   
- Campaign and flashgg version are the ones used during the MicroAOD production step    
- (1): Creates dataset entry (folder under MetaData/data/ with dataset.json with list of files)    
- (2): Check for duplicates, select datasets you want (or include all)    
- (3): Calculate weights, import number of events, etc    

#### 2) Only once: prepare json file with list of datasets to run on   
```
cd ${CMSSW_BASE}/src/flashgg/H4GFlash/test/RunJobs/
vim ToRun.json
```   
File should look like this:
```
{
    "processes" : {
        "GluGluToBulkGravitonToHHTo2B2G_M-1000_narrow_13TeV-madgraph" : [
            ["/GluGluToBulkGravitonToHHTo2B2G_M-1000_narrow_13TeV-madgraph", {"args" : ["campaign=<Campaign>","PURW=1", "OtherArgs..."]}]
        ],
        ...
    },
    "cmdLine" : "targetLumi=2.7e+3 puTarget=1.34e+05,6.34e+05,8.42e+05,1.23e+06,2.01e+06,4.24e+06,1.26e+07,4.88e+07,1.56e+08,3.07e+08,4.17e+08,4.48e+08,4.04e+08,3.05e+08,1.89e+08,9.64e+07,4.19e+07,1.71e+07,7.85e+06,4.2e+06,2.18e+06,9.43e+05,3.22e+05,8.9e+04,2.16e+04,5.43e+03,1.6e+03,551,206,80.1,31.2,11.9,4.38,1.54,0.518,0.165,0.0501,0.0144,0.00394,0.00102,0.000251,5.87e-05,1.3e-05,2.74e-06,5.47e-07,1.04e-07,1.86e-08,3.18e-09,5.16e-10,9.35e-11"
}
```   
- The "args" in each process is the list of individual args being passed to the cmsRun command    
- The list in "cmdLine" is passed for all processes   
- Remember to edit <Campaign> to match the campaign dataset you created on step (1)
- puTarget is the bin contents of your minBias PU distribution (target)   

#### 3) Run!
```
mkdir outDir
fggRunJobs.py --load ToRun.json -H -D -P -n 500 -d outDir -x cmsRun ../MakeTrees.py maxEvents=-1 -q 1nh --no-use-tarball
```   
This will submit all the jobs to lxbatch and start a monitoring task. After all jobs have been submitted, feel free to quit it if you want. However, leaving it running will also resubmit jobs that fail for lxbatch reasons. You can continue the monitoring task with:   
```
fggRunJobs.py --load outDir/configs.json --cont
```




Plot decay chain
----

    cmsRun TreeDecayDrawer.py   inputFiles=file:/tmp/amassiro/eos/cms/store/user/amassiro/H4G/microAOD/myMicroAODOutputFile_GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8.root 
    cmsRun TreeDecayDrawer.py   inputFiles=file:/tmp/amassiro/eos/cms/store/user/amassiro/H4G/microAOD/myMicroAODOutputFile_GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8.root \
                                maxEvents=1
        
    -- decay tree: --
    H0{status: 22} <idx: 0>
    +-> h0{status: 22} <idx: 1>
    |   +-> gamma{status: 1} <idx: 3> gamma{status: 1} <idx: 4>
    +-> h0{status: 22} <idx: 2>
        +-> gamma{status: 1} <idx: 5> gamma{status: 1} <idx: 6>
    
    
    
    cmsRun TreeDecayDrawer.py    inputFiles=file:/tmp/amassiro/eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris/160524_103125/0000/HIG-RunIIFall15MiniAODv2-00711_52.root        \
                                 maxEvents=1
        
        

        
        
        
