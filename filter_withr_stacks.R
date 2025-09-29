#####STEP 1: FILTERING

#####WE TOOK THE OG SCRIPTS AND FUNCTIONS FROM: https://github.com/jdalapicolla/LanGen_pipeline_version2

pacman::p_load(r2vcftools, tidyverse, vcfR, SNPRelate, dartR, poppr, adegenet, LEA, pcadapt, qvalue, psych, tess3r, VennDiagram, sf)
vcf_file="populations.all.vcf"
snps_raw =  vcfLink(vcf_file, overwriteID=T)
snps = Filter(snps_raw, filterOptions(max.alleles=2, min.alleles=2), indels="remove")
snps_unind = snps
genotypes = GenotypeMatrix(snps_unind)
Missing = apply(GenotypeMatrix(snps_unind), 2, function(x) sum(x < 0)/length(x)*100)
Missing.df = Missing %>%
as.data.frame() %>%
rownames_to_column(., var = "ID_original") %>%
mutate (ID = str_remove(ID_original, pattern="_sorted")) %>%
setNames(., c("ID_original", "Missing", "ID"))
View(Missing.df)
max20=20
df2<-filter(Missing.df, Missing <= max20)
snps_missinglocilessthan20 = Subset(snps_unind, sites = df2$ID)
Save(snps_missinglocilessthan20, paste0("filtered_chordodes_less20.vcf"))

