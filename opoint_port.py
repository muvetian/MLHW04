import numpy as np
import pandas as pd
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
    lst_str = []
    for file in glob.glob("*.json.xml"):
        with open(file) as f:
            print file
            try:
                json_parsed = json.load(f)
                if (json_parsed["searchresult"]["documents"] != 0):
                    feed_article_id_str = str(json_parsed["searchresult"]["document"][0]["id_site"]) + "_" +  str(json_parsed["searchresult"]["document"][0]["id_article"])
                    if((all_opoint['feed_article_id'] == feed_article_id_str).any()):
                        lst_str.append(file+":"+feed_article_id_str)
            except ValueError:
                print 'Decoding JSON has failed'



    print list_str


    # print all_opoint
if __name__ == "__main__":
    main()
