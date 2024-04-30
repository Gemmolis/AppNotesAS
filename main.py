import json
import os
import datetime
from datetime import datetime 

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

    
# определяем функцию для чтения всех заметок
def readNotes():
    for note in notes:
     print(f"ID: {note['id']}; Заголовок: {note['title']}; Текст: {note['body']}; Дата: {note['date']} ")

# Определяем функцию для редактирования заметки
def editNote():
    noteId = int(input("Введите ID заметки, которую необходимо отредактировать  ==> "))
    noteIndex = -1

    for index, note in enumerate(notes):
        if note["id"] == noteId:
            noteIndex = index
            break

    if noteIndex != -1:
        noteTitle = input("Введите новый заголовок заметки:  ")
        noteBody = input("Введите новый текст заметки:  ")

        notes[noteIndex]["title"] = noteTitle
        notes[noteIndex]["body"] = noteBody
        notes[noteIndex]["date"] = datetime.now().strftime("%d.%m.%Y")

        saveNotes()
        print("Заметка успешно изменена  ==> ")
    else: 
        print("Заметка с указанным ID не найдена.")

#  определяем функцию для удаления заметки
def deletNote():
    noteId = int(input("Введите ID заметки, которую необходимо удалить ==> "))
    noteIndex = -1

    for index, note in enumerate(notes):
        if note["id"] == noteId:
            noteIndex = index
            break
    if noteIndex != -1:
        del notes[noteIndex]
        saveNotes()
        print(" \n Заметка успешно удалена")
    else:
        print("Заметка с указанным ID не найдена.")
        
# Определяем функцию для сохранения заметок в файл

def saveNotes():
    with open("notes.json", "w") as file:
        json.dump(notes, file)

# Определяем функцию для загрузки заметки из файла
def loadNotes():
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as file:
            notes.extend(json.load(file))


# Определяем фильтрацию по дате заметки
def filterNotes():
    datum = str(input("Введите дату заметки для поиска в формате дд.мм.гггг ==> "))
    filteredNotes = []
    
    for note in notes:
        if note["date"] == datum:
            filteredNotes.append(note)
                     

    for note in filteredNotes:
                
        print(f"ID: {note['id']}; Заголовок: {note['title']}; Текст: {note['body']}; Дата: {note['date']} ")


# основной код программы
notes = []

# загружаем заметки из файла
loadNotes()

while True:
    
    print(" \n Меню:")
    print("1. Создать заметку")
    print("2. Просмотреть все заметки")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")   
    print("5. Отбор заметок по дате")
    print("6. Выход \n")

    choice = input("Выберите действие:  ")
    
    if choice == "1":
        creatNote()
    elif choice == "2":
        readNotes()
    elif choice == "3":
        editNote()
    elif choice == "4":
        deletNote()
    elif choice == "5":
        filterNotes()
    elif choice == "6":
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")


