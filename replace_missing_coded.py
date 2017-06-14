#!/usr/bin/python2


def replace_missing_coded(fileName):

  hap_file_samples=open(fileName,"r") # haplotype file Ad locusxind
  outputfile=open("haplotype_withoutChcu_filtered_missing_coded","w")



  for line in hap_file_samples:
    if line.startswith("Cat"):
      #cat=line.split("\t")[0] # locus title
      ind=line.split("\t")[4:] # individuals names
      outputfile.write("CatalogID"+"\t"+"\t".join(str(i) for i in ind))
    else:
      locus=line.split("\t")[0] # locus ID in catalog (tag)
      haplotypes=line.strip("\n").split("\t")[4:]
      nbases=len(max(haplotypes,key=len))# get the maximum number of bases of the locus
      #print nbases
      hap=[]
      for h in haplotypes:
        if h=="-":
	  hap.append(nbases*"0")
        else:
	  hap.append(h)

      outputfile.write(locus+"\t"+"\t".join(str(i) for i in hap)+"\n")   #without loci names
  return "haplotype_withoutChcu_filtered_missing_coded"

