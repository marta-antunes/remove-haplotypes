#!/usr/bin/python2
# transpose table tab delimited

def transpose_table_tabs(fileName):

	inputfile=open(fileName,"r")
	outfile=open("haplotype_withoutChcu_filtered_missingCoded_transposed","w")
	lines=(line.strip("\n").split("\t") for line in inputfile)
	for row in zip(*lines):
	    outfile.write("\t".join(row)+"\n")
	return "haplotype_withoutChcu_filtered_missingCoded_transposed"
