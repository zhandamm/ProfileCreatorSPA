import os
import time
import pyautogui as pg

project_dir = os.path.dirname(os.path.abspath(__file__))


def move_to_coordinates(coordinates, duration):
    center_cords = pg.center(coordinates)
    pg.moveTo(center_cords[0], center_cords[1])
    print(center_cords)


def click_on_image(image_path, move_duration=0.1):
    found = False
    while not found:
        try:
            founded_cords = pg.locateOnScreen(image_path, confidence=0.75)
            if founded_cords:
                # pg.moveTo(founded_cords, duration= move_duration)
                pg.click(founded_cords)
                found = True
            else:
                print("Изображение не найдено. Повторная попытка через 1 секунду...")
                time.sleep(1)
        except pg.ImageNotFoundException:
            print("Изображение не найдено. Повторная попытка через 1 секунду...")
            time.sleep(1)


def close_window(window_title: str):
    """Закрывает окно по заголовку."""
    # Переключение на нужное окно
    try:
        pg.getWindowsWithTitle(window_title)[0].activate()
        time.sleep(0.5)  # Небольшая задержка, чтобы окно успело активироваться
        pg.hotkey('alt', 'f4')  # Использование горячих клавиш для закрытия
        print("Окно закрыто")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def collapse_all_windows():
    pg.hotkey('win', 'd')


def run_ahk_proxyPaster():
    try:
        os.startfile(os.path.join(project_dir, "proxyPaster.ahk"))

        print("Скрипт запущен.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def run_ahk_profileNames():
    try:
        os.startfile(os.path.join(project_dir, "namesPaster.ahk"))

        print("Скрипт запущен.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
