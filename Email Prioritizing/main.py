import pandas as pd
import sklearn
import csv
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import numpy

STOP = set(stopwords.words('english'))
words = pd.read_csv('./Data/U_Keyword_Dataset.txt', sep='/n', quoting=csv.QUOTE_NONE,
                    names=["Urgency_Keywords"])  # csv comma seperated value
words = words['Urgency_Keywords'].values  # to numpy
words = words.tolist()  # to list


ps = PorterStemmer()


def SplitIntoWords(message): return TextBlob(message.lower()).words


def WordsIntoBaseForm(message):
    return [ps.stem(word) for word in SplitIntoWords(message)]


sub_str = "Its urgently work please reply quick"
sub_str = WordsIntoBaseForm(sub_str)


count = 0
for sub_sub_str in sub_str:
    if sub_sub_str in words:
        count += 1
print(count)
