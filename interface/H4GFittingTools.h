#ifndef H4GFittingTools_h
#define H4GFittingTools_h

class RooWorkspace;
class RooArgList;
class RooDataSet;
class RooFitResult;

namespace H4GFittingTools {

    struct FitRes {
        std::string function;
        float kolmogorov;
        float chi2;
        float minNLL;
        RooFitResult* result;
    };
    
//    std::vector<H4GFittingTools::FitRes> FitFunctions(RooWorkspace* w, std::vector<std::string> functionsToFit, RooDataSet* data, RooArgList* mypdfs, std::string sVar, TH1F* dataHist);
//    std::vector<H4GFittingTools::FitRes> FitFunctions(RooWorkspace* w, std::vector<std::string> functionsToFit, RooDataSet* data, std::string sVar, TH1F* dataHist);
    std::vector<H4GFittingTools::FitRes> FitFunctions(RooWorkspace* w, std::vector<std::string> functionsToFit, RooDataSet* data, int isSignal = 0);
    void PlotCurves(std::string plotTitle, RooWorkspace* w, std::vector<std::string> functionsToFit, std::vector<std::string> legends,
			 std::vector<H4GFittingTools::FitRes> fitResults,
			RooDataSet* data, std::string sVar, std::string nbins, std::string plotName, int error, int isBkg = 0, float totNorm = -1);
};

#endif
