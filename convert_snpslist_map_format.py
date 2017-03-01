#!/usr/bin/python2
# Converts haplotype file (filtered) to MAP file format for plink


def convert_snpslist_map_format(fileName):

	inputfile=open(fileName,"r") # haplotype file Ad locus x ind from stacks (withoutChcu haplotypes) 
	outputfile=open("snps_provis.map","w")


	for line in inputfile:
	  if line.startswith("Cat"):
	    pass
	  else:
	    locus=line.split("\t")[0] # locus ID in catalog (tag)
	    haplotypes=line.strip("\n").split("\t")[2:]
	    nbases=len(max(haplotypes,key=len))# get the maximum number of bases of the locus
	   
	    for i in range(nbases):
	      outputfile.write("1"+" "+locus+"-"+str(i)+" "+"0"+" "+"0"+"\n")
	return "snps_provis.map"



	   
