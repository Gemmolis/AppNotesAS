import json
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

    # Определяем функцию для сохранения заметок в файл

def saveNotes():
    with open("notes.json", "w") as file:
        json.dump(notes, file)

# определяем функцию для чтения всех заметок
def readNotes():
    for note in notes:
        print(f"ID: {note['id']}; Заголовок: {note['title']}; Текст: {note['body']}; Дата: {note['date']} ")




# основной код программы
notes = []

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


