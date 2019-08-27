import sys
import pandas as pd

#read in blast result csv
df = pd.read_csv(sys.argv[1])
output = sys.argv[2]

# get query start and end positions from full table
bed = df.iloc[:,7:9]
# get accession number from "direction" column and insert into first position
bed.insert(0,'accession', [x.split(' ')[0] for x in df.direction])

#write out to a tsv with bed file suffix
bed.to_csv(output, sep='\t', header=False, index=False)
