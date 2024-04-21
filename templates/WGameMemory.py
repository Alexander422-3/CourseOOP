import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import json
from uuid import uuid4

class Statistic:
    @staticmethod
    def registration(nickname: str, password: str):
        if not password.isdigit():
            return "Цифр"
        with open('../users.json', 'r') as file:
            users = json.loads(file.read())
        if nickname == "" or password == "":
            return "Пусто"
        for user in users:
            if user['nickname'] == nickname:
                return "Никнейм занят"
        user = {"id": str(uuid4()), "nickname": nickname, "password": password, "maxlevel": 0}
        users.append(user)
        with open('../users.json', 'w') as file:
            file.write(json.dumps(users))
        return "1"

    @staticmethod
    def login(nickname: str, password: str):
        with open('../users.json', 'r') as file:
            users = json.loads(file.read())
        for user in users:
            if user['nickname'] == nickname and user["password"] == password:
                return user["id"]
        return "0"

    @staticmethod
    def update_stats(id: str, level: int):
        with open('../users.json', 'r') as file:
            users = json.loads(file.read())
        for user in users:
            if user['id'] == id:
                if user['maxlevel'] < level:
                    user['maxlevel'] = level
                    break
        with open('../users.json', 'w') as file:
            file.write(json.dumps(users))


    @staticmethod
    def get_statics():
        with open('../users.json', 'r') as file:
            users = json.loads(file.read())
        sorted_users = sorted(users, key=lambda x: x["maxlevel"], reverse=True)
        return sorted_users

