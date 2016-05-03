#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <utility>
#include "flashgg/H4GFlash/interface/H4GTools.h"

#ifdef _CINT_
#pragma link C++ class std::vector<std::map<std::string,float>>;
#pragma link C++ class std::vector<std::map<std::string,int>>;
#pragma link C++ class H4GTools::H4G_DiPhoton+;
#pragma link C++ class std::vector<H4GTools::H4G_DiPhoton>+;
#pragma link C++ class H4GTools::H4G_TetraPhoton+;
#pragma link C++ class std::vector<H4GTools::H4G_TetraPhoton>+;
#endif

namespace {
	struct dictionary {
		std::vector<std::map<std::string,float>> dummy_idvars;
		std::vector<std::map<std::string,int>> dummy_idbools;
		H4GTools::H4G_DiPhoton dummy_h4g_diphos;
		std::vector<H4GTools::H4G_DiPhoton> dummy_v_h4g_diphos;
		H4GTools::H4G_TetraPhoton dummy_h4g_tetraphos;
		std::vector<H4GTools::H4G_TetraPhoton> dummy_v_h4g_tetraphos;
	};
}
