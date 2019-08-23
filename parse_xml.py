# adapted from https://github.com/AnneliektH/EVEs_arthropod/blob/master/parse_xml.py
from __future__ import division
from Bio.Blast import NCBIXML
import csv
import sys
import pandas as pd

result = NCBIXML.parse(open(sys.argv[1]))
output = sys.argv[2]

# Write a header for the outputfile
header = ('sequence', 'length', 'perc_identity', 'gaps', 'frame',
          'position_on_hit_start','position_on_hit_stop',
          'position_on_query_start', 'position_on_query_stop', 'evalue',
          'score',  'direction')

# open the outputfile
with open(output,'w') as f:
  writer = csv.writer(f)
  writer.writerow(header)

  # Go into fasta records
  for record in result:

    # Go into fasta alignments
    if record.alignments:

      # Check each alignment
      for alignment in record.alignments:

          # Make recognizable names for all xml input objects.
          for hsp in alignment.hsps:
            sequence = alignment.title
            length = hsp.align_length
            perc_identity = float((hsp.identities/hsp.align_length)*100)
            gaps = hsp.gaps
            query_frame = hsp.frame
            direction = record.query

            # Hit is viral hit from viral database
            position_on_hit_start = hsp.sbjct_start
            position_on_hit_stop = hsp.sbjct_end

            # Query is piRNA cluster of insect
            position_on_query_start = hsp.query_start
            position_on_query_stop = hsp.query_end
            evalue = hsp.expect
            score = hsp.score

            # Write to csv
            row = (sequence, length, perc_identity, gaps, query_frame[0],
            position_on_hit_start, position_on_hit_stop ,position_on_query_start,
            position_on_query_stop, evalue, score, direction)
            writer.writerow(row)

  # close the file
  f.close()
  result.close()

df = df = pd.read_csv(output)
# max eval on position_on_query_start is equal
max_eval = df.groupby(['sequence', 'position_on_query_start']).evalue.transform(max)
df4 = df[df.evalue == max_eval]

# max eval on position_on_query_stop is equal
max_eval = df.groupby(['sequence', 'position_on_query_stop']).evalue.transform(max)
df5 = df[df.evalue == max_eval]

# merge both max tables
df = df4.append(df5)

# and remove where start sequence is equal
df = df.drop_duplicates(['sequence', 'position_on_query_start'])

# remove where stop sequence is equal
df = df.drop_duplicates(['sequence', 'position_on_query_stop'])

#remove where stop and start are equal
df = df.drop_duplicates([ 'sequence', 'position_on_query_start', 'position_on_query_stop'])

# output to csv
df.to_csv(output.rstrip('.csv')+'_filtered.csv', index = False)

result.close()
