#!/usr/bin/python2
#RH_pipeline:RH Remove Haplotypes
import subprocess
import sys
import os
from remove_chcu_haplotypes import *
from filter_haplotypes import filter_haplotypes
from haplotype_frequencies import get_frequencies
from replace_missing_coded import replace_missing_coded
from transpose_table_tabs import transpose_table_tabs
from convert_haplotypes_to_snps_ped_format import convert_haplotypes_to_snps_ped_format
from convert_snpslist_map_format import convert_snpslist_map_format
from add_snpsnames import add_snpsnames
from transpose_table_spaces import transpose_table_spaces
from filter_snps import filter_snps
from get_map import get_map



#input files and parameters
try:
	populationHaplotypes_file = sys.argv[1]
	reference_haplotypes = sys.argv[2]
	missing_data = sys.argv[3]
except:
	print "Not enough arguments provided... Usage: RH_pipeline.py haplotypes reference_haplotypes %_of_missing_data"
	sys.exit(1)




##################################### call functions  #################################################################################
#departure_point: we have haplotypes for each individual that is the result of crossing population with homokariotipic chcu



#construct a dictionary of chcu based on information in batch_1.hapstats.tsv
chcu_dictionary=fill_chcu_dict(reference_haplotypes)


print "\n"+"Removing chcu haplotypes...\n"
#remove from Haplotypes Ad or Gro x chcu file (batch_1.haplotypes.tsv) what is in the dictionary of chcu
haplotypes_without_chcu=remove_chcuHaplotypes(chcu_dictionary,populationHaplotypes_file)


print "Filtering Haplotypes...\n"
#if the symbol '-'(missing data) ocorres more than x times, the haplotype is removed; 
#if the % of missing data is higher than some value, the correspondent haplotype is removed;   
filtered_haplotypes=filter_haplotypes(haplotypes_without_chcu,missing_data)


print "Getting frequencies...\n"
#haplotype_frequencies()
frequencies=get_frequencies(filtered_haplotypes)
print "Frequencies done!\n"


#replace '-' haplotypes for '0000000000'
missing_code_replaced=replace_missing_coded(filtered_haplotypes)


#transpose table
print "transposing table...\n"
transposed_table=transpose_table_tabs(missing_code_replaced)


print "getting provisory ped format without snps names...\n"
#the ped format includes:... 
haplotypes_pedFormat_provis=convert_haplotypes_to_snps_ped_format(transposed_table)


print "getting map format...\n"
#the map format: By default, each line of the MAP file describes a single marker and must contain exactly 4 columns: 
#chromosome (1-22, X, Y or 0 if unplaced),rs# or snp identifier, Genetic distance (morgans) is 0 if unknown, and Base-pair position (bp units)  is 0 if unknown
#chromosome we put all 1 because we don't know???
#snp identifier (ex.25-0 means locus 25 and max lengh of locus 25 is 0???)
haplotypes_map_format=convert_snpslist_map_format(filtered_haplotypes)


#append snps names to the beginning of peds file
print "appending snps names...\n"
snpNames_added=add_snpsnames(haplotypes_map_format,haplotypes_pedFormat_provis)


print "checking number of columns...\n"
#get number of columns in each line (just to check if the matrix is correct), variable NF is set to the total number of fields in the input record
file_out=open("snps_withnames_numbcolumns","w")
check_numberOfColumns_in_matrix = subprocess.Popen(['awk', '{print NF}', snpNames_added],stdout=file_out)


#Tranpose matrix
transpossed_table_spaces=transpose_table_spaces(snpNames_added,"snps_withnames_transposed")


#filter snps to exclude snps with more than 2 alleles
print "filtering snps...\n"
filtered_snps=filter_snps(transpossed_table_spaces)


#Remove first column (names of snps) and separator
print "removing names snps...\n"
outputFile = open("snps_removenames_snps","w")
remove_firstColumn = subprocess.Popen(['awk','BEGIN{FS=OFS=" "}{$1="";sub(" ","")}1',filtered_snps],stdout=outputFile)


#Transpose again to get final PED
print "obtaining final ped...\n"
print transpose_table_spaces("snps_removenames_snps","snps.ped")





#Get MAP file from filtered snps
#doubles the entries
print "doubling entries...\n"
doubled=get_map(filtered_snps)


#remove every other line
print "removing duplicated lines...\n"
outFile = open('snps.map','w')
haplotypes_map_format_final = subprocess.Popen(['awk','NR % 2==0',doubled],stdout=outFile)
outFile.close()






