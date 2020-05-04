## nltk.download() script is broken; manually pull in required folders from http://www.nltk.org/nltk_data/ into 'nltk_data' folder in home directory

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.corpus import state_union ## state of the union addresses from various presidents
from nltk.tokenize import PunktSentenceTokenizer    ## unsupervised machine learning tokenizer that you can train if you want, but it comes pre-trained

#################
#               #
# Tokenizers    #
#               #
#################

## Two different tokenizers: one that splits by words and one that splits by sentence

example_text = "Hello Mr. Smith, how are you doing today? The weather is great and Python is awesome. The sky is pinkish blue. You should not eat cardboard."

## Now there's something important to consider about this example_text
## Spliting by sentence won't be as easy as just splitting by (. ? !),
## because of the 'Mr. Smith".
## You could use regular expressions to split by sentence and then split by words,
## however, there's a better option using tokenizers
## NLTK is very powerful and can be used to save LOTS of time writing regular expressions

print(sent_tokenize(example_text))

## Output: ['Hello Mr. Smith, how are you doing today?', 'The weather is great and Python is awesome.', 'The sky is pinkish blue.', 'You should not eat cardboard.']
## As seen here, the sent_tokenizer 

print(word_tokenize(example_text))

## Output: ['Hello', 'Mr.', 'Smith', ',', 'how', 'are', 'you', 'doing', 'today', '?', 'The', 'weather', 'is', 'great', 'and', 'Python', 'is', 'awesome', '.', 'The', 'sky', 'is', 'pinkish', 'blue', '.', 'You', 'should', 'not', 'eat', 'cardboard', '.']
## This is interesting because it did not consider the 'Mr.' to be two words, but considers other punctuation to be a separate word.
## This is because word_tokenize recognizes punctuation as it's own word, by default, but you can change this

#################
#               #
# Stopwords     #
#               #
#################

example_sentence = "This is an example showing off stopword filtration"
stop_words = set(stopwords.words("english"))
## The stopwords we will be using are defined as the set of stopwords in the english language predefined by NLTK
## You can also add your own words by appending them onto stop_words
## These stop words will be used to filter the sentence, and pull out only important words

print(stop_words)
words = word_tokenize(example_sentence)
filtered_sentence = []
for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)

print(filtered_sentence)

## This is the manual code for filtering a sentence with stopwords, but there's also a one-liner in NLTK 
## that you can use for the same purpose, and it's cleaner

clean_filtered_sentence = [w for w in words if not w in stop_words]
print(clean_filtered_sentence)


## The following could also work, but the output set is in reverse order
filtered_sentence =  set(word_tokenize(example_sentence)) - set(stopwords.words("english"))
print(filtered_sentence)

#################
#               #
# Stemming      #
#               #
#################

ps = PorterStemmer()
example_words = ["python", "pythoner", "pythoning", "pythoned", "pythonly"]

for word in example_words:
    print(ps.stem(word))

new_text = "It is very important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."
words = word_tokenize(new_text)
stemmed_words = []
for word in words:
    stemmed_words.append(ps.stem(word))

print(stemmed_words)

###########################
#                         #
# Part of Speech Tagging  #
#                         #
###########################

## here we want to use the sample text 'state_union'

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")
custom_sent_tokenizer = PunktSentenceTokenizer(train_text) ## initializing the tokenizer by training the tokenizer on a train_text
tokenized = custom_sent_tokenizer.tokenize(sample_text)    ## using trained tokenizer on sample_text

def process_content():
    try:
        for i in tokenized:  ## for each word in tokenized list
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)
    
    except Exception as e:
        print(str(e))

process_content()

## when part of speech tagging is done in this way, tuples are created of the (word, part_of_speech)