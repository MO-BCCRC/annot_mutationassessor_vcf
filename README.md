#annot_mutationassessor_vcf:
annotates a vcf file with mutationassessor db


```
Development information

date created : 5 May 2015
last update  :
Developer    : Jamie Rosner (jrosner@bccrc.ca)
Input        : vcf, mutation assessor db directory
Output       : annotated vcf
Parameters   :
Seed used    : annotate_mutation_assessor.py
```

###Usage:
specify a vcf file and a MA database directory and the MA annotation will be placed in the
INFO section of the vcf file

* vcf files should be sorted by chromosome and position in order to prevent poor performance

###Dependencies

- python

###Known issues


###Last updates

