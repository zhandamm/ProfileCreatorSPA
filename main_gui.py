import time
from doctest import master

import customtkinter as ctk
import gui_actions
from tkinter import filedialog
import configparser
import os
import pyautogui as pg

import main


from catch_proxy import catch_proxy


# Установка темной темы и размера окна
ctk.set_appearance_mode("dark")  # Темная тема
ctk.set_default_color_theme("dark-blue")  # Цветовая схема

# Создаем главное окно
app = ctk.CTk()
app.title("ProfileCreator")
app.geometry("450x350")  # Размер окна

config = configparser.ConfigParser()

def load_settings():
    if os.path.exists('config.ini'):
        config.read('config.ini')
        if 'SETTINGS' in config:
            aqum_entry.insert(0, config['SETTINGS'].get('aqum_path', ''))
            proxy_entry.insert(0, config['SETTINGS'].get('website_url', ''))


# Функция для кнопки "Запуск"
def start_profile_creator(amount=0):
    """Запускает процесс, если значение amount больше нуля."""
    if amount == 0:
        print("Количество равно нулю, выполнение не требуется.")
        return  # Выход из функции, если amount равно нулю

    print("Запуск нажат")
    gui_actions.collapse_all_windows()
    time.sleep(0.75)
    gui_actions.close_window("proxyPaster.ahk")
    main.create_profiles(amount)


def start_proxy_catcher():
    catch_proxy()



# Функция для перехода на панель "Настройки"
def show_settings():
    # Скрываем главные элементы
    hide_all_frames()

    # Отображаем панель настроек
    settings_frame.pack(fill="both", expand=True, padx=20, pady=20)


def show_proxy_paster():
    # Скрываем остальные фреймы
    hide_all_frames()

    # Показываем фрейм Proxy Paster
    proxy_paster_frame.pack(fill="both", expand=True, padx=20, pady=20)


def hide_all_frames():
    main_frame.pack_forget()
    settings_frame.pack_forget()
    proxy_paster_frame.pack_forget()


# Функция для возврата к основному интерфейсу
def show_main():
    # Скрываем панель настроек
    hide_all_frames()

    # Отображаем главные элементы
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)


# Функция для выбора пути к файлу aqum.exe
def browse_aqum_path():
    file_path = filedialog.askopenfilename(title="Выберите файл aqum.exe", filetypes=[("EXE Files", "*.exe")])
    if file_path:
        aqum_entry.delete(0, ctk.END)
        aqum_entry.insert(0, file_path)


# Функция для сохранения настроек в config.ini
def save_settings():
    config = configparser.ConfigParser()
    config['SETTINGS'] = {
        'website_url': proxy_entry.get(),
        'aqum_path': aqum_entry.get()
    }
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    print("Настройки сохранены в config.ini")


# Главный фрейм с кнопками "Запуск" и "Настройки"
main_frame = ctk.CTkFrame(master=app)
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Поле для ввода количества профилей
profile_count_label = ctk.CTkLabel(master=main_frame, text="Количество профилей:")
profile_count_label.pack(pady=(10, 0))

profile_count_entry= ctk.CTkEntry(master=main_frame, width=140)
profile_count_entry.pack(pady=5)



run_button = ctk.CTkButton(master=main_frame, text="Запуск",
                           command=lambda: start_profile_creator(int(profile_count_entry.get())))
run_button.pack(pady=10)

# Добавление кнопки для перехода на фрейм Proxy Paster в главный фрейм
proxy_paster_button = ctk.CTkButton(master=main_frame, text="Прокси", command=show_proxy_paster)
proxy_paster_button.pack(pady=10)

settings_button = ctk.CTkButton(master=main_frame, text="Настройки", command=show_settings)
settings_button.pack(pady=10)








# TODO Proxy frame

# Добавление фрейма для Proxy Paster
proxy_paster_frame = ctk.CTkFrame(master=app)


# Поле для ввода количества профилей
profile_count_label = ctk.CTkLabel(master=proxy_paster_frame, text="Количество прокси:")
profile_count_label.pack(pady=(10, 0))

proxy_count_entry= ctk.CTkEntry(master=proxy_paster_frame, width=140)
proxy_count_entry.pack(pady=5)

run_button = ctk.CTkButton(master=proxy_paster_frame, text="Запуск",
                           command=lambda: catch_proxy(int(proxy_count_entry.get())))
run_button.pack(pady=10)

# Кнопка для возврата к главному экрану
proxy_back_button = ctk.CTkButton(proxy_paster_frame, text="Назад", command=show_main)
proxy_back_button.pack(pady=(5, 10))






# TODO Settings frame

# Фрейм для настроек
settings_frame = ctk.CTkFrame(master=app)

# Заголовок настроек
label = ctk.CTkLabel(settings_frame, text="Настройки приложения", font=("Arial", 16))
label.grid(row=0, column=0, columnspan=3, pady=(10, 20))

# Поле для ввода пути к файлу aqum.exe и кнопка для выбора файла
aqum_label = ctk.CTkLabel(settings_frame, text="Путь к AQUM Browser.exe:")
aqum_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)

aqum_entry = ctk.CTkEntry(settings_frame, width=300)
aqum_entry.grid(row=2, column=0, padx=10, pady=5)

aqum_browse_button = ctk.CTkButton(settings_frame, text="Выбрать", command=browse_aqum_path, width=40)
aqum_browse_button.grid(row=2, column=2, padx=4, pady=5)

# Поле для ввода ссылки на сайт с проксями
proxy_label = ctk.CTkLabel(settings_frame, text="Ссылка на прокси:")
proxy_label.grid(row=4, column=0, sticky="w", padx=10, pady=5)

proxy_entry = ctk.CTkEntry(settings_frame, width=300)
proxy_entry.grid(row=5, column=0, columnspan=1, padx=10, pady=5)

apply_button = ctk.CTkButton(settings_frame, text="Применить", command=save_settings)
apply_button.grid(row=6, column=0, pady=(5, 10))
# Кнопка "Назад" для возврата к основному интерфейсу
back_button = ctk.CTkButton(settings_frame, text="Назад", command=show_main)
back_button.grid(row=7, column=0, padx=10, pady=(5, 10))

# Загрузка настроек при инициализации
load_settings()

# Запуск приложения
app.mainloop()
