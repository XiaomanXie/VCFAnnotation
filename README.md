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
| Column | Description | Note |
|     :---:    |     :---:      | :--- |
| Chrom   | Chromosome     | CHROM field in the VCF file.  |
| Pos     | Position       | POS field in the VCF file.|
|Ref|Reference base(s) |REF field in the VCF file.|
|Alt| Alternative base(s)|While the ALT field in VCF file is a comma separated list, there is only one allele in the Alt field of the annotated file.|
|Type| Variant type| The type of allele, either snp, mnp, ins, del, or complex. Parsed from the 'TYPE' sub-field of INFO.|
|Effect| Effect/Consequence of the variant (missense, intergenic, etc.) |The effect of each variant is the 'major consequence' obtained from ExAC. If there are multiple major consequences for one variant, they are ranked according to the severity reported by Ensembl. The variant is annotated with the most deleterious consequence.|
|Read Depth|Depth of sequence coverage at the site of variation | Total read depth at the locus. Parsed from the 'DP' sub-field of INFO.|
|Alt Count| Number of reads supporting the variant|Alternate allele observations, with partial observations recorded fractionally. Parsed from the 'AO' sub-field of INFO. |
|Alt Ratio| Percentage of reads supporting the variant versus those supporting reference reads|The ratio of Alt count to Read Depth.|
|Allele Frequency| Allele frequency in the range (0,1]| Allele frequency of variant from ExAC API. |



