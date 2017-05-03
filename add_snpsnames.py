#!/usr/bin/python2
# removes loci with more than 10% missing individuals


from sys import argv

def add_snpsnames(mapFileName,pedFileName):

	map_file=open(mapFileName,"r") # MAP snp file
	outputfile=open("snps_withnames.ped","w")


	snps=[]
	for line in map_file: #iterates over map file
	  snps.append(line.split(" ")[1]) #column 2 index 1 contain snps info
	map_file.close()
	
	scaffolds=[]
	mapp_file=open(mapFileName,"r")
	for l in mapp_file: #iterates over map file
	  scaffolds.append(l.split(" ")[0]) #column 1 index 0 contain scaffolds info
	  #print "AQUII",scaffolds
	#print "AQUI",scaffolds
	mapp_file.close()
	
	outputfile.write("#FAMID"+" "+"#IND"+" "+"#PATID"+" "+"#MATID"+" "+"#SEX"+" "+"#PHENO"+" "+" ".join((str(i)+" "+str(i)) for i in snps)+"\n"+"0"+" "+"0"+" "+"0"+" "+"0"+" "+"0"+" "+"0"+" "+" ".join((str(j)+" "+str(j)) for j in scaffolds)+"\n")  #PED format (plink) 
	  
	ped_file=open(pedFileName,"r") # PED snp file 

	for line in ped_file:
	  outputfile.write(line.strip()+"\n")
	return "snps_withnames.ped"


  
    
