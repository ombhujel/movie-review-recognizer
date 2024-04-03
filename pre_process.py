
import os
import string
import json
from collections import Counter
os.getcwd()

train_folder_positive = os.path.join(os.getcwd(), 'train\lpos')
train_folder_negative = os.path.join(os.getcwd(), 'train\lneg')
test_folder_positive = os.path.join(os.getcwd(), 'test\lpos')
test_folder_negative = os.path.join(os.getcwd(), 'test\lneg')


most_Fren = open("_training_vocabulary_.txt" , "w", encoding="utf-8")
most_Fren.close()
mos_Fren = open("_test_vocabulary_.txt" , "w", encoding="utf-8")
mos_Fren.close()


most_Freq__train = open("_training_vocabulary_.txt" , "r+", encoding="utf-8")
training_file_path = "_training_vocabulary_.txt"
output_file_train_pos_100 = open("output_file_pos_100.txt", "w", encoding="utf-8")
output_file_train_neg_100= open("output_file_neg_100.txt", "w", encoding="utf-8")
output_file_train_pos_10 = open("output_file_pos_10.txt", "w", encoding="utf-8")
output_file_train_neg_10= open("output_file_neg_10.txt", "w", encoding="utf-8")
output_file_train_pos_300 = open("output_file_pos_300.txt", "w", encoding="utf-8")
output_file_train_neg_300= open("output_file_neg_300.txt", "w", encoding="utf-8")

most_Freq_test = open("_test_vocabulary_.txt" , "r+", encoding="utf-8")
test_file_path = "_test_vocabulary_.txt"
output_file_test_100 = open("output_file_test_100.txt", "w", encoding="utf-8")
output_file_test_10 = open("output_file_test_10.txt", "w", encoding="utf-8")
output_file_test_300 = open("output_file_test_300.txt", "w", encoding="utf-8")


num_10 = 10
num_100 = 100
num_300 = 300
vocab_10 = []
vocab_100 = []
vocab_300 = []


all_stopwords = ['your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 
                "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 
                'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 
                "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
                'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and',
                'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'i','to','in','br',
                'for','on', 'with', 'film', 'movie', 'you', 'by','from', 'there','when','my','movies',
                's', ' ', 'not', '', 'one', 'all', 'so', 'just', 'about', 'out', 'some', 'very', 'even', 'up', 'would', 'only', 'time', 'really', 'story', 'see', 'can', 'me', 'than', 'we', 'much', 'well', 'get', 'will', 'into', 'also', 'other', 'people', 'first', 'how', 'most', 'dont', 'made', 'then', 'make', 'films', 'could', 'any', 'too', 'after', 'characters', 'think', 'watch', 'two', 'many', 'seen', 'character', 'acting', 'where', 'plot', 'love', 'know', 'life', 'show', 'ever', 'still', 'over', 'off', 'end', 'say', 'here', 'man', 'why', 'scene', 'such', 'scenes', 'go', 'should', 'something', 'through', 'im', 'back', 'real', 'watching', 'years', 'though', 'now', 'thing', 'actors', 'another', 'new', 'before', 'actually', 'makes','', 'nothing', 'find', 'look', 'few', 'lot', 'part', 'want', 'pretty', 'down', 'horror', 'thought', 'series', 'right', 'almost', 'point', 'must', 'family', 
 'kind', 'yet', 'away', 'sure', 'tv', 'making', 'woman', 'going', 'every', 'work', 'us', 's', 'director', 'thats', 'things', 'cast', 'around', 'seems', 'take', 'both' , 'give', 'may', 'between', 'ive', 'girl', 'each','own', 'gets', 'saw','come', 'times','theres','role','whole', 'dome', 'music', 'script', 'hes','guy','minutes', 'feel','performance','girl','each', 'found','played','anyone','our','comes', 'course', 'trying', 'hoes','day','looks','shows', 'put', 'place','book','once','set','main','reason','sense','everything','looking','true','ending','someone','plays','actor', 'seem', 'three', 'dvd', 'said','takes','young','got','world','big','screen','together','play','john','during','later','effects','seeing','audience','house','american','idea','wife','youre','read','year','second','used','given','father','use','rest','men','performances']


#So far, we have imported os library, to go through all the text file one by one, which is defined in
#the first four line below, then, using the string library, we remove the punctuations and at the same
#time, we lowercase all of them, and finally assemble them all together and write in the file, all this
#is under the function name stemming which takes two parameters, and they are, the path to the text file
#which needs to be stemmed and the file where we want to write the stemmed data.
#we pass the path to the file we want to read in path parameter and parameter fill_file is the file we want to write

def stemming(path, fill_file):
    for root, folders, files in os.walk(path):
        for file in files:
            path = os.path.join(root, file)
            with open(path, encoding="utf-8") as inf:
                text = inf.read()
                words = text.lower().split()
                table = str.maketrans("", "", string.punctuation)
                no_punctuation = [w.translate(table) for w in words]
                #print(no_punctuation)
                no_Sw = [word for word in no_punctuation if not word in all_stopwords]
                attach_again = " ".join(no_Sw)
                #attach_again = " ".join(no_punctuation)
                fill_file.write(attach_again +" ")


