import sys
import pandas as pd

#read in BLAST result csv
rownames = ['query', 'subject', 'per_id', 'length', 'mismatch', 'gap_open', 'q_start', 'q_end', 's_start', 's_end', 'evalue', 'bitscore']
df = pd.read_csv(sys.argv[1],sep = '\t', header=None, names = rownames)

# first remove sequences with the same start and end position
def remove_dup(df):
    df.sort_values('evalue', inplace=True)  #sort on e value, lowest (best) evalue is first
    df.drop_duplicates(['query', 'q_start', 'q_end'], inplace=True, keep="first")
    df.reset_index(inplace=True, drop=True)
    return df

# now remove hits that overlap by any amount, keeping the higher blast score
def remove_overlap(df):
    df_grouped=df.groupby('query') # group the dataframe by query
    # list to store index that are either unique enough or have highest evalue
    results = []
    # list to save those that have already been added so they can be skiped
    to_be_skipped = []

    for group_name, df_group in df_grouped:

        for index, row in df_group.iterrows():

            # check if sequence or simmilar sequence already added
            if index in to_be_skipped:
                continue

            # initialize empty simmilar dict
            similar = {}

            for index2, row2 in df_group.iterrows():

                # check if possition start or stop is equal and is not self.
                if index == index2:
                    continue

                # check if possition start or stop is equal and is not self.
                    # if entry is comparing to itself
                if row[7] == row2[7] and row2[8] == row[8]:
                    continue

                elif (row[7] in range(row2[7], row2[8]) or
                row2[7] in range(row[7], row[8]) or
                row[8] in range(row2[7], row2[8]) or
                row2[8] in range(row[7], row[8])):
                    # add both indexes of simmilar sequences plus their score to the dict
                    similar[index] = row[10]
                    similar[index2] = row2[10]

            # check if simmilar sequences have been found
            if len(similar) > 0:

                # get the max score from the simmilar sequences
                max_index = max(similar, key=similar.get)

                # add index with maximum score to results list
                results.append(max_index)

                # add checked indices to be skipped list
                for k,v  in similar.items():
                    to_be_skipped.append(k)

            # if seqeunce is unique add index to results
            if len(similar) == 0:
                results.append(index)
                to_be_skipped.append(index)
    return df.loc[results]

df_dedup = remove_dup(df)
df_unique = remove_overlap(df_dedup)

df_unique.to_csv(sys.argv[2])