class Menu:
    def __init__(self, parent):
       self.parent = parent
       self.id = "0"

    def field(self):
       self.parent.title("Запомни число")
       self.parent.geometry("550x400")
       self.parent.resizable(False, False)
       self.parent.config(bg="#6361AD")
       menu_title = tk.Label(self.parent, text="Запомни число", font=("Arial", 24), bg="#6361AD", foreground="white")
       menu_title.place(x=165, y=5)
       button_start_game = tk.Button(self.parent, text="Начать игру", font=("Arial", 12), command=self.start_game, bg="white")
       button_start_game.place(relx=0.35, rely=0.35, anchor="center", width=140, height=50)
       button_rules_game = tk.Button(self.parent, text="Правила игры", font=("Arial", 12), command=self.rules_game, bg="white")
       button_rules_game.place(relx=0.66, rely=0.35, anchor="center", width=140, height=50)
       button_quit_game = tk.Button(self.parent, text="Выход из игры", font=("Arial", 12), command=self.quit_game, bg="white")
       button_quit_game.place(relx=0.5, rely=0.75, anchor="center", width=140, height=50)
       button_registration = tk.Button(self.parent, text="Регистрация", font=("Arial", 12), command=self.reg, bg="white")
       button_registration.place(relx=0.35, rely=0.55, anchor="center", width=140, height=50)
       button_autorization = tk.Button(self.parent, text="Авторизация", font=("Arial", 12), command=self.auto,
                                            bg="white")
       button_autorization.place(relx=0.66, rely=0.55, anchor="center", width=140, height=50)


    def start_game(self):
        self.parent.destroy()
        game_window = tk.Tk()
        game = Game(game_window, self)

    def reg(self):
        reg_game = tk.Toplevel()
        reg_game.title("Запомни число")
        reg_game.geometry("300x175")
        reg_game.config(bg="#6361AD")
        reg_game.resizable(False, False)
        login_label = tk.Label(reg_game, text="Никнейм: ", font=("Arial", 11),
                               bg="#6361AD", foreground="white")
        login_label.place(relx=0.12, rely=0.15, anchor="center", width=150, height=25)
        password_label = tk.Label(reg_game, text="Пароль: ", font=("Arial", 11),
                                    bg="#6361AD", foreground="white")
        password_label.place(relx=0.12, rely=0.35, anchor="center", width=150, height=25)
        self.nickname_pole = tk.Entry(reg_game, width=5, font=("Arial", 12), justify="center", highlightbackground="black",
                                   highlightthickness=1)
        self.nickname_pole.place(relx=0.5, rely=0.15, anchor="center", width=150, height=25)

        self.successful_label = tk.Label(reg_game, text="", font=("Arial", 11),
                                    bg="#6361AD", foreground="white")
        self.successful_label.place(relx=0.5, rely=0.8, anchor="center", width=150, height=25)

        self.password_pole = tk.Entry(reg_game, width=5, font=("Arial", 12), justify="center",
                                 highlightbackground="black",
                                 highlightthickness=1)
        self.password_pole.place(relx=0.5, rely=0.35, anchor="center", width=150, height=25)

        button_reg = tk.Button(reg_game, text="Зарегистрироваться", font=("Arial", 12), command=self.try_reg,
                                            bg="white")
        button_reg.place(relx=0.5, rely=0.65, anchor="center", width=155, height=30)

    def try_reg(self):
        error = Statistic.registration(self.nickname_pole.get(), self.password_pole.get())
        if error == "Никнейм занят":
            self.successful_label.config(text="Никнейм занят!")
        elif error == "Пусто":
            self.successful_label.config(text="Вы не ввели текст!")
        elif error =="Цифр":
            self.successful_label.config(text="Пароль только из цифр")
        else:
            self.successful_label.config(text="Регистрация успешна!")


    def try_auto(self):
        id = Statistic.login(self.nickname_pole.get(), self.password_pole.get())
        if id == "0":
            self.auth_errors.config(text="Неверные данные")
        else:
            self.id = id
            self.auth_errors.config(text="Вход выполнен")


    def auto(self):
        auth_game = tk.Toplevel()
        auth_game.title("Запомни число")
        auth_game.geometry("300x175")
        auth_game.config(bg="#6361AD")
        auth_game.resizable(False, False)
        self.auth_errors = tk.Label(auth_game, text="", font=("Arial", 11),
                               bg="#6361AD", foreground="white")
        self.auth_errors.place(relx=0.5, rely=0.8, anchor="center", width=150, height=25)

        login_label = tk.Label(auth_game, text="Никнейм: ", font=("Arial", 11),
                               bg="#6361AD", foreground="white")
        login_label.place(relx=0.12, rely=0.15, anchor="center", width=150, height=25)
        self.password_label = tk.Label(auth_game, text="Пароль: ", font=("Arial", 11),
                                    bg="#6361AD", foreground="white")
        self.password_label.place(relx=0.12, rely=0.35, anchor="center", width=150, height=25)
        self.nickname_pole = tk.Entry(auth_game, width=5, font=("Arial", 12), justify="center", highlightbackground="black",
                                   highlightthickness=1)
        self.nickname_pole.place(relx=0.5, rely=0.15, anchor="center", width=150, height=25)
        self.password_pole = tk.Entry(auth_game, width=5, font=("Arial", 12), justify="center",
                                 highlightbackground="black",
                                 highlightthickness=1)
        self.password_pole.place(relx=0.5, rely=0.35, anchor="center", width=150, height=25)

        button_auth = tk.Button(auth_game, text="Авторизироваться", font=("Arial", 12), command=self.try_auto,
                                            bg="white")
        button_auth.place(relx=0.5, rely=0.65, anchor="center", width=155, height=30)

    def rules_game(self):
        info_game = tk.Toplevel()
        info_game.title("Запомни число")
        info_game.geometry("300x175")
        info_game.resizable(False, False)
        info_game.config(bg="#6361AD")
        title_rules = tk.Label(info_game, text="Правила игры:", font=("Arial", 13), bg="#6361AD", foreground="white")
        title_rules.place(x=5, y=5)
        rules1 = tk.Label(info_game, text="- Запомни последовательность чисел", font=("Arial", 11), bg="#6361AD",
                                    foreground="white")
        rules1.place(x=12, y=25)
        rules2 = tk.Label(info_game, text="- Введи числа в нижние квадраты", font=("Arial", 11),
                               bg="#6361AD",
                               foreground="white")
        rules2.place(x=12, y=45)
        rules3 = tk.Label(info_game, text="- Повышай свой уровень", font=("Arial", 11),
                               bg="#6361AD", foreground="white")
        rules3.place(x=12, y=65)
        rules4 = tk.Label(info_game, text="- Просматривай статистику", font=("Arial", 11),
                               bg="#6361AD", foreground="white")
        rules4.place(x=12, y=85)
        close_button = tk.Button(info_game, text="Закрыть", bg="white", command=lambda: info_game.destroy())
        close_button.place(relx=0.38, rely=0.85)

    def quit_game(self):
        if messagebox.askokcancel("Выход из приложения", "Действительно хотите закрыть приложение?"):
            self.parent.destroy()


