#!/bin/bash

#for i in 100 101 102 103 105 106 107 108 109 111 112 113 114 115 116 117 124 126 127 129 130 132 133 135 136 141 149 14 150 151 152 153 158 15 161 162 163 166 167 16 174 175 177 179 17 180 181 183 184 185 186 187 18 190 196 197 198 199 19 31 37 38 39 3 40 41 42 43 49 50 51 52 53 54 55 58 59 5 61 62 64 65 66 67 70 71 72 73 74 76 80 81 82 83 84 85 86 87 8 91 92 93 94 95 96 98 99;

thispath=${PWD}
path=/tmp/rateixei/eos/cms/store/user/rateixei/H4G/FlatTrees/data/
cd $path
files=( *.root )
cd $thispath
for i in "${files[@]}"
do
	newfile=${i/.root/_SEL.root}
	echo $newfile
	python H4GTreeSkimmer.py -i $path/$i -o root/$newfile -p 4 -f 2
done

