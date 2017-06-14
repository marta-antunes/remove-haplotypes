#!/usr/bin/python2
# Converts haplotype file (filtered) to MAP file format for plink


def convert_snpslist_map_format(fileName):

	inputfile=open(fileName,"r") # haplotype file Ad locus x ind from stacks (withoutChcu haplotypes) 
	outputfile=open("snps_provis.map","w")

	j=0
	for line in inputfile:
	  if line.startswith("Cat"):
	    pass
	  else:
	    locus=line.split("\t")[0] # locus ID in catalog (tag)
	    scaffold=line.split("\t")[2] # scaffold
	    BP_item=[]
	    haplotypes=line.strip("\n").split("\t")[4:]#haplotypes start in column 3
	    nbases=len(max(haplotypes,key=len))# get the maximum number of bases of the locus
	    try:
	      BP_list=line.split("\t")[3].split(",")
	      #print "lista_de_posicoes:",BP_list
	      for i in range(nbases):
		#print "BP_item:",BP_list[i]
		outputfile.write(str(scaffold)+" "+locus+"-"+str(i)+" "+"0"+" "+str(BP_list[i])+"\n")
	    except IndexError:
	      i=0
		  
	return "snps_provis.map"

#convert_snpslist_map_format("haplotypes_withoutChcu_filtered")

	   

#def convert_snpslist_map_format(fileName):
#
#	inputfile=open(fileName,"r") # haplotype file Ad locus x ind from stacks (withoutChcu haplotypes) 
#	outputfile=open("snps_provis.map","w")


#	for line in inputfile:
#	  if line.startswith("Cat"):
#	    pass
#	  else:
#	    locus=line.split("\t")[0] # locus ID in catalog (tag)
#	    scaffold=line.split("\t")[2] # scaffold
#	    BP=[line.split("\t")[3]]
#	    #BP=line.split("\t")[3]#bp
#	    #print "BP:",BP
#	    haplotypes=line.strip("\n").split("\t")[4:]#haplotypes start in column 3
#	    nbases=len(max(haplotypes,key=len))# get the maximum number of bases of the locus
#	   
#	    for i in range(nbases):
#                for e in BP:
#                    #print "E:", e
#                    outputfile.write(str(scaffold)+" "+locus+"-"+str(i)+" "+"0"+" "+e+"\n")
##	return "snps_provis.map"