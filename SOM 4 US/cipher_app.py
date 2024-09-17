import tkinter as tk
from tkinter import messagebox

# Алгоритмы шифрования и дешифрования
def encode(text):
    encoded_text = ""
    for char in text:
        encoded_text += chr(ord(char) + 3)  # Простое шифрование сдвигом на 3 символа
    return encoded_text

def decode(text):
    decoded_text = ""
    for char in text:
        decoded_text += chr(ord(char) - 3)  # Обратный процесс
    return decoded_text

# Функции для кнопок
def on_encode():
    input_text = text_input.get("1.0", "end-1c")
    if len(input_text) > 200:
        messagebox.showerror("Ошибка", "Превышено ограничение в 200 символов.")
        return

    encoded_text = encode(input_text)
    text_output.config(state='normal')
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, encoded_text)
    text_output.config(state='disabled')

    decode_button.config(state='normal')  # Активировать кнопку "Декодировать"

def on_decode():
    encoded_text = text_output.get("1.0", "end-1c")
    decoded_text = decode(encoded_text)

    text_input.delete("1.0", tk.END)
    text_input.insert(tk.END, decoded_text)

# Создание главного окна
root = tk.Tk()
root.title("Шифратор и дешифратор")
root.geometry("450x450")
root.config(bg='#f5f5f5')  # Фон окна

# Стили кнопок и текста
button_style = {
    "font": ("Helvetica", 12, "bold"),
    "bg": "#4CAF50",  # Зеленый цвет кнопки
    "fg": "white",
    "relief": "groove",  # Плоские кнопки с рельефом
    "bd": 2,  # Граница для округления
    "activebackground": "#45a049",  # Цвет при нажатии
    "highlightthickness": 0,
    "cursor": "hand2"
}

entry_style = {
    "font": ("Arial", 12),
    "bg": "white",
    "fg": "black",
    "highlightbackground": "#ddd",
    "highlightcolor": "#888"
}

# Оформление с текстом и полями
tk.Label(root, text="Введите текст (до 200 символов):", bg="#f5f5f5", font=("Helvetica", 12)).pack(pady=10)
text_input = tk.Text(root, height=5, width=40, **entry_style)
text_input.pack(pady=10)

# Кнопка шифрования
encode_button = tk.Button(root, text="Кодировать", command=on_encode, **button_style)
encode_button.pack(pady=10)

# Поле для вывода зашифрованного текста
tk.Label(root, text="Зашифрованный текст:", bg="#f5f5f5", font=("Helvetica", 12)).pack(pady=10)
text_output = tk.Text(root, height=5, width=40, state='disabled', **entry_style)
text_output.pack(pady=10)

# Кнопка дешифрования (изначально отключена)
decode_button = tk.Button(root, text="Декодировать", state='disabled', command=on_decode, **button_style)
decode_button.pack(pady=10)

# Запуск главного цикла приложения
root.mainloop()
