#!/usr/bin/python2
# removes loci with more than 10% missing individuals


def filter_snps(fileName):

  inputfile=open(fileName,"r") # PED snp file transposed (locus x ind) Ad_snp_transposed
  outputfile=open("snps_withnames_transposed_filteredsnps","w")
  
  for line in inputfile:
    if line.startswith("#"):
       outputfile.write(line.strip()+"\n")
    else:
      alleles=[]
      snps=line.strip().split(" ")[1:]
      for s in snps:
        if s in ("A","T","C","G"):
          alleles.append(s)
        else:
          pass
        
      set_alleles=set(alleles)
      
      if len(set_alleles)>2:
        #removes snps with more than 2 alleles
        pass
      else:
         outputfile.write(line.strip()+"\n")
  return "snps_withnames_transposed_filteredsnps"

  
