import os
import pandas as pd
fnames = []
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    if(f.split(".")[len(f.split("."))-1]=="dat"):
        fnames.append(str(f))
features_list = []
sentences = []        
for fname in fnames:
    file = open(fname, 'r')
    string = file.read()
    string_list = string.split("\n")
    words = []
    chunkTypes = []
    chunkIDs = []
    posTags = []
    for string in string_list:
        if(string!='' and string.split("\t")[1]!="NULL"):
            features = []
            components = string.split("\t")
            features.append(components[1]) #word
            words.append(components[1])
            features.append(components[2]) #lemma
            features.append(components[3]) #basic pos tag
            features.append(components[4]) #advanced pos tag
            posTags.append(components[4])
            tags = components[5].split("|") #this we need to decipher
            gender = tags[1].split("-")[1]
            if(gender==''):
                gender = "-"
            features.append(gender) #gender
            num = tags[2].split("-")[1]
            if(num==''):
                num = "-"
            features.append(num) #singularity 
            pers = tags[3].split("-")[1]
            if(pers==''):
                pers = "-"
            features.append(pers) #person 
            derivation = tags[5].split("-")[1]
            if(derivation==''):
                derivation = "-"
            features.append(derivation) #this feature describes how the word-form is derived
            chunkID = tags[7].split("-")[1]
            if(chunkID==''):
                chunkID = "-"
            chunkIDs.append(chunkID)
            chunkType = tags[8].split("-")[1]
            if(chunkType==''):
                chunkType = "-"
            chunkTypes.append(chunkType)
        
        if(string=='' and "".join(words)!=""):
            sentences.append([" ".join(words)," ".join(posTags)," ".join(chunkIDs), " ".join(chunkTypes)])
            words = []
            chunkTypes = []
            chunkIDs = []
            posTags = []
        features_list.append(features)           

feature_head = ["token", "lemma", "basic_pos_tag", "advanced_pos_tag", "gender", "singularity", "person", "derivation"]
sents_head = ["sentence", "pos_tags", "chunk_id", "chunk_type"]        
feature = pd.DataFrame(features_list, columns = feature_head)
sentence = pd.DataFrame(sentences, columns = sents_head)
sentence.dropna(how='any')

feature.to_csv("feature.csv")

sentence.to_csv("sentences.csv")