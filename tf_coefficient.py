from bs4 import BeautifulSoup
from collections import Counter

def  coefficient_tf(segmentedCorpusFile: str) -> Counter:
   # Fonction qui calcule le coefficient tf pour chaque mot dans le corpus segmenté
   result = []
   with open(segmentedCorpusFile , 'r' , encoding='utf-8') as fp:
        word_counts = Counter()
        for line in fp:
            line = line.strip()
            if line : # Evitemement des lignes vides
               parts = line.split("\t")
               if len(parts) == 2:
                  word, id_doc = parts
                  word_counts[word,id_doc] += 1  # Compte des occurences
            
   return word_counts 

def write_coefficient_tf(tf_counts: Counter, outputFile: str):
    with open(outputFile, "w", encoding="utf-8") as f:
        f.write("id_doc\tmot\ttfi\n")
        for (word, id_doc), count in tf_counts.items():
            f.write(f"{id_doc}\t{word}\t{count}\n")


segmentedCorpusFile = "output/test2.txt"
outputFile = "output/resulat_tf.txt"

tf_counts = coefficient_tf(segmentedCorpusFile)
write_coefficient_tf(tf_counts, outputFile)


