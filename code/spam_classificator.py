import pandas as pd
import pickle
import string
import nltk
import spacy
import json

nltk.download('stopwords')
nltk.download('punkt')
stopwords = nltk.corpus.stopwords.words('portuguese')

original_file = pd.read_csv('../data/Data_Test.csv')
df = original_file.copy()

with open('../model/spacy.pkl', 'rb') as f:
    spc = pickle.load(f)

with open('../model/commom_spam_words.pkl', 'rb') as f:
    dict_freq_words = pickle.load(f)


def normalize_text(text):
    nopunc = [char for char in text if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    return ' '.join([word for word in nopunc.split() if word.lower() not in stopwords])


def freqUpper(text):
    uppers = [char for char in text if char.isupper()]
    return len(uppers)


def get_most_commom_spam_words(message):
    values = []
    dict_top_spam_words = {}
    for word in message:
        values.extend([item[0] for item in dict_freq_words if word in item])
    for value in values:
        try:
            dict_top_spam_words[value] += 1
        except:
            dict_top_spam_words[value] = 1
    return dict_top_spam_words


def get_pos(message):
    doc = spc(message)
    dict_pos = {}
    for token in doc:
        try:
            dict_pos[token.pos_] += 1
        except:
            dict_pos[token.pos_] = 1
    return dict_pos


df['Message_Norm'] = df['Message'].apply(normalize_text)
df['Message_Tokens'] = df['Message'].apply(nltk.tokenize.word_tokenize)
df['len'] = df['Message'].apply(len)
df['freq_uppers'] = df['Message_Norm'].apply(freqUpper)
df['dict_commom_spam'] = df['Message_Tokens'].apply(get_most_commom_spam_words)
df['dict_pos'] = df['Message'].apply(get_pos)
df['dict_pos'] = df['dict_pos'].apply(lambda x: str(x).replace(
    '\'', '"').replace('None', '0').replace('True', '1').replace('False', '0'))
df_pos = df['dict_pos'].apply(json.loads).apply(pd.Series).fillna(0)
df = pd.concat([df, df_pos], axis=1)
df['len_tokens'] = df['Message_Tokens'].apply(len)
with open('../model/numeric_columns.pkl', 'rb') as f:
    numeric_columns = pickle.load(f)

for column in numeric_columns:
    df[column] = (df[column] / df['len_tokens']) * 100

df['len_common_spam_words'] = df['dict_commom_spam'].apply(
    lambda x: sum(x.values()))
df['pct_common_spam_words'] = (
    df['len_common_spam_words'] / df['len_tokens']) * 100

with open('../model/used_columns.pkl', 'rb') as f:
    used_columns = pickle.load(f)

with open('../model/std_transform.pkl', 'rb') as f:
    std_transform = pickle.load(f)

with open('../model/spam_tree.pkl', 'rb') as f:
    spam_tree = pickle.load(f)

df = df[used_columns]
df_scaled = std_transform.transform(df)
spam = spam_tree.predict(df_scaled)
original_file['SPAM'] = spam
original_file['SPAM'] = original_file['SPAM'].map({1: True, 0: False})
original_file.to_csv('../data/Data_Tagged.csv')
