This repository contains chromosome/contig name mappings between UCSC &lt;-> Ensembl &lt;-> Gencode for a variety of genome.

The files are named `AAA_BBB2CCC.txt`, where `AAA` is a genome and version (e.g., GRCh37) and BBB and CCC are sources (namely, ensembl, UCSC, or gencode). Each file contains two columns. The first is the chromosome name in `BBB` and the second that in `CCC`. For example, let's suppose we're interested in converting gencode to ensembl chromosome names for GRCh37. We would then look in the `GRCh37_gencode2ensembl.txt` file and would see lines such as:

    chrX	X
    chrY	Y
    chrM	MT
    GL877870.2	HG1001_PATCH
    GL877872.1	HG1032_PATCH
    GL383535.1	HG104_HG975_PATCH
    JH159133.1	HG1063_PATCH

In this case, `chrX` is the gencode name and `X` is the equivalent Ensembl name.

Please submit a pull request or an issue if you find any errors!
