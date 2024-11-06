from PIL import Image
import os
import pytesseract
counter = 0
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" 
for filename in os.listdir('dictionary/'):
    with open(os.path.join(os.getcwd()+'\\dictionary\\'+filename), 'r', encoding="utf-8") as f: 
        dictionary = open('dictionarytxt/'+f'dictionary{counter}.txt', 'w', encoding="utf-8")
        dictionary.write(f'{pytesseract.image_to_string(Image.open('dictionary/'+filename), lang='kaz')}' + '\n')
        dictionary.write('---------------\n')
        counter += 1
        print('Ай сигма, добавилось столько страниц: '+ str(counter))