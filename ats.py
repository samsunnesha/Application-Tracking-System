import doc2txt

resume = doc2txt.process("MounicaCV3.doc")
print(resume)
job_desc=doc2txt.process("job_desc.txt")
print(job_desc)

text=[resume,job_desc]

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
count_matrix = cv.fit_transform(text)

from sklearn.metrics.pairwise import cosine_similarity
print(cosine similarity(count_matrix))

match = cosine_similarity(count_matrix)[0][1]
match = match*100
match = round(match,2)
print(match)

if(match>60):
    print("Congratulations! Your Application has been accepted")
else:
    print("Sorry!Your Application has been rejected")    
