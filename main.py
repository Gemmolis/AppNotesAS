import json

# Функция для создания заметки

def creatNote():
    noteDate = datetime.now().strftime("%d.%m.%Y") # текущая дата
    noteId = len(notes) + 1 # уникальный номер заметки
    noteTitle = input("Создайте заголовок:  ")
    noteBody = input("Создайте текст:  ")

    # объявляем заметку 
    note = {
        "id": noteId,
        "title": noteTitle,
        "body": noteBody,
        "date": noteDate 
    }
    notes.append(note) #добавляет один аргумент  в конец списка

    saveNotes()
    
    print("Заметка успешно создана")

    # Определяем функцию для сохранения заметок в файл

def saveNotes():
    with open("notes.json", "w") as file:
        json.dump(notes, file)


