"""
Author: Xiaoman (Mia) Xie
Date: 03/04/2021
This script annotates a VCF file with variant information from the INFO column of the VCF and ExAC.
It takes two arguments:
-vcf: Input VCF to be annotated
-out: Path to the output file
Please run this script with command: python annotate.py -vcf [input_vcf_file] -out [name_of_output_file] 
"""

import os
import re
import sys
import argparse
#from collections import OrderedDict, deque
#from copy import copy
import pandas as pd
import utils.vcf as VCF
from utils.exac import GetExAC
import csv

def VCFAnnotate(input,output):
    with open(output, mode='w') as out:
        w = csv.writer(out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        w.writerow(['Chrom','Pos','Ref','Alt','Type','Effect','Read Depth','Alt Count','Alt Ratio','Allele Frequency'])

        for variant in VCF.LoadVCF(input): 
            var = VCF.GetInfo(variant)
            for e_var in var:
                var_id = '-'.join(e_var[0:4])
                allele_freq,effect = GetExAC(var_id)
                e_var.append(allele_freq)
                e_var.insert(5,effect)
                w.writerow(e_var)
    out.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='VCF Annotation')
    parser.add_argument('-vcf', type=str, help='Input VCF file')
    parser.add_argument('-o', type=str, help='Path to output file')
    args = parser.parse_args()

    VCFAnnotate(args.vcf,args.o)

