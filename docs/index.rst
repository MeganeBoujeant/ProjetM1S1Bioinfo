.. ProjectM1S1Bioinfo documentation master file, created by
   sphinx-quickstart on Wed Nov 18 16:44:39 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to ProjectM1S1Bioinfo's documentation!
==============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   	
Quickstart Demo (GUIless) 
*************************
- Let's import our two classes :: 

   from blast_hitter import BlastHitter
   from clusterizer import Clusterizer

- Proteomes can be downloaded with RefSeqScraper script, or manually saved to data/genomes repository. A list of all paths should be initalised, so that we can use BlastHitter's factory method to create a bunch of blasthitter objects of all possible permutations. :: 

   proteomes = ["../data/genomes/Rickettsia_rickettsii_str._Arizona_strain=Arizona_protein.faa",            
   "../data/genomes/Streptococcus_pneumoniae_R6_strain=R6_protein.faa",
   "../data/genomes/Streptococcus_pyogenes_strain=NCTC8232_protein.faa",
   "../data/genomes/Streptococcus_thermophilus_LMD-9_strain=LMD-9_protein.faa",
   "../data/genomes/Piscirickettsia_salmonis_strain=Psal-158_protein.faa"]

   bhitters = BlastHitter.from_list(proteomes)

- We can blast them and accumulate the reciprocal best hits with a for loop : :: 

   for bh in bhitters  : 
       bh.blast_them()
       bh.rbh_them()

- Now let's create a Clusterizer object after populating our blasthitters with RBH files : :: 

   clust = Clusterizer(bhitters, proteomes)
   
- The next and final step would be to create clusters, aligning each one and concatenating all of them and last but not least would be to launch the phylogenetic algorithm and to draw the newick tree: :: 

   clust.cluster_them()
   clust.one_align_to_rule_them_all()
   clust.draw_tree()
     
   
Documentation
*************
.. toctree::
   :maxdepth: 2
   :caption: Contents:

Graphical User Interface
========================
.. automodule:: interface
   :members:
   
RefSeqScraper
=============
.. automodule:: refseq_scraper
   :members:

BlastHitter
===========
.. automodule:: blast_hitter
   :members:

Clusterizer
===========
.. automodule:: clusterizer
   :members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
