"""
This script provides functions to load and parse VCF files and extract annotations from the INFO column.

======================
LoadVCF: Load the variants in a VCF file and parse CHROM,POS,REF,ALT,INFO columnd from the VCF file.
Input: 
vcf_file (str): The path to the VCF file that need to be annotated.

Output/Return: 
ret (list): A list of variant objects

======================
GetInfo: Extract informaction from the INFO column of a variant
Input: 
var(variant object): A variant object

Output/Return: 
2D list, annoations of each alternative allele at this position
"""

import argparse
import re

class INFO:
    def __init__(self,items):
        #items_tuple = []
        self.items = []
        for item in items:
            self.items.append(re.findall('^(.+)=(.+)',item)[0])
        self.items = dict(self.items)
    
    def get(self,id):
        return self.items[id]

class Variant:
    def __init__(self,header,var):
        columns = header.replace('#','').strip('\n').split('\t')
        entry = var.rstrip().split('\t')

        self.CHROM = entry[columns.index('CHROM')]
        self.POS = entry[columns.index('POS')]
        self.REF = entry[columns.index('REF')]
        self.ALT = entry[columns.index('ALT')].split(',')
        self.INFO = INFO(entry[columns.index('INFO')].split(';'))
        #self.CHROM = entry[columns.index('CHROMS')]


def LoadVCF(vcf_file):
    ret = []
    with open(vcf_file) as f:
        for line in f:
            if line.startswith('#CHROM'):
                header = line
            if line[0] != '#':
                variant = Variant(header,line)
                ret.append(variant)
    return ret

def GetInfo(var):
    chrom = var.CHROM
    pos = var.POS
    ref = var.REF
    alt = var.ALT
    dp = int(var.INFO.get('DP'))
    tp = var.INFO.get('TYPE')
    ao = var.INFO.get('AO')
    #ro = var.INFO.get('RO')
    if len(var.ALT) == 1:
        return [[chrom,str(pos),ref,alt[0],tp,dp,int(ao),int(ao)/dp]]
    else: # different alternative alleles are annotated separately
        tp = tp.rstrip().split(',')
        ao = ao.rstrip().split(',')
        ao = [int(e) for e in ao]
        return [[chrom,str(pos),ref,var.ALT[i],tp[i],dp,ao[i],ao[i]/dp] for i in range(len(var.ALT))]
