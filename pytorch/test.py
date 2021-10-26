import glob

directory = 'pytorch/IMDB Data/test'
for filename in glob.glob(str(directory)+'/neg/*.txt'):
        with open(filename, 'r',  encoding="utf8") as f:
            print(filename.split('_')[0].split('/')[-3])