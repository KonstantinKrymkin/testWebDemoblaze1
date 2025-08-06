from gtts import gTTS
import pandas as pd
import os

# Слова и переводы — можно расширить
vocab = {
    "barcode": "штрихкод",
    "be asthmatic": "страдать астмой",
    "come out in a rash": "появляется сыпь",
    "come out in spots": "появляются пятна/прыщи",
    "cough": "кашель",
    "cut sth out": "перестать делать/есть что-то",
    "feel dizzy": "чувствовать головокружение",
    "keep track of": "отслеживать",
    "lose appetite": "потерять аппетит",
    "my thumb hurts": "у меня болит большой палец",
    "pass out": "потерять сознание",
    "faint": "упасть в обморок",
    "recover from": "восстановиться после",
    "get over an illness": "выздороветь",
    "reduce anxiety": "уменьшить тревожность",
    "runny nose": "насморк",
    "sore throat": "боль в горле",
    "stomachache": "боль в животе",
    "stress out": "сильно нервничать",
    "suffer from": "страдать от"
}

# Папка для аудио
audio_dir = "audio"
os.makedirs(audio_dir, exist_ok=True)

# Создание карточек
cards = []
for word, translation in vocab.items():
    # Генерация аудио
    tts = gTTS(text=word, lang='en')
    audio_file = f"{audio_dir}/{word.replace(' ', '_')}.mp3"
    tts.save(audio_file)

    # Для Anki вставка [sound:filename.mp3]
    cards.append({
        "English": word,
        "Russian": translation,
        "Audio": f"[sound:{os.path.basename(audio_file)}]"
    })

# Сохраняем как CSV
df = pd.DataFrame(cards)
df.to_csv("d:\\Temp\\anki_flashcards.csv", index=False)

print("✅ Карточки и аудио готовы: anki_flashcards.csv + папка /audio")
