Event mixing
====

Idea: mix odd and even events to create a blinded "real data" phase space, with no peak structure

    python H4GTreeMixing.py   --inputFile /afs/cern.ch/user/a/amassiro/public/H4G/signal_m_50.root     --outputFile    mytest.root
    
    python H4GTreeMixing.py   --inputFile /tmp/amassiro/eos/user/t/torimoto/4gamma/SkimmedTrees/Sep29/signal_m_10.root     --outputFile    mytest_10.root

    python H4GTreeMixing.py   --inputFile /tmp/amassiro/eos/user/t/torimoto/4gamma/SkimmedTrees/Oct6/signal_m_10.root     --outputFile    mytest_10.root
    python H4GTreeMixing.py   --inputFile /tmp/amassiro/eos/user/t/torimoto/4gamma/SkimmedTrees/Oct6/signal_m_15.root     --outputFile    mytest_15.root
    python H4GTreeMixing.py   --inputFile /tmp/amassiro/eos/user/t/torimoto/4gamma/SkimmedTrees/Oct6/signal_m_25.root     --outputFile    mytest_25.root
    python H4GTreeMixing.py   --inputFile /tmp/amassiro/eos/user/t/torimoto/4gamma/SkimmedTrees/Oct6/signal_m_60.root     --outputFile    mytest_60.root
    
    python H4GTreeMixing.py   --inputFile /tmp/amassiro/eos/user/t/torimoto/4gamma/SkimmedTrees/Oct6/ggjjControlRegion.root    --outputFile    /tmp/amassiro/controlregion.root
    
    
    
