"""
Nome: Gabriel Melo
Matrícula: 125.304-6

Modo de uso

Case Sensitive: python word_finder [PALAVRA]
Case Insensitive: python word_finder [PALAVRA] -i
"""

import re
import argparse
import pandas as pd

parser = argparse.ArgumentParser(description="Search for an exact word in a specific CSV column using Regex.")
    
# Required positional arguments
parser.add_argument("word", help="The exact word to search for")
parser.add_argument("-i", "--ignore-case", action="store_true", 
                    help="Make the search case-insensitive")

args = parser.parse_args()

ignore_case = re.IGNORECASE if args.ignore_case else 0

df = pd.read_csv("./rdany-chat.csv")
df = df[["source", "text", "date", "hour"]]

target_word = args.word
column_name = "text"

regex_pattern = rf'\b{target_word}\b'
filtered_df = df[df[column_name].str.contains(regex_pattern, regex=True, flags=ignore_case, na=False)]

occurrence_count = len(filtered_df)

print(f"\nOccurrences: {occurrence_count}")
print(filtered_df)