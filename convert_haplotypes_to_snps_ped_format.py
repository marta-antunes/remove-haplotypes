#!/usr/bin/python2
# converts haplotype file (from stacks, filtered, missing coded and transposed) to PED snp format (plink)


def convert_haplotypes_to_snps_ped_format(fileName):
  inputfile=open(fileName,"r") # haplotype file Ad individuals(rows) x locus (columns) - resulted from transpose_table
  outputfile=open("snps_provis.ped","w")
   
   
  for line in inputfile:
    if line.startswith("Cat"):
      pass
    elif line.startswith("BP"):
      pass
    else:
      ind=line.split("\t")[0]
      haplotypes=line.strip("\n").split("\t")[1:]
      snps=[]
      for hap in haplotypes:
        for h in hap:
          snps.append(h)
      outputfile.write( "1"+" "+ind+" "+"0"+" "+"0"+" "+"0"+" "+"0"+" "+" ".join((str(i)+" "+str(i)) for i in snps)+"\n")
  return "snps_provis.ped"
      

