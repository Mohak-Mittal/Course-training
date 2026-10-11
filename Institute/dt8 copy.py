import re
text = "hi i am mohak and  i am a student " 
patt = r"\w{3,7}"
print(re.findall(patt ,text))