#So, the function "most_frequency", basically on the surface returns the words with most frequency, i.e given the parameters, 
#the first one "path" which is path to the file you want to read, the second one "num" which is starting from the 
#most frequent how many words you want 10, 20, 100, and the final one "arr", which stores the most frequent word in 
#ascending order, i.e from most frequent and lower.

def most_frequency(path, num, arr):
    with open(path, 'r', encoding="utf-8") as f:
        text = f.read()
    words = [w.strip('!,.?12 34567890-=@#$%^&*()_+ ') for w in text.lower().split()]
    counter = Counter(words)
    #print(json.dumps(counter.most_common()))
    
    a = json.dumps(counter.most_common())
    b = 0
    for key in json.loads(a):
        b = b + 1
        if(b==num+1):
            break
        k = str(key)
        k=k.replace("[","")
        k=k.replace("]","")
        k=k.replace("'","")
        k=k.replace("0","")
        k=k.replace("1","")
        k=k.replace("2","")
        k=k.replace("3","")
        k=k.replace("4","")
        k=k.replace("5","")
        k=k.replace("6","")
        k=k.replace("7","")
        k=k.replace("8","")
        k=k.replace("9","")
        k=k.replace(",","")
        k=k.replace(" ", "")
        if(k == ' '):
            b=b-1
            continue
        if(k == ''):
            b=b-1
            continue
        
        arr.append(k)



# Basically here, the first part of this is similar to the stemming we did earlier, which removes the punctuations,
# and after forming each review in a list of words, and then is the difference, it compares that list with the list 
# of top most frequent words we came up with function mpst_frequency above, and came up with the vector ready to be
# inputted in the LR model.
"""
def converting_to_vector(path, f, array, type):
    for root, folders, files in os.walk(path):
        for file in files:
            path = os.path.join(root, file)
            with open(path, encoding="utf-8") as inf:
                text = inf.read()
                words = text.lower().split()
                table = str.maketrans("", "", string.punctuation)
                no_punctuation = [w.translate(table) for w in words]
                if(type == 1):
                    f.write("1 ")
                else:
                    f.write("0 ")
                flag = 0
                for x in array:
                    for y in no_punctuation:
                        flag = 0
                        if(x == y):
                            f.write("1 ")
                            flag = 1
                            break
                    if(flag != 1):
                        f.write("0 ")
                f.write('\n')
"""
def converting_to_vector(path, f, array, type):
    for root, folders, files in os.walk(path):
        for file in files:
            path = os.path.join(root, file)
            with open(path, encoding="utf-8") as inf:
                text = inf.read()
                words = text.lower().split()
                table = str.maketrans("", "", string.punctuation)
                no_punctuation = [w.translate(table) for w in words]
                if(type == 1):
                    f.write("1 ")
                else:
                    f.write("0 ")
                flag = 0
                for x in array:
                    for y in no_punctuation:
                        flag = 0
                        if(x == y):
                            f.write("1 ")
                            flag = 1
                            break
                    if(flag != 1):
                        f.write("0 ")
                f.write('\n')


# Removing the punctuations and stopwords from all of the training and tests, positive and 
# negative reviews

stemming(train_folder_positive,most_Freq__train )
stemming(train_folder_negative, most_Freq__train )

stemming(test_folder_positive,most_Freq_test )
stemming(test_folder_negative, most_Freq_test )

most_Freq__train.close()
most_Freq_test.close()



# Initializing appropriate functions to extract the most common words after
# for both size of length 10 and 100 and storing it in the respective 
# lists for later use, in forming input vector.
most_frequency(training_file_path, num_100, vocab_100)
most_frequency(training_file_path, num_10, vocab_10)
most_frequency(training_file_path, num_300, vocab_300)


print(vocab_300)
print(vocab_100)
print(vocab_10)


# Initializing appropriate function to convert the input review in the size of 10 and 100


converting_to_vector(train_folder_negative, output_file_train_neg_100, vocab_100, 0)
converting_to_vector(train_folder_positive, output_file_train_pos_100, vocab_100, 1)

converting_to_vector(train_folder_negative, output_file_train_neg_10, vocab_10, 0)
converting_to_vector(train_folder_positive, output_file_train_pos_10, vocab_10, 1)

converting_to_vector(train_folder_negative, output_file_train_neg_300, vocab_300, 0)
converting_to_vector(train_folder_positive, output_file_train_pos_300, vocab_300, 1)




converting_to_vector(test_folder_positive, output_file_test_100, vocab_100, 1)
converting_to_vector(test_folder_negative, output_file_test_100, vocab_100, 0)
converting_to_vector(test_folder_positive, output_file_test_10, vocab_10, 1)
converting_to_vector(test_folder_negative, output_file_test_10, vocab_10, 0)
converting_to_vector(test_folder_positive, output_file_test_300, vocab_300, 1)
converting_to_vector(test_folder_negative, output_file_test_300, vocab_300, 0)


output_file_train_pos_100.close()
output_file_train_neg_100.close()
output_file_train_pos_10.close()
output_file_train_neg_10.close()
output_file_train_pos_300.close()
output_file_train_neg_300.close()

output_file_test_100.close()


print("All the required actions in pre_process.py are completed!")
