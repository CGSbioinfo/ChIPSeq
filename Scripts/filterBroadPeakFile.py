import sys
import os

broadFileName = sys.argv[1]
fileTab = broaFile.split(".")
outFile = fileTab[0]+"filtered.broadPeak"
broadFile = open(broadFileName)

for peaks in broadFile:
	peaks = peaks.strip()
	peaksTab = peaks.split("\t")
	if peaksTab[8]>3:
		outFile.write(peaks+"\n")
