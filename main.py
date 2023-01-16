import os
from gtts import gTTS
from art import tprint
import pdfplumber
from pathlib import Path



def pdf_to_mp3(file_path='путь к pdf файлу', language='en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf' or 'txt':

        print(f'[+] Original file: {Path(file_path).name}')
        print('[+] Processing...')
        #return 'File exists'
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
                pages = [page.extract_text() for page in pdf.pages]
        text = ''.join(pages)

        text = text.replace('\n', '')
        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        # my_audio.save(f'{file_name}.mp3')
        my_audio.save("%s.mp3" % os.path.join(Path(file_path).parent, file_name))
    else:
        return 'File not exists, check the file path'


def main():
    tprint('PDF>>TO>>MP3', font='bulbhead')
    file_path = input(r"Enter a file's path: ")
    language = input(r"Choose language, for example 'en' or 'ru': ")
    print(pdf_to_mp3(file_path=file_path, language=language))


if __name__ == '__main__':
    main()
