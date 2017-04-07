#!/usr/bin/env python


def fill_chcu_dict(chcu_file):
	chcu_dict=dict()
	haplotypes=[]
	hap_file_chcu=open(chcu_file,"r") # hapstats file Chcu
	for line in hap_file_chcu:
	  if line.startswith("#"):
	    pass
	  else:
	    locus=line.split("\t")[1] # locus ID in catalog (tag)
	    haplotypes=line.split("\t")[13].strip().split(";")[0:]
	    for h in haplotypes:
	      if h==haplotypes[0]:
		chcu_dict[locus]=[h.split(":")[0]]
	      else:
		chcu_dict[locus].append(h.split(":")[0])
        print chcu_dict
	return chcu_dict

	#for k,v in chcu_dict.iteritems():  # list locus and haplotypes
	#  print k, v

	hap_file_chcu.close()

def remove_chcuHaplotypes(chcu_dict,population_file):
	hap_file=open(population_file,"r") # haplotype.tsv file for Ad
	OutFile=open("haplotypes_withoutChcu","w")
	removals_report=open("removals_report","w")
	countInputLines = 0 #receives the number of locus on input file
	countOutputLines= 0 #receives the number of locus on output file
	for line in hap_file:
          countInputLines=countInputLines+1
	  if line.startswith("Cat"):
	    OutFile.write(line)
	  else:
	    locus=line.split("\t")[0] # locus ID in catalog (tag)
	    if locus in chcu_dict:
	      cnt=line.split("\t")[1] # count of number of samples with this locus
	      haplotypes=line.strip().split("\t")[2:] # each column has the haplotypes for each individual

	      new_haplotype=[] #after removing chcu haplotype
	    
	      for h in haplotypes:
		if h.count("/")==0:
		  if h in chcu_dict[str(locus)]: # homozygotic for the same allele as chcu - retain one allele
		    new_haplotype.append(h)
		  else:                         # homozygotic for allele not present in chcu (not reliable)
		    new_haplotype.append("-")
		elif h.count("/")==1:
		  hap=h.split("/")
		  if hap[0] in chcu_dict[locus] and hap[1] not in chcu_dict[locus]: # heterozygotic for one allele of chcu - retain the other allele
		    new_haplotype.append(hap[1])
		  elif hap[0] not in chcu_dict[locus] and hap[1] in chcu_dict[locus]: # heterozygotic for one allele of chcu - retain the other allele
		    new_haplotype.append(hap[0])
		  else:
		    new_haplotype.append("-") # none of the alleles present in chcu - not reliable
		else:
		  new_haplotype.append("-") # more than 2 haplotypes per individual - not reliable
	      OutFile.write(str(locus)+"\t"+str(cnt)+"\t"+"\t".join(str(i) for i in new_haplotype)+"\n")
	      countOutputLines=countOutputLines+1
            
        removals_report.write("Number of locus Before remove chcu haplotypes:"+str(countInputLines)+"\n"+"Number of locus After remove chcu haplotypes:"+str(countOutputLines))
        print "Number of locus Before chcu haplotypes removal:", countInputLines
        print "Number of locus After chcu haplotypes removal:", countOutputLines
	return "haplotypes_withoutChcu"
	

