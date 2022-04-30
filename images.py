# Import modules

import pandas as pd 
import urllib.request   

# ----------------------------------------------------------------
def url_to_jpg(i, url, file_path):



    #get the original file name with format jpg
    filename = url.split('/')[-1]
    
    full_path = '{}{}'.format(file_path, filename)
    urllib.request.urlretrieve(url, full_path)

    print('{} saved.'.format(filename))


    return None 

# ----------------------------------------------------------------

# Set Constants

FILENAME = 'links.csv'
FILE_PATH = 'images/'

# Read list of URLs as Pandas DataFrame
urls = pd.read_csv(FILENAME)

# Save Images to the Directory by iterating through the list
for i, url in enumerate(urls.values):
      url_to_jpg(i, url[0], FILE_PATH)

