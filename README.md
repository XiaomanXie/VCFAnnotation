# VCFAnnotation

VCFAnnotation is a small tool written in Python to annotate each variant in a given VCF files with the information 
parsed from the VCF file as well as annotations extracted from ExAC. For variants with multiple possible alternative 
allels at the same location, alternative alleles are separated into different rows so that each row has only one 
alternative allele, which is further annotated with correponding variant type and effect.
Each variant is annotated with the following pieces of information:
1. Type of variation (snp(Single Nucleotide Polymorphism), mnp(Multiple Nucleotide Polymorphism), del(Deletion), ins(Insertion), complex(Complex Variant))
2. Effect/Consequence of the variant (missense, intergenic, etc.). Variant major consequence is obtained from ExAC. If there are multiple effects, the variant is annotated with the most deleterious possibility according to Ensembl variant severity (http://useast.ensembl.org/info/genome/variation/prediction/predicted_data.html). 
3. Depth of sequence coverage at the site of variation.
4. Number of reads supporting the variant.
5. Percentage of reads supporting the variant versus those supporting reference reads.
6. Allele frequency of variant from ExAC API (API documentation is available here:
http://exac.hms.harvard.edu/).

## Run
Please first download the repository:
```
git clone https://github.com/XiaomanXie/VCFAnnotation.git
```
In the repository, run the main script annotate.py using the following command to annotate the input VCF file. Names in < > are for the user to replace with the appropriate file names.
```
python annotate.py -vcf <input.vcf> -o <output.csv>
```
If you wish to use the sample VCF file, please use:
```
python annotate.py -vcf Challenge_data_\(1\).vcf -o Annotated_VCF.csv
```
## Output file
The annotated variants are included in the output csv file. 
| Column | Meaning | Description |
|     :---:    |     :---:      |          ---: |
| Chrom   | git status     | git status    |
| Pos     | git diff       | git diff      |
|Ref| | |
|Alt| | |
|Type| | |
|Effect| | |
|Read Depth| | |
|Alt Count| | |
|Alt Ratio| | |
|Allele Frequency| | |

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
