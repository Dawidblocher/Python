upper_case_letter = {
  'А': 'A',
  'Б': 'B',
  'В': 	'V', 
  'Г': 	'G', 	
  'Д':  'D', 	
  'Е':	'E', 	
  'Ё': 	'Ё', 
  'Ж': 	'Ž', 
  'З': 	'Z', 
  'И': 	'I', 	
  'Й': 	'J', 	
  'К': 	'K',	
  'Л': 	'L', 
  'М': 	'M', 	
  'Н': 	'N', 
  'О': 	'O', 
  'П': 	'P', 
  'Р': 	'R', 
  'С': 	'S', 	
  'Т': 	'T', 
  'У': 	'U', 
  'Ф': 	'F', 	
  'Х': 	'H', 	
  'Ц': 	'C', 	
  'Ч':	'Č' ,	
  'Ш': 	'Š', 	
  'Щ': 	'Ŝ' ,	
  'Ъ': 	'″' ,
  'Ы': 	'Y' ,	
  'Ь':	'′' ,	
  'Э': 	'È' ,
  'Ю': 	'Û' ,
  'Я': 	'Â' ,	
  '’':   '’'
}

lower_case_letter = {
   'а':	 'a'	,
   'б':	 'b'	,
   'в':	 'v',
   'г':	 'g',	
   'д':	 'd',	
   'е':	 'e',	
   'ё':	 'ё',	
   'ж':	 'ž',
   'з':	 'z',	
   'и':	 'i',	
   'й':	 'j',	
   'к':	 'k',	
   'л':	 'l',	
   'м':	 'm',	
   'н':	 'n',	
   'о':	 'o',	
   'п':	 'p',	
   'р':	 'r',	
   'с':	 's',	
   'т':	 't',	
   'у':	 'u',	
   'ф':	 'f',	
   'х':	 'h',	
   'ц':	 'c',	
   'ч':	 'č',	
   'ш':	 'š',	
   'щ':	 'ŝ',
   'ъ':	  '″',	
   'ы':	 'y'	,
   'ь':	  '′'	,
   'э':	 'è',
   'ю':	 'û',
   'я':	 'â'	
}

def translChar(char):
  if char in upper_case_letter.keys():
    char = upper_case_letter[char]
  elif char in lower_case_letter.keys():
    char = lower_case_letter[char] 
  else:
    char = char
  return char 

def translText(text):
  transl = ''
  for l in text:
    transl = transl + translChar(l)
  return transl  

input_file  = open('input.txt', 'r', encoding="utf-8")
output_file = open('output.txt', 'w')

translText = translText(input_file.read())
output_file.write(translText)

input_file.close()
output_file.close()

 
    

