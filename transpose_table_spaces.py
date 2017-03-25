#!/usr/bin/python2
# transpose space delimited table



def transpose_table_spaces(inFileName,outFileName):

	inputfile=open(inFileName,"r") 
	outputfile=open(outFileName,"w")
	
	lines=(line.strip("\n").split(" ") for line in inputfile)
	for row in zip(*lines):
		outputfile.write(" ".join(row)+"\n")
	outputfile.close()
	out=outFileName
	return out





