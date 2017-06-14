This repository contains chromosome/contig name mappings between UCSC &lt;-> Ensembl &lt;-> Gencode for a variety of genomes.

The files are named `AAA_BBB2CCC.txt`, where `AAA` is a genome and version (e.g., GRCh37) and BBB and CCC are sources (namely, ensembl, UCSC, or gencode). Each file contains two columns. The first is the chromosome name in `BBB` and the second that in `CCC`. For example, let's suppose we're interested in converting gencode to ensembl chromosome names for GRCh37. We would then look in the `GRCh37_gencode2ensembl.txt` file and would see lines such as:

    chrX	X
    chrY	Y
    chrM	MT
    GL877870.2	HG1001_PATCH
    GL877872.1	HG1032_PATCH
    GL383535.1	HG104_HG975_PATCH
    JH159133.1	HG1063_PATCH

In this case, `chrX` is the gencode name and `X` is the equivalent Ensembl name.

Missing Chromosomes/Contigs
---------------------------

It's not always the case that a given chromosome/contig exists in all sources. An example of that is `GRCh38_gencode2ucsc.txt`. There, a number of entries exist in gencode that are absent in UCSC. In cases such as this, the second column in a txt file will simply be empty:

    KI270937.1      chr3_KI270937v1_alt
    KI270938.1      chr19_KI270938v1_alt
    KN196472.1      
    KN196473.1      

There is always a second tab-separated field above, but `KN196472.1` and `KN196473.1` simply don't exist in UCSC. So a script using these files can simply look for columns with values "" to indicate "missing".

Different sized chromosomes/contigs
-----------------------------------

Please note that while the sequence contained in one system may be completely present in another, the coordinates used may not be the same. This is commonly seen with Ensembl chromosome/contig names for "alt-scaffolds", "fix-patches", and "novel-patches". Ensembl will place "NNN" on either side of the sequence so that the patched or scaffolded sequence has the appropriate position compared to the chromosome it's related to. In NCBI, these sequences are not N-padded, so while the sequences are the same, the positions are offset from each other. Such cases are treated as with missing chromosomes/contigs.

Ambiguous/multi-way mappings
----------------------------

Occasionally, e.g., with mm9, UCSC will merge contigs together into an ordered `*_random` sequence. This means that an individual entry in UCSC can map to multiple entries in Ensembl and Gencode. Such case are treated the same as missing entries, described above. An alternative would be to provide a comma-separated list of mapping targets and their chromosome offsets and or ranges. As this situation tends to only occur in older UCSC reference genomes, which are decreasingly used, I would prefer to avoid this complication.

Patch versions
--------------

It's often the case that a patch will have an associated version, such as `.2` in `KB469738.2`. While the patch itself will exist across genome updates, the version number may change. Consequently, it may be required to strip off these version when performing name conversions, simply to support different versions/patches of the same genome.

Note
----

Note that some data sources are absent. For example, wormbase has not been included, since it's chromosome naming system is identical to that in Ensembl.

Please submit a pull request or an issue if you find any errors!

Galaxy tool
-----------

These mapping tables can be use with the [replace_chromosome_names](https://toolshed.g2.bx.psu.edu/view/earlhaminst/replace_chromosome_names/) Galaxy tool to replace chromosome names in a tabular dataset in [Galaxy](https://galaxyproject.org/).
