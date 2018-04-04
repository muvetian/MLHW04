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
    # os.chdir("/Users/kyle/Documents/2018/CSC371MachineLearning/hw04/opoint/2018/03/01")
    i = 0
    look_up_dic = []
    print all_opoint.shape
    with open("file_lookup_fr_term.txt", "r") as text_file:
        data = text_file.read().replace('\n', '')

                # x = [n.strip() for n in x]

    test = all_opoint.loc[all_opoint['feed_article_id'] == '118204_197482']
    look_up_dic = ast.literal_eval(data)
    # print len(look_up_dic)

    # ----------
    columns = ['title','text','moment_score']

    os.chdir("/Users/kyle/Documents/2018/CSC371MachineLearning/hw04/opoint/2018/03/01")
    data = pd.DataFrame(columns = columns)
    for i in range(len(look_up_dic)):
        with open(look_up_dic[i].split(":")[0]) as f:
            json_parsed = json.load(f)
            text = json_parsed["searchresult"]["document"][int(look_up_dic[i].split(":")[1])]["body"]["text"]
            row = all_opoint.loc[all_opoint['feed_article_id'] == look_up_dic[i].split(":")[2]]
            title = row["title"].values[0]
            mmnt_scr = row["momentum"].values[0]
            # print "Title:" + title + "|||| Momentum Score:" + str(mmnt_scr)
            data.loc[i] = [title,text,mmnt_scr]
    # data.loc[0] = ["sadsad",1230]
    print data
    os.chdir("/Users/kyle/Documents/2018/CSC371MachineLearning/hw04/opoint/")
    data.to_pickle("textaggregate.pkl")
    # ---------
    # df = pd.read_pickle("textaggregate.pkl")
    # print df.loc[0]["text"]
    # ---------
    # data.append({'text': "asd",'moment_score':10}, ignore_index=True)

    # print test
    # count = 0;
    # os.chdir("/Users/kyle/Documents/2018/CSC371MachineLearning/hw04/opoint/2018/03/01")
    # for file in glob.glob("*.json.xml"):
    #     count += 1;
    # print (count)
    # lst_str = []
    test = all_opoint.loc[all_opoint['feed_article_id'] == '550_3006626']

    print test["momentum"].values[0]
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
    #                         print file+":"+ str(i) +":"+feed_article_id_str
    #                         lst_str.append(file+":"+ str(i) +":"+feed_article_id_str)
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
