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

namespace H4GTools {

      typedef math::XYZTLorentzVector LorentzVector;

      struct H4G_DiPhoton{
        LorentzVector p4;
        int ip1;
        int ip2;
	float SumPt;
      };

      struct H4G_TetraPhoton{
        LorentzVector p4;
        int ip1;
        int ip2;
        int ip3;
        int ip4;
        int idp1;
        int idp2;
	float SumPt;
      };

}
