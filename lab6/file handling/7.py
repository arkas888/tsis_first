import os

def copy_file(source_path, destination_path):
    try:
        # Проверяем существование исходного файла
        if os.path.exists(source_path):
            # Открываем исходный файл для чтения ('rb' - режим чтения в двоичном формате)
            with open(source_path, 'rb') as source_file:
                # Открываем или создаем целевой файл для записи ('wb' - режим записи в двоичном формате)
                with open(destination_path, 'wb') as destination_file:
                    # Копируем содержимое исходного файла в целевой файл
                    destination_file.write(source_file.read())
            print(f"Содержимое файла '{source_path}' успешно скопировано в файл '{destination_path}'.")
        else:
            print(f"Исходный файл '{source_path}' не существует.")
    except Exception as e:
        print(f"Произошла ошибка при копировании файла: {e}")

def main():
    # Введите пути к исходному и целевому файлам
    source_path = input("Введите путь к исходному файлу: ")
    destination_path = input("Введите путь к целевому файлу: ")

    # Вызываем функцию для копирования содержимого файла
    copy_file(source_path, destination_path)

if __name__ == "__main__":
    main()
    
'''Импортируем модуль os для работы с операционной системой.

Создаем функцию copy_file(source_path, destination_path), которая принимает путь к исходному и целевому файлам и копирует содержимое.

Проверяем существование исходного файла с использованием os.path.exists(source_path).

Если исходный файл существует, открываем его для чтения в двоичном режиме ('rb') и целевой файл для записи в двоичном режиме ('wb').

Копируем содержимое исходного файла в целевой файл с использованием destination_file.write(source_file.read()).

Если происходит ошибка в блоке try, выводим сообщение об ошибке.

В функции main() запрашиваем у пользователя пути к исходному и целевому файлам.

Если программа запускается как основная, вызываем main().'''