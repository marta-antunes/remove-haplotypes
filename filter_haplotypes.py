#!/usr/bin/python2
# removes loci with more than 10% missing individuals 

def filter_haplotypes(FileName,missing_data):
  inputfile=open(FileName,"r")
  outputfile=open("haplotypes_withoutChcu_filtered","w")
  locus_removed=0
  locus_kept=0
  for line in inputfile:
    if line.startswith("Cat"):
      outputfile.write(line)
    else:
      locus=line[0]
      haplotypes=line[2:]
      if haplotypes.count("-") > int(missing_data):
        locus_removed+=1
        pass
      else:
        locus_kept+=1
        outputfile.write(line)
  print "locus removed:"+str(locus_removed)
  print "locus kept:"+str(locus_kept)+"\n"
  return "haplotypes_withoutChcu_filtered"
  	    

