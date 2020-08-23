"""
# README
## A collection of custom helper functions for data science projects

Functions are ordered along the following topics 
> 1.    Export data
> 2.    Retrieve data
> 3.    Process lists
> 4. 	Miscellaneous


"""


import pandas as pd
import os
from time import strftime


#######################################################
### 1. Export data
#   make_csv()
#   timestamp_now()
#######################################################

def make_csv(x, filename, data_dir, append=False, header=False, index=False):
    '''Merges features and labels and converts them into one csv file with labels in the first column.
       :param x: Data features
       :param file_name: Name of csv file, ex. 'train.csv'
       :param data_dir: The directory where files will be saved
       '''
    
    # create dir if nonexistent
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    # make sure its a df
    x = pd.DataFrame(x)
    
    # export to csv
    if not append:
        x.to_csv(os.path.join(data_dir, filename), 
                                     header=header, 
                                     index=index)
    # append to existing
    else:
        x.to_csv(os.path.join(data_dir, filename),
                                     mode = 'a',
                                     header=header, 
                                     index=index)        
    
    # nothing is returned, but a print statement indicates that the function has run
    print('Path created: '+str(data_dir)+'/'+str(filename))
    

def timestamp_now():
    """Create timestamp string in format: yyyy/mm/dd-hh/mm/ss
        primaryliy used for file naming

    Input
        None
        
    Return
        String: Timestamp for current time
        
    """
    
    timestr = strftime("%Y%m%d-%H%M%S")
    timestamp = '{}'.format(timestr)  
    
    return timestamp





#######################################################
### 2. Retrieve data
#   get_firms_sp500()
#   regex_strip_legalname()
#######################################################

def get_firms_sp500():
    """Obtain S&P 500 listings from Wikipedia"""
    table=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    df_sp500 = table[0]
    
    return df_sp500

import re
def regex_strip_legalname(raw_names):
    """Removes legal entity, technical description or firm type from firm name
    
    Input
        raw_names: list of strings with firm names
        
    Return
        list of strings: firm names without legal description 
    
    """
    
    pattern = r"(\s|\.|\,|\&)*(\.com|Enterprise|Worldwide|Int\'l|N\.V\.|LLC|Co\b|Inc\b|Corp\w*|Group\sInc|Group|Company|Holdings\sInc|\WCo(\s|\.)|plc|Ltd|Int'l\.|Holdings|\(?Class\s\w+\)?)\.?\W?"
    stripped_names = [re.sub(pattern,'', n) for n in raw_names]
    
    return stripped_names







#######################################################
### 3. Process lists
#   list_flatten()
#   list_remove_duplicates()
#   list_batch
#######################################################

def list_flatten(nested_list):
    """Flattens nested list"""
    return [element for sublist in nested_list for element in sublist]

def list_remove_duplicates(l):
    """Removes duplicates from list elements whilst preserving element order
    adapted from 
    https://stackoverflow.com/questions/480214/how-do-you-remove-duplicates-from-a-list-whilst-preserving-order
    
    Input
        list with string elements
    
    Return 
        Sorted list without duplicates
    
    """
    seen = set()
    seen_add = seen.add
    return [x for x in l if not (x in seen or seen_add(x))]

def list_batch(lst, n=5):
    """Yield successive n-sized chunks from list lst
    
    adapted from https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
    
    Input
        lst: list 
        n: selected batch size
        
    Return 
        List: lst divided into batches of len(lst)/n lists
    """
    
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


#######################################################
### 4. Miscellaneous
#   date_add_year()
# 	sleep_countdown()
#######################################################

from datetime import date

def date_add_year(d, years):
    """Add/subtract a year from today's date 
    Return the same calendar date (month and day) in the
    destination year, if it exists, otherwise use the following day
    (e.g. changing February 29 to March 1). 
    Source: https://stackoverflow.com/a/15743908

    Input: 
		d: datetime, date
		years: int, number of years to add/subtract from date d
    
    Return:
		date: date with year added/subtracted 
    """
    try:
        return d.replace(year = d.year + years)
    except ValueError:
        return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))    


import sys

def sleep_countdown(duration, print_step=2):
	"""Sleep for certain duration and print remaining time in steps of print_step
	
	Input
		duration: duration of timeout (int)
		print_step: steps to print countdown (int)

	Return 
		None
	"""
	for i in range(duration,0,-print_step):
	    sleep(print_step)
	    sys.stdout.write(str(i-print_step)+' ')
	    sys.stdout.flush()