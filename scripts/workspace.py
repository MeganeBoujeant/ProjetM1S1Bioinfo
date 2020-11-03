#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 12:46:59 2020

"""

import os 
os.chdir("/home/ghassan/M1/ProjetM1S1Bioinfo/scripts") # mégane change le chemin pour que ça colle avec ton ordi
from seqkit_stats import stats
from parse_proteome import parse_fasta
from programme_un import blast


proteome1 = "../data/genomes/Yersinia_pestis_strain=FDAARGOS_protein.faa"
proteome2 = "../data/genomes/Aliivibrio_salmonicida_LFI1238_strain=LFI_protein.faa" 


stats(proteome1)
stats(proteome2)

prot1 = parse_fasta(proteome1)
prot2 = parse_fasta(proteome2)
prot1

cmdblast1, output1 = blast(proteome1,proteome2)

cmdblast1
output1

os.system(cmdblast1)
