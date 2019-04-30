import nltk
from nltk import tokenize


file1 = open("text.en","r") 
string = file1.read() 
file1.close()

string = string.replace('\n\n','\n')
string = string.replace('\n\n','\n')
string = string.replace('\n\n', '\n')
string = string.replace('\n', ' ')

try:
	output=tokenize.sent_tokenize(string)
except LookupError:
	nltk.download('punkt')
	output=tokenize.sent_tokenize(string)	


with open("text_lines.en","w") as f:
	f.writelines("%s\n" % l for l in output) 
f.close()
