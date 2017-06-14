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
	    BP=line.split(" ")[2] #because bp information is on 3rd column, index 2
	    outfile.write(scaffold+" "+locus+" "+"0"+" "+BP+"\n")
	return "snps_doubled.map"

	  
