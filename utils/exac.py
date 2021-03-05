"""
This script extracts allele frequency and the most severe consequence of a variant from ExAC.

Input:
id: string, with format [chromosome]-[position]-[ref]-[alt]

Output/Return:
allele_freq: float, allele frequency ('NA' if the information is not recorded in ExAC)
effect: str, the most severe consequence of the variant ('NA' if the information is not recorded in ExAC)
"""

#!/usr/bin/env python3
import requests

def GetExAC(id):
    effect_severity = [
        'transcript_ablation',
        'splice_acceptor_variant',
        'splice_donor_variant',
        'stop_gained',
        'frameshift_variant',
        'stop_lost',
        'start_lost',
        'transcript_amplification',
        'inframe_insertion',
        'inframe_deletion',
        'missense_variant',
        'protein_altering_variant',
        'splice_region_variant',
        'incomplete_terminal_codon_variant',
        'stop_retained_variant',
        'synonymous_variant',
        'coding_sequence_variant',
        'mature_miRNA_variant',
        '5_prime_UTR_variant',
        '3_prime_UTR_variant',
        'non_coding_transcript_exon_variant',
        'intron_variant',
        'NMD_transcript_variant',
        'non_coding_transcript_variant',
        'upstream_gene_variant',
        'downstream_gene_variant',
        'TFBS_ablation',
        'TFBS_amplification',
        'TF_binding_site_variant',
        'regulatory_region_ablation',
        'regulatory_region_amplification',
        'feature_elongation',
        'regulatory_region_variant',
        'feature_truncation',
        'intergenic_variant',
        'NA'
    ]

    rank = {e: i for i, e in enumerate(effect_severity)}

    data = requests.get(f"http://exac.hms.harvard.edu/rest/variant/variant/{id}")
    data = data.json()
    try:
        allele_freq = round(data["allele_freq"], 4)
    except: 
        allele_freq = "NA"
                
    try:
        effect = []
        for vep in data['vep_annotations']:
            effect.append(vep['major_consequence'])
        effect = list(set(effect))
        effect = sorted(effect, key=lambda x: rank[x])[0]
    except: 
        effect = "NA"
    return allele_freq , effect