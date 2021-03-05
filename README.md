# VCFAnnotation

VCFAnnotation is a small tool written in Python to annotate each variant in a given VCF files with the information 
parse from the VCF file as well as annotations extracted from ExAC. It can report monomorphic sites, sites with reference alleles inconsistent with the reference genome, sites with invalid genotypes, non-SNP site (e.g. indels), and all sites with allele frequencies greater than ''0.5''. After you passed the checking, you can go on to run rvtests - rare-variant test software.
This program is used to annotate each variant in the provided vcf file. The program is written in python 3.6, please make sure you have the right version installed.
For this challenge, you are asked to prototype a variant annotation tool. We will provide you with
a VCF file, and you will create a small software program to annotate each variant in the file.
Each variant must be annotated with the following pieces of information:
1. Type of variation (substitution, insertion, CNV, etc.) and their effect (missense, silent,
intergenic, etc.). If there are multiple effects, annotate with the most deleterious
possibility.
2. Depth of sequence coverage at the site of variation.
3. Number of reads supporting the variant.
4. Percentage of reads supporting the variant versus those supporting reference reads.
5. Allele frequency of variant from ExAC API (API documentation is available here:
http://exac.hms.harvard.edu/).
6. Any additional annotations that you feel might be relevant.

This repository is for the Tempus Bioinformatics Technical Challenge as described in the TempusBioinformaticsChallenge.pdf.

The instructions were:

For this challenge, you are asked to prototype a variant annotation tool. We will provide you with a VCF file, and you will create a small software program to output a table annotating each variant in the file. Each variant must be annotated with the following pieces of information:

Type of variation (Substitution, Insertion, Silent, Intergenic, etc.) If there are multiple possibilities, annotate with the most deleterious possibility.
Depth of sequence coverage at the site of variation.
Number of reads supporting the variant.
Percentage of reads supporting the variant versus those supporting reference reads.
Allele frequency of variant from Broad Institute ExAC Project API (API documentation is available here: http://exac.hms.harvard.edu/)
Additional optional information from ExAC that you feel might be relevant.
Additional instructions were "It is acceptable to use variant annotation tools (snpEff, Oncotator, VEP, etc.) for addition of gene, effect and transcript information. All I/O, transformations, and external source interactions must be done with standard libraries (numerical libraries or data frame libraries such as pandas are also acceptable).

Please use this opportunity to demonstrate your knowledge of software development and your abilities to think critically about how a toy program like this should be engineered."

How to Run
Run build.sh to create the environment if you like, but the environment.yml file uploaded simplifies the process and all you need to run is simply :

bash annotate.sh
to create the environment from the YML file, it installs VEP, annotates with VEP, then runs annotate.py and creates the final resulting VCF file, final.vcf.

FINAL FILE ("final.vcf") has "Custom" column at the end of the columns. This contains:
