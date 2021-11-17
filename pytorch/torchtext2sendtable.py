# import datasets
import string
import re
from nltk.tokenize import sent_tokenize

def torchtext2nltkMLE(train_iter, firstn):
    send_list = []
    for i, [label,line] in enumerate(train_iter):
        if i > firstn:
            break
        line = re.sub('<[^<]+?>|\"', '', line)
        sent = sentence_token_nltk(line)
        for msent in sent:
            msent = msent.lower()
            msent = re.sub('<[^<]+?>|\"|_|,', '', msent)
            msent = re.sub('\?|!|:|\.{2,}', '.', msent)
            msent = re.sub('\.{2,}','.',msent)
            msent = re.sub('\([^\)]+\)', ' ', msent)
            sent_list = msent.split('.')
            sent_list = [item for item in filter(lambda x:x != '', sent_list)]
            send_list += sent_list
    send_table = []
    for sent in send_list:
        word_list = []
        for word in sent.split(' '):
            word_list.append(word)
        word_list = [item for item in filter(lambda x:x != '', word_list)]
        send_table.append(word_list)
    return send_table

def tokenize(label, line):
    return line.split()

def sentence_token_nltk(str):
    sent_tokenize_list = sent_tokenize(str)
    return sent_tokenize_list