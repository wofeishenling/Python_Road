import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def show_cor_of(info_table,x,y,z,sortkey=''):
    if(sortkey!=''):
        info_table.sort_values(by=sortkey,ascending='',inplace=True)
    size = info_table.index.size
    p_list = np.linspace(1,0,int(11))
    cor_list = []
    cor_list.append([])
    cor_list.append([])
    for p in p_list:
        print(p)
        #spearman correlation coefficient
        #原始数据
        X1= info_table[x][:int(p*size)]
        Y1= info_table[y][:int(p*size)]
        Z1= info_table[z][:int(p*size)]
        #s.corr()函数计算
        r=X1.corr(Y1,method='spearman')
        q=X1.corr(Z1,method='spearman')
        cor_list[0].append(r)
        cor_list[1].append(q)
        print("corelationship of len and averge_content: %f",r)
        print("corelationship of len and freq: %f",q)
    x1 = p_list
    y1 = cor_list[0]
    y2 = cor_list[1]
    plt.xlabel("persent%")
    plt.ylabel("correlationship")
    plt.plot(x1,y1)
    plt.plot(x1,y2)
    plt.show()
    plt.savefig('./cor_diff_rank.jpg', bbox_inches='tight', dpi=300)