plot:
    
    r99t mytest_15.root mytest_25.root mytest_60.root 

    tree1 = (TTree*) _file0->Get("H4GSel")
    tree2 = (TTree*) _file1->Get("H4GSel")
    tree3 = (TTree*) _file2->Get("H4GSel")
    
    tree1->Draw("tp_mass >> h1(100,0,400)",  "p1_pt > 30  &&   p2_pt > 20  &&  dphigh_mass > 55");
    tree2->Draw("tp_mass >> h2(100,0,400)",  "p1_pt > 30  &&   p2_pt > 20  &&  dphigh_mass > 55");
    tree3->Draw("tp_mass >> h3(100,0,400)",  "p1_pt > 30  &&   p2_pt > 20  &&  dphigh_mass > 55");
    
    h1->SetLineColor(kBlue)
    h2->SetLineColor(kGreen+3)
    h3->SetLineColor(kPink)
    
    
    h1->SetLineWidth(2)
    h2->SetLineWidth(2)
    h3->SetLineWidth(2)
    
    h1->Scale(1./h1->Integral())
    h2->Scale(1./h2->Integral())
    h3->Scale(1./h3->Integral())
    
    h1->Draw()
    h2->Draw("same")
    h3->Draw("same")
    
    h1->SetTitle("15 GeV")
    h2->SetTitle("25 GeV")
    h3->SetTitle("60 GeV")
    
    gPad->BuildLegend()
    
    
    
    
    
    r99t  /tmp/amassiro/controlregion.root  /tmp/amassiro/eos/user/t/torimoto/4gamma/SkimmedTrees/Oct6/ggjjControlRegion.root
    
    
    tree1 = (TTree*) _file0->Get("H4GSel")
    tree2 = (TTree*) _file1->Get("H4GSel")
    
    tree1->Draw("tp_mass >> h1(100,0,700)",  "p1_pt > 30  &&   p2_pt > 20");
    tree2->Draw("tp_mass >> h2(100,0,700)",  "p1_pt > 30  &&   p2_pt > 20");
    
    h1->SetLineColor(kBlue)
    h2->SetLineColor(kPink)
        
    h1->SetLineWidth(2)
    h2->SetLineWidth(2)
    
    h1->Scale(1./h1->Integral())
    h2->Scale(1./h2->Integral())
    
    h2->Draw()
    h1->Draw("same")
    
    h1->SetTitle("mixed")
    h2->SetTitle("original")
    
    gPad->BuildLegend()


    
    
    
    
    r99t mytest_15.root  /tmp/amassiro/eos/user/t/torimoto/4gamma/SkimmedTrees/Oct6/signal_m_15.root
    
    
    tree1 = (TTree*) _file0->Get("H4GSel")
    tree2 = (TTree*) _file1->Get("H4GSel")
    
    tree1->Draw("tp_mass >> h1(100,0,400)",  "p1_pt > 30  &&   p2_pt > 20");
    tree2->Draw("tp_mass >> h2(100,0,400)",  "p1_pt > 30  &&   p2_pt > 20");
    
    h1->SetLineColor(kBlue)
    h2->SetLineColor(kPink)
        
    h1->SetLineWidth(2)
    h2->SetLineWidth(2)
    
    h1->Scale(1./h1->Integral())
    h2->Scale(1./h2->Integral())
    
    h2->Draw()
    h1->Draw("same")
    
    h1->SetTitle("mixed")
    h2->SetTitle("original")
    
    gPad->BuildLegend()


    
    
    
    
    
    
    
    r99t mytest_10.root  /tmp/amassiro/eos/user/t/torimoto/4gamma/SkimmedTrees/Oct6/signal_m_10.root
    
    
    tree1 = (TTree*) _file0->Get("H4GSel")
    tree2 = (TTree*) _file1->Get("H4GSel")
    
    tree1->Draw("dp1_mass >> h1(100,0,100)",  "p1_pt > 30  &&   p2_pt > 20");
    tree2->Draw("dp1_mass >> h2(100,0,100)",  "p1_pt > 30  &&   p2_pt > 20");
    
    h1->SetLineColor(kBlue)
    h2->SetLineColor(kPink)
        
    h1->SetLineWidth(2)
    h2->SetLineWidth(2)
    
    h1->Scale(1./h1->Integral())
    h2->Scale(1./h2->Integral())
    
    h1->Draw()
    h2->Draw("same")
    
    h1->SetTitle("mixed")
    h2->SetTitle("original")
    
    gPad->BuildLegend()
    
    
    
     r99t mytest_25.root  /tmp/amassiro/eos/user/t/torimoto/4gamma/SkimmedTrees/Oct6/signal_m_25.root
    
    
    tree1 = (TTree*) _file0->Get("H4GSel")
    tree2 = (TTree*) _file1->Get("H4GSel")
    
    tree1->Draw("dp1_mass >> h1(100,0,100)",  "p1_pt > 30  &&   p2_pt > 20");
    tree2->Draw("dp1_mass >> h2(100,0,100)",  "p1_pt > 30  &&   p2_pt > 20");
    
    h1->SetLineColor(kBlue)
    h2->SetLineColor(kPink)
        
    h1->SetLineWidth(2)
    h2->SetLineWidth(2)
    
    h1->Scale(1./h1->Integral())
    h2->Scale(1./h2->Integral())
    
    h2->Draw()
    h1->Draw("same")
    
    h1->SetTitle("mixed")
    h2->SetTitle("original")
    
    gPad->BuildLegend()
    
    
    
     
    
    
    r99t mytest_60.root  /tmp/amassiro/eos/user/t/torimoto/4gamma/SkimmedTrees/Oct6/signal_m_60.root
    
    
    tree1 = (TTree*) _file0->Get("H4GSel")
    tree2 = (TTree*) _file1->Get("H4GSel")
    
    tree1->Draw("dp1_mass >> h1(100,0,100)",  "p1_pt > 30  &&   p2_pt > 20");
    tree2->Draw("dp1_mass >> h2(100,0,100)",  "p1_pt > 30  &&   p2_pt > 20");
    
    h1->SetLineColor(kBlue)
    h2->SetLineColor(kPink)
        
    h1->SetLineWidth(2)
    h2->SetLineWidth(2)
    
    h1->Scale(1./h1->Integral())
    h2->Scale(1./h2->Integral())
    
    h1->Draw()
    h2->Draw("same")
    
    h1->SetTitle("mixed")
    h2->SetTitle("original")
    
    gPad->BuildLegend()
    
    
    
 