#!/usr/bin/python2


from sys import argv


def get_frequencies(fileName):
  hap_file_samples=open(fileName,"r") # haplotype file for individuals from stacks
  outfile=open("freq","w") 

  for line in hap_file_samples:
    if line.startswith("Cat"):
      pass
    else:
      locus=line.split("\t")[0] # locus ID in catalog (tag)
      haplotypes=line.strip("\n").split("\t")[4:]
      
      set_haplotypes=set(haplotypes)
      set_haplotypes.discard("-")
      set_haplotypes.discard("-\n")
      
      #print locus, len(set_haplotypes)
      for h in set_haplotypes:
	 outfile.write(str(locus)+" "+h+" "+str(haplotypes.count(h))+"\n")
  return "freq"
	


