from gtts import gTTS
import os
from deep_translator import GoogleTranslator

translations = []

# Создайте папку для аудиофайлов
output_dir = "english_audio"
os.makedirs("d:\\Temp\\output_dir", exist_ok=True)


# fileList collection with words
# wordFile.txt file that has all words

# Прочитайте слова из файла
with open("d:\\Temp\\wordFile_en.txt", "r", encoding="utf-8") as file:
    fileList = [line.strip() for line in file if line.strip()]

# Перевод. Получение имени mp3 без спец символов.
for word in fileList:
    translated_word = GoogleTranslator(source='en', target='ru').translate(word)
    mp3_file_name= word.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_").replace("'", "").replace("-", "_")
    mp3_file = gTTS(text=word, lang='en', tld='com')  # Американское произношение
    mp3_file.save(os.path.join("d:\\Temp\\output_dir", f"{mp3_file_name}.mp3"))
    translations.append((word, translated_word, "[sound:" + mp3_file_name + ".mp3]"))


# Сохранение в файл с разделителем табуляции
with open("d:\\Temp\\translations.txt", "w", encoding="utf-8") as file:
    for eng, rus, mp3 in translations:
        file.write(f"{eng}\t{rus}\t{mp3}\n")

