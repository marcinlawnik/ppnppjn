# Zadanie 1: Ściągnij, rozpakuj i załaduj korpus do nltk.
# http://bachan.speechlabs.pl/files/Zal_korpus_01.zip

import urllib.request
import zipfile
from os.path import exists

url = 'http://bachan.speechlabs.pl/files/'
filename = 'Zal_korpus_01.zip'

if not exists(filename):
    print("Downloading " + filename)
    filehandle, _ = urllib.request.urlretrieve(url + filename, filename)
    zip_file_object = zipfile.ZipFile(filehandle, 'r')
    zip_file_object.extractall()
else:
    print(filename + " already downloaded")
