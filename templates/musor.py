import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import customtkinter
class Game:
    def __init__(self, master):
        self.master = master
        self.master.title("Запомни число")
        self.master.geometry("700x400")
        self.master.resizable(False, False)
        self.master.config(bg="#B2B1CF")
        self.square_size = 50
        self.squares = []
        self.numbers_sequence = []

        for i in range(8):
            square = tk.Canvas(master, width=self.square_size, height=self.square_size, bg="white", highlightthickness=0)
            square.grid(row=0, column=i, padx=17, pady=90)
            self.squares.append(square)

        self.draw_squares()
        #button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.start_button = customtkinter.CTkButton(master, corner_radius=10, fg_color="white", text_color="black",
                                                    hover_color="lightgray", text="Начать игру", command=self.start_game)
        self.start_button.configure(state=DISABLED)
        self.start_button.grid(row=3, column=2, columnspan=4, pady=10)

        self.show_answer = tk.Button(master, text="Показать ответ", command=self.print_numbers_sequence, bg="#B2B1CF")
        self.show_answer.grid(row=5, column=2, columnspan=4, pady=10)

        self.quit_button = tk.Button(master, text="Выход", command=self.on_closing, bg="#B2B1CF")
        self.quit_button.grid(row=4, column=2, columnspan=4, pady=10)

        self.game_title = tk.Label(master, text="Запомни число", font=("Arial", 24), bg="#B2B1CF")
        self.game_title.place(x=235, y=20)
        self.sequence_label = tk.Label(master, text="", bg="#B2B1CF")
        self.sequence_label.grid(row=2, column=0, columnspan=8, pady=10)

    def draw_squares(self):
        colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "cyan"]
        for i, square in enumerate(self.squares):
            square.create_rectangle(0, 0, self.square_size, self.square_size, fill=colors[i], outline="black")

    # self.start_button.grid(row=4, column=1, columnspan=6, pady=10)
    # self.show_answer.grid(row=6, column=1, columnspan=6, pady=10)
    # self.quit_button.grid(row=7, column=1, columnspan=6, pady=10)
    # sequence_str = "Последовательность чисел: " + ", ".join(map(str, self.numbers_sequence))
    # self.sequence_label.config(text=sequence_str)
    # self.sequence_label.place(x=270, y=375)

    # self.draw_squares()
    # self.draw_user_squares()
    # def draw_squares(self):
    # for i, square in enumerate(self.squares):
    # square.create_rectangle(0, 0, self.square_size, self.square_size, fill="white", outline="black")
    def start_game(self):
        self.numbers_sequence = []
        self.current_square_index = 0
        self.show_random_number()

    def show_random_number(self):
        if self.current_square_index < len(self.squares):
            square = self.squares[self.current_square_index]
            random_number = random.randint(1, 10)
            square.delete("number")
            square.create_text(self.square_size/2, self.square_size/2, text=str(random_number), font=("Arial", 12), tags="number")
            self.numbers_sequence.append(random_number)
            self.master.after(1500, lambda: self.hide_number(square))
            self.current_square_index += 1

    def hide_number(self, square):
        square.delete("number")
        self.show_random_number()

    def on_closing(self):
        if messagebox.askokcancel("Выход из приложения","Действительно хотите закрыть приложение?"):
            root.destroy()

    def print_numbers_sequence(self):
        sequence_str = "Последовательность чисел: " + ", ".join(map(str, self.numbers_sequence))
        self.sequence_label.config(text=sequence_str)

# Создание главного окна
root = tk.Tk()

app = Game(root)

root.mainloop()
# self.button_start_game = ctk.CTkButton(parent, font=("Arial", 16), corner_radius=15, width=150, height=50, fg_color="white", text_color="black",
#                                        hover_color="lightgray", text="Начать игру", command=self.start_game) #Ошибка хз как фиксить
# self.button_start_game.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
# self.button_rules_game = ctk.CTkButton(parent, font=("Arial", 16), corner_radius=15, width=150, height=50,
#                                         fg_color="white", text_color="black",
#                                         hover_color="lightgray", text="Об игре", command=self.rules_game)
# self.button_rules_game.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
# self.button_quit_game = ctk.CTkButton(parent, font=("Arial", 16), corner_radius=15, width=150, height=50,
#                                         fg_color="white", text_color="black",
#                                        hover_color="lightgray", text="Выход из игры", command=self.quit_game)
# self.button_quit_game.place(relx=0.5, rely=0.75, anchor=tk.CENTER) # Не знаю как фиксить