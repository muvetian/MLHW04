import numpy as np
import pandas as pd
import ast
import os
import glob, os
import gzip
import shutil
import json
def decompress():
    print "Decompressing."
    os.chdir("/Users/kyle/Documents/2018/CSC371MachineLearning/hw04/opoint/2018/03/01")

    for file in glob.glob("*.gz"):
        with gzip.open(file, 'rb') as f_in:
            with open(file[:-3], 'wb') as f_out:
                print "."
                shutil.copyfileobj(f_in, f_out)
    print "Done"
def main():
    all_moment = pd.read_csv("data_drop_w_momentum.csv")
    all_opoint = all_moment.loc[all_moment['feed_source'] == 'opoint']
    os.chdir("/Users/kyle/Documents/2018/CSC371MachineLearning/hw04/opoint/2018/03/01")
    i = 0

    # lst_str = []
    # test = all_opoint.loc[all_opoint['feed_article_id'] == '550_3006626']
    # print test
    # for file in glob.glob("*.json.xml"):
    #     with open(file) as f:
    #         # print file
    #         try:
    #             json_parsed = json.load(f)
    #             document_count = json_parsed["searchresult"]["documents"]
    #             if (document_count != 0):
    #                 for i in range(document_count):
    #                     feed_article_id_str = str(json_parsed["searchresult"]["document"][i]["id_site"]) + "_" +  str(json_parsed["searchresult"]["document"][i]["id_article"])
    #                     if((all_opoint['feed_article_id'] == feed_article_id_str).any()):
    #                         print file+":"+feed_article_id_str
    #                         lst_str.append(file+":"+feed_article_id_str)
    #             else:
    #                 print "0\n";
    #         except ValueError:
    #             print 'Decoding JSON has failed'
    # print lst_str
    # for item in lst_str:
    #     with open("file_lookup.txt", "w") as text_file:
    #         text_file.write(item)
    #         text_file.write('\n')




    # print all_opoint
if __name__ == "__main__":
    main()
