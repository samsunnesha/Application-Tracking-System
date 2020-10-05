import docx2txt
#load the resume of applicant
resume = docx2txt.process("resume_file_name.docx")
#print the resume
print(resume)
#load the job description
job_desc = docx2txt.process("job_description.docx")
#print the job dscription
print(job_desc)
#list of text to store resume and job description
text = [resume,job_desc]
from sklearn.feature_extraction.text import CountVectorizer
cu = CountVectorizer()
count_matrix = cv.fit_transform(text)
from sklearn.metrics.pairwise.import cosine_similarity
print(cosine_similarity(count_matrix))
match = cosine_similarity(count_matrix)[0][1]
match = match*100
match = round(match,2)
print(match)   **you will get match in percentage

if(match>60):
print("Congratulations! Your Application has been accepted")
else:
print("Sorry! Your Application has been rejected")
