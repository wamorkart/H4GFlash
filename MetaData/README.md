## How to use MetaData in Flashgg   
   
1) Create flashgg/MetaData/data/SigH4G_80X_v1   
2) Copy H4GFlash/MetaData/H4G_datasets.json to flashgg/MetaData/data/SigH4G_80X_v1/datasets.json   

```   
mkdir ${CMSSW_BASE}/src/flashgg/MetaData/data/SigH4G_80X_v1
cp ${CMSSW_BASE}/src/flashgg/H4GFlash/MetaData/H4G_datasets.json ${CMSSW_BASE}/src/flashgg/MetaData/data/SigH4G_80X_v1/datasets.json
```
   
3) Copy the content of H4GFlash/MetaData/cross_sections.txt to the beginning of ${CMSSW_BASE}/src/flashgg/MetaData/data/cross_sections.json   
   
Now you are ready to use FLASHgg fggRunJobs tools.
