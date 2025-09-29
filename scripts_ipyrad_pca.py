import ipyrad.analysis as ipa
import pandas as pd
import toyplot
imap = {
 "GTA": ["BLM", "CAS", "CH116", "DGL", "FMW", "GIW", "HMM", "MCCH_02", "MPW", "NAS", "XBF"],
 "YIL": ["ALV", "BDSN", "CFHF_01", "L1S", "LOG"],
 "JHI": ["AVX", "DVD", "FLAC", "JPG", "KTV", "MP_04", "WAV"],
 "CEN": ["CH413", "MMN", "NOU", "XCL"],
}
data="notov_from2lmsbr_21.snps.hdf5" ####OR WHICH HDF5 FILE YOU WANT TO USE
minmap = {i: 0.5 for i in imap}
ipa.snps_extracter(data).names
['ALV', 'AVX', 'BDSN', 'BLM', 'CAS', 'CFHF_01', 'CH116', 'CH413', 'DGL', 'DVD', 'FLAC', 'FMW', 'GIW', 'HMM', 'JPG', 'KTV', 'L1S', 'LOG', 'MCCH_02', 'MMN', 'MPW', 'MP_04', 'NAS', 'NOU', 'WAV', 'XBF', 'XCL']
pca3 = ipa.pca(
   data=data,
   imap=imap,
   minmap=minmap,
   mincov=0.5,
   impute_method=4,
)
pca3.run(nreplicates=100, seed=123)
pca3.draw(0, 2);
pca3.draw(outfile="mincov05mypca.pdf")
