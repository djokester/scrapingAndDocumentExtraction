import csv
import pandas as pd
features_list = []
sentences = []
fnames = ["file-andhe_ki_lathi-1507111038.dat", "file-doli_banaam_arthi.dat", "file-katl_e_bayan-1507111042.dat", "file-khadi_ka_kurtha-0807112238.dat", "file-kiraye_ka_ghar-1507111043.dat", "file-mouth_ka_saudagar-1507111034.dat", "file-parithyaag-0707111503.dat", "file-rishthey_ka_dhaag-0807112232.dat", "file-rishthey_ka_dhaag-0807112232.dat", "file-sapna-0707111503.dat", "file-tyaag-1507111040.dat", "file-udhaar-0707111504.dat", "file-yes-sir-0707111505.dat"]
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