from flask import Flask, render_template, request, redirect, url_for
from tkinter import messagebox
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Menu.html')

@app.route('/start_game')
def start_game():
    # Ваш код для перехода на новое окно или страницу с игрой
    return "Игра началась!"

@app.route('/exit')
def exit_game():
    os.close(0)
    return "Приложение закрыто!"

if __name__ == '__main__':
    app.run(debug=True)