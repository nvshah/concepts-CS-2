# file_searcher

import os
from fuzzywuzzy import fuzz

root_dir = input('Enter root directory for your search: ')
file_types = input('Enter the file extensions to look for (seperated by spaces) (Empt = All): ')
fuzzy_search = input('Enter a search query (Empty = Any): ')

file_types = tuple(file_types.split())

for root, dirs, files in os.walk(root_dir):
    for name in files:
        if (not file_types) or name.endswith(file_types):
            if ((not fuzzy_search) or
              fuzz.token_sort_ratio(fuzzy_search.lower(), name.lower()) > 50):
                print(root + os.sep + name)
        