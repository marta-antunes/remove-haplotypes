#!/usr/bin/python2
# removes loci with more than 10% missing individuals 
import csv



def count_ind(file_name):
	with open(file_name) as f:
    		reader = csv.reader(f, delimiter='	', skipinitialspace=True)
    		first_row = next(reader)
    		num_cols = len(first_row)-3 #-3 is the removal of first, second and third (Cat,count and scaffold) columns
		return num_cols



def number_of_haplotypes_to_remove(number_of_individuals,missing_data):
	"""
	"""
	number_of_ind_to_remove=int(missing_data)*int(number_of_individuals)/100
	return number_of_ind_to_remove



def filter_haplotypes(FileName,missingData):
  inputfile=open(FileName,"r")
  outputfile=open("haplotypes_withoutChcu_filtered","w")
  cols=count_ind(FileName)
  removals=number_of_haplotypes_to_remove(cols,missingData)
  locus_removed=0
  locus_kept=0
  for line in inputfile:
    if line.startswith("Cat"):
      outputfile.write(line)
    else:
      locus=line[0]
      haplotypes=line[4:] #because haplotypes are in column 4,5,6...
      if haplotypes.count("-") > int(removals):
        locus_removed+=1
        pass
      else:
        locus_kept+=1
        outputfile.write(line)
  print "number of individuals removed:",removals+"\n"
  print "locus removed:"+str(locus_removed)
  print "locus kept:"+str(locus_kept)+"\n"
  return "haplotypes_withoutChcu_filtered"


#filter_haplotypes("Ad_haplotype_withoutChcu",11)