class Game:
    def __init__(self, master, Menu):
        self.history = {}
        self.master = master
        self.menu = Menu
        self.master.title("Запомни число")
        self.master.geometry("717x400")
        self.master.resizable(False, False)
        self.master.config(bg="#6361AD")
        self.square_size = 68
        self.level = 1
        self.user_answers = [-1, -1, -1, -1, -1, -1, -1]
        self.squares = []
        self.user_squares = []
        self.numbers_sequence = []
        self.k = 0
        self.sdvig_x = 0


        for i in range(7):
            square = tk.Canvas(master, width=self.square_size, height=self.square_size, bg="white",
                               highlightbackground="black", highlightthickness=1)
            square.grid(row=0, column=i, padx=17, pady=90)
            self.squares.append(square)

        for y in range(7):
            user_square = tk.Entry(master, width=5, font=("Arial", 12), justify="center", highlightbackground="black",
                                   highlightthickness=1)
            user_square.place(relx=0.071+self.sdvig_x, rely=0.55, anchor="center", width=71, height=71)
            user_square.config(state=DISABLED)
            user_square.config(validate="key")
            user_square.config(validatecommand=(user_square.register(self.validate_input), '%P'))
            self.user_squares.append(user_square)
            self.sdvig_x += 0.145

        self.start_button = tk.Button(master, text="Запустить игру", font=("Arial", 12), command=self.start_game, bg="white")
        self.start_button.place(relx=0.5, rely=0.7, anchor="center", width=120, height=30)


        self.show_answer_button = tk.Button(master, text="Показать ответ", font=("Arial", 12), command=self.print_numbers_sequence, bg="white")
        self.show_answer_button.place(relx=0.9, rely=0.85, anchor="center", width=120, height=30)
        self.show_answer_button.config(state=DISABLED)

        self.button_hide_answer = tk.Button(master, text="Cкрыть ответ", font=("Arial", 12), command=self.clear_squares_text, bg="white")
        self.button_hide_answer.place(relx=0.9, rely=0.95, anchor="center", width=120, height=30)
        self.button_hide_answer.config(state=DISABLED)

        self.quit_button = tk.Button(master, text="Выход в меню", command=self.on_closing, bg="white")
        self.quit_button.place(x=10, y=370)

        self.answer_button = tk.Button(master, text="Ответить", font=("Arial", 12), command=self.check_answer, bg="white")
        self.answer_button.place(relx=0.5, rely=0.8, anchor="center", width=120, height=30)
        self.answer_button.config(state=DISABLED)

        self.game_title = tk.Label(master, text="Запомни число", font=("Arial", 20), bg="#6361AD", foreground="white")
        self.game_title.place(x=260, y=5)
        self.sequence_label = tk.Label(master, text="", bg="#B2B1CF")

        self.game_level = tk.Label(master, text="Уровень " + str(self.level), font=("Arial", 14), bg="#6361AD", foreground="white")
        self.game_level.place(x=310, y=50)

        self.show_stats_button = tk.Button(master, text="Показать статистику", font=("Arial", 10), command=self.show_all_stats,
                                       bg="white")
        self.show_stats_button.place(x=10, y=330)
    def clear_squares_text(self):
        for square in self.squares:
            square.delete("number")

    def clear_user_squares_text(self):
        for square in self.user_squares:
            square.delete(0, END)
    def start_game(self):
        self.clear_squares_text()
        self.numbers_sequence = []
        self.current_square_index = 0
        self.show_random_number()

    def show_random_number(self):
        if self.current_square_index < len(self.squares):
            square = self.squares[self.current_square_index]
            if self.level == 1:
                random_number = random.randint(0, 9)
            elif self.level == 2:
                random_number = random.randint(10, 99)
            elif self.level == 3:
                random_number = random.randint(100, 999)
            elif self.level == 4:
                random_number = random.randint(1000, 9999)
            #random_number =random.randint(10**(self.level-1), 10**self.level-1)
            square.delete("number")
            square.create_text(self.square_size/2, self.square_size/2, text=str(random_number), font=("Arial", 12), tags="number")
            self.k += 1
            if self.k == len(self.squares):
                self.show_answer_button.config(state=NORMAL)
                self.answer_button.config(state=NORMAL)
                self.button_hide_answer.config(state=NORMAL)
                for i in range(0, 7):
                    self.user_squares[i].config(state=NORMAL)
                self.k = 0
            elif self.k != len(self.squares):
                self.show_answer_button.config(state=DISABLED)
                self.answer_button.config(state=DISABLED)
                self.button_hide_answer.config(state=DISABLED)
                for i in range(0, 7):
                    self.user_squares[i].config(state=DISABLED)
            self.numbers_sequence.append(random_number)
            self.master.after(100, lambda: self.hide_number(square))
            self.current_square_index += 1
    def hide_number(self, square):
        square.delete("number")
        self.show_random_number()
    def on_closing(self):
        self.master.destroy()
        menu_window = tk.Tk()
        menu = Menu(menu_window)
        menu.field()

    def print_numbers_sequence(self):
        index = 0
        for i in range(0, 7):
            square_answers = self.squares[index]
            square_answers.create_text(self.square_size / 2, self.square_size / 2, text=str(self.numbers_sequence[i]), font=("Arial", 12),
                           tags="number")
            index += 1

    def validate_input(self, new_text):
        if new_text.isdigit() or new_text == "":
            return True
        else:
            return False
    def get_answer(self):
        #self.massiv_users = [-1, -1, -1, -1, -1, -1, -1]
        for i in range(7):
            user_input = self.user_squares[i].get()
            if not user_input:
                messagebox.showerror("Ошибка", "Вы не заполнили все поля")
                return 1
            else:
                #self.massiv_users[i] = int(user_input)
                self.user_answers[i] = int(user_input)
        #print(self.massiv_users)
        print(self.user_answers)
    def check_answer(self):
        print(self.numbers_sequence)
        if self.get_answer() == 1:
            return 1
        #self.history[self.level] = {'program_number': self.numbers_sequence, 'user_answer': self.massiv_users}
        self.history[self.level] = {'program_number': self.numbers_sequence, 'user_answer': self.user_answers}
        #if self.level == 4 and self.massiv_users == self.numbers_sequence:
        if self.level == 4 and self.user_answers == self.numbers_sequence:
            result = "Вы успешно прошли игру!"
            current_level = self.level
            self.statistica(current_level, result)
            self.level = 1
            self.game_level.config(text="Уровень " + str(self.level))
            self.clear_squares_text()
            self.clear_user_squares_text()
            for i in range(0, 7):
                self.user_squares[i].config(state=DISABLED)
            self.show_answer_button.config(state=DISABLED)
            self.button_hide_answer.config(state=DISABLED)
            self.answer_button.config(state=DISABLED)
            self.show_history()
        #elif self.massiv_users == self.numbers_sequence:
        elif self.user_answers == self.numbers_sequence:
            messagebox.showinfo("Уведомление", "Уровень пройден успешно!")
            self.level += 1
            self.game_level.config(text="Уровень " + str(self.level))
            self.clear_squares_text()
            self.clear_user_squares_text()
            for i in range(0, 7):
                self.user_squares[i].config(state=DISABLED)
            self.show_answer_button.config(state=DISABLED)
            self.button_hide_answer.config(state=DISABLED)
            self.answer_button.config(state=DISABLED)
        else:
            result = "Вы успешно прошли игру!"
            current_level = self.level
            self.statistica(current_level, result)
            self.level = 1
            self.game_level.config(text="Уровень " + str(self.level))
            self.clear_squares_text()
            self.clear_user_squares_text()
            for i in range(0, 7):
                self.user_squares[i].config(state=DISABLED)
            self.show_answer_button.config(state=DISABLED)
            self.button_hide_answer.config(state=DISABLED)
            self.answer_button.config(state=DISABLED)
            self.show_history()

    def statistica(self, current_level, result):
        statistic = tk.Toplevel()
        statistic.title("Запомни число")
        statistic.geometry("300x175")
        statistic.config(bg="#6361AD")
        statistic.resizable(False, False)
        self.statistic_label = tk.Label(statistic, text=result+"\n Желаете сохранить статистику?", font=("Enter", 11),
                                    bg="#6361AD", foreground="white", width=30, height=3)
        self.statistic_label.place(relx=0.5, rely=0.15, anchor="center")
        statistic_label_auto = tk.Label(statistic, text="", font=("Enter", 11),
                                    bg="#6361AD", foreground="white", width=30, height=2)
        statistic_label_auto.place(relx=0.5, rely=0.35, anchor="center")
        statistic_button = tk.Button(statistic, text="Cохранить статистику", font=("Arial", 12), command=lambda: self.save_stats(statistic, current_level),
                                       bg="white")
        statistic_button.place(relx=0.5, rely=0.8, anchor="center", width=165, height=30)
    def save_stats(self, statistic, current_level):
        if self.menu.id == "0":
            statistic.winfo_children()[1].configure(text="Вы не авторизированы")
            button_registration = tk.Button(statistic, text="Регистрация", font=("Arial", 12), command=self.menu.reg,
                                            bg="white")
            button_registration.place(relx=0.2, rely=0.55, anchor="center", width=150, height=25)
            button_autorization = tk.Button(statistic, text="Авторизация", font=("Arial", 12), command=self.menu.auto,
                                            bg="white")
            button_autorization.place(relx=0.76, rely=0.55, anchor="center", width=150, height=25)
        else:
            print("menuid=", self.menu.id, "level=", current_level)
            Statistic.update_stats(self.menu.id, current_level)
            statistic.winfo_children()[1].configure(text="Статистика сохранена")

    def show_all_stats(self):
        show_statistic = tk.Toplevel()
        show_statistic.title("Запомни число")
        show_statistic.geometry("400x600")
        show_statistic.config(bg="#6361AD")
        show_statistic.resizable(False, False)
        statistic_frame = tk.Frame(show_statistic, width=400, height=600, background="#6361AD")
        statistic_label1 = tk.Label(statistic_frame, text="Cтатистика", font=("Enter", 20),
                                   bg="#6361AD", foreground="white", width=10, height=1)
        statistic_label1.grid(row=0, column=0, columnspan=3, pady=10)
        statistic_label2 = tk.Label(statistic_frame, text="Игрок", font=("Enter", 18),
                                   bg="#6361AD", foreground="white", width=8, height=1)
        statistic_label2.grid(row=1, column=0, pady=10)
        statistic_label3 = tk.Label(statistic_frame, text="Уровень", font=("Enter", 18),
                                   bg="#6361AD", foreground="white", width=8, height=1)
        statistic_label3.grid(row=1, column=1, pady=10)
        statistic_label4 = tk.Label(statistic_frame, text="Место", font=("Enter", 18),
                                    bg="#6361AD", foreground="white", width=8, height=1)
        statistic_label4.grid(row=1, column=2, pady=10)

        stats = []
        users = Statistic.get_statics()
        for i in range(len(users)):
            temp = []
            label1 = tk.Label(statistic_frame, text=users[i]["nickname"], font=("Enter", 18),
                                   bg="#6361AD", foreground="white", width=8, height=1)
            label1.grid(row=2 + i, column=0, pady=5)
            label2 = tk.Label(statistic_frame, text=users[i]["maxlevel"], font=("Enter", 18),
                             bg="#6361AD", foreground="white", width=8, height=1)
            label2.grid(row=2 + i, column=1, pady=5)
            label3 = tk.Label(statistic_frame, text=str(i+1), font=("Enter", 18),
                              bg="#6361AD", foreground="white", width=8, height=1)
            label3.grid(row=2 + i, column=2, pady=5)
            temp.append(label1)
            temp.append(label2)
            temp.append(label3)
            stats.append(temp)
        statistic_frame.pack()
    def show_history(self):
        history_window = tk.Toplevel(self.master)
        history_window.title("История игры")
        history_window.geometry("400x500")

        history_label = tk.Label(history_window, text="История игры", font=("Arial", 14))
        history_label.pack()

        for level, data in self.history.items():
            level_label = tk.Label(history_window, text=f"Уровень {level}:", font=("Arial", 12))
            level_label.pack()

            program_label = tk.Label(history_window, text=f"Число программы: {data['program_number']}")
            program_label.pack()

            user_label = tk.Label(history_window, text=f"Ваш ответ: {data['user_answer']}")
            user_label.pack()

            separator = tk.Frame(history_window, height=2, bd=1, relief=tk.SUNKEN)
            separator.pack(fill=tk.X, padx=5, pady=5)

root = tk.Tk()
app = Menu(root)
app.field()
root.mainloop()