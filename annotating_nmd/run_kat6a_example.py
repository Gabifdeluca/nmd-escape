import pandas as pd
from annotating_nmd import *  # Import necessary functions

# Path to the kat6a_mutations.bed file in the tests/data/ directory
bed_file_path = 'tests/data/kat6a_mutations.bed'

# Step 1: Read the kat6a_mutations.bed file into a pandas DataFrame
cds_bed_df = pd.read_table(bed_file_path, names=['chrom', 'start', 'end', 'cds_id', 'score', 'strand'])

# Print the DataFrame to inspect the data
print("CDS BED DataFrame:")
print(cds_bed_df)

# Step 2: Generate sizes dataframe using the make_cds_size_df function
sizes_df = make_cds_size_df(cds_bed_df)

# Print the resulting sizes dataframe
print("\nCDS Sizes DataFrame:")
print(sizes_df)
