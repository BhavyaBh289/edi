import smart_search
from gensim import *
functioncaller = smart_search.model()
pdf_list = functioncaller.getting_list_of_words('./IPC.pdf')
print("done")
print(pdf_list)
location[0:5] = functioncaller.perform_skip(pdf_list, servant)
