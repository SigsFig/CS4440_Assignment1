# -------------------------------------------------------------------------
# AUTHOR: Nicholas Hoang
# FILENAME: similarity.py
# SPECIFICATION: Given a CSV file of document data, computes the cosine similarity between the documents and their words. Returns the two most similar documents based on the cosine similarity score.
# FOR: CS 4440 (Data Mining) - Assignment #1
# TIME SPENT: 2 hours
# -----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH
#AS numpy or pandas.
#You have to work here only with standard dictionaries, lists, and arrays
# Importing some Python libraries
import csv
from sklearn.metrics.pairwise import cosine_similarity

documents = []

#reading the documents in a csv file
with open('cleaned_documents.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            documents.append (row)

#Building the document-term matrix by using binary encoding.
#You must identify each distinct word in the collection using the whibbte space as your character delimiter.
#--> add your Python code here
docTermMatrix = []

# Build a vocabulary by splitting on whitespace (lowercased)
vocab_set = set()
doc_tokens = []  # list of token lists for each document

for row in documents:
    # join columns into one text (in case text spans multiple columns)
    text = " ".join(row).strip()
    # split on whitespace and lowercase tokens (per instruction)
    tokens = [tok.lower() for tok in text.split() if tok.strip() != ""]
    doc_tokens.append(tokens)
    for t in tokens:
        vocab_set.add(t)

# fixed ordering of terms
vocab = sorted(vocab_set)

# build binary document-term matrix (list of lists)
for tokens in doc_tokens:
    token_set = set(tokens)
    row_vec = [1 if term in token_set else 0 for term in vocab]
    docTermMatrix.append(row_vec)


# Compare the pairwise cosine similarities and store the highest one
# Use cosine_similarity([X], [Y]) to calculate the similarities between 2 vectors
# --> Add your Python code here
if len(docTermMatrix) < 2:
    print("Need at least two documents to compute similarity.")
else:
    max_sim = -1.0
    max_i = None
    max_j = None
    n = len(docTermMatrix)
    for i in range(n):
        for j in range(i + 1, n):
            sim = cosine_similarity([docTermMatrix[i]], [docTermMatrix[j]])[0][0]
            if sim > max_sim:
                max_sim = sim
                max_i = i
                max_j = j

    # Print the highest cosine similarity following the information below
    # The most similar documents are document 10 and document 100 with cosine
    # similarity = x
    # --> Add your Python code here
    if max_i is not None and max_j is not None:
        # documents list corresponds to CSV data rows after header; use 1-based indexing
        print(f"The most similar documents are document {max_i+1} and document {max_j+1} with cosine similarity = {max_sim:.4f}")
    else:
        print("Could not determine the most similar documents.")
