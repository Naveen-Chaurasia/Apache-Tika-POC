
# import parser object from tike
from tika import parser  
  
# opening pdf file
parsed_pdf = parser.from_file("W461C103_R0_Air Heater Mtg bracket.doc")
  
# saving content of pdf
# you can also bring text only, by parsed_pdf['text'] 
# parsed_pdf['content'] returns string 
data = parsed_pdf['content'] 
#data = parsed_pdf['metadata']
#data = parsed_pdf['status']
  
  
# Printing of content 
print("********************************")
print(data)
print("********************************")  
# <class 'str'>
print(type(data))
