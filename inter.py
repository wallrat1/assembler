import struct
import json
import sys

# Интерпретатор команд
def interpret(binary_file, output_file):
    memory = [0] * 256  # Инициализируем память нулями

    with open(binary_file, "rb") as infile:
        while byte := infile.read(1):
            opcode = int.from_bytes(byte, "little")
            
            if opcode == 0x02:  # WRITE
                value, addr = struct.unpack("BB", infile.read(2))
                memory[addr] = value
                print(f"WRITE: значение={value}, адрес={addr}")
            
            elif opcode == 0x05:  # COMPARE ">"
                addr1, number, addr_result = struct.unpack("BBB", infile.read(3))
                result = 1 if memory[addr1] > number else 0
                memory[addr_result] = result
                print(f"COMPARE '>': addr1={addr1}, number={number}, result={result}")
            
            else:
                print(f"Неизвестная команда: {opcode:#x}")
                raise ValueError(f"Неизвестная команда: {opcode:#x}")

    # Сохраняем память в JSON
    with open(output_file, "w") as outfile:
        json.dump(memory, outfile, indent=4)
    print(f"Память сохранена в {output_file}.")

# Чтение аргументов командной строки
if len(sys.argv) != 3:
    print("Использование: python3 interpreter.py <binary_file> <output_file>")
else:
    binary_file = sys.argv[1]
    output_file = sys.argv[2]
    interpret(binary_file, output_file)

