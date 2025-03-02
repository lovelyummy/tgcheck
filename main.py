import nltk
import random
from nltk.corpus import words

# Загружаем словарь английских слов NLTK
nltk.download("words")

# Фильтруем слова: минимум 5 букв и уникальные
unique_words = list(set(word.lower() for word in words.words() if len(word) >= 5))

# Выбираем случайные 2000 слов
random_words = random.sample(unique_words, 2000)

# Сохраняем в файл
with open("unique_words.txt", "w") as file:
    for word in random_words:
        file.write(word + "\n")

print("Файл unique_words.txt создан.")
