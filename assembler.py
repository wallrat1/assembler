import struct

# Создаем бинарный файл с командами
def create_binary_file(output_file):
    with open(output_file, "wb") as f:
        vector_start = 50  # Начальный адрес в памяти для вектора
        vector_length = 6  # Длина вектора
        number = 114       # Число для сравнения

        # Заполнение памяти вектором (например, [110, 112, 115, 116, 113, 117])
        vector = [110, 112, 115, 116, 113, 117]
        for i, value in enumerate(vector):
            f.write(struct.pack("BBB", 0x02, value, vector_start + i))  # WRITE

        # Выполняем поэлементное сравнение ">" для каждого элемента
        for i in range(vector_length):
            f.write(struct.pack("BBBB", 0x05, vector_start + i, number, vector_start + i))

    print(f"Бинарный файл {output_file} успешно создан.")

# Вызываем функцию
create_binary_file("program.bin")

