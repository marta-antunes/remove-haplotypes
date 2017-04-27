#!/usr/bin/python2
# 


def get_map(fileName):
	inputfile=open(fileName,"r")
	outfile=open("snps_doubled.map","w")

	for line in inputfile:
	  if line.startswith("#"):
	    pass
	  else:
	    locus=line.split(" ")[0] # locus ID in catalog (tag)
	    scaffold=line.split(" ")[1]
	    outfile.write(scaffold+" "+locus+" "+"0"+" "+"0"+"\n")
	return "snps_doubled.map"

	  
