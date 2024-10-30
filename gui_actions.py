
import os
import time
import pyautogui as pg
import cv2

def move_to_coordinates(coordinates, duration):
    center_cords = pg.center(coordinates)
    pg.moveTo(center_cords[0], center_cords[1])
    print(center_cords)


def click_on_image(image_path, move_duration=0.5):
    found = False
    while not found:
        try:
            founded_cords = pg.locateOnScreen(image_path, confidence=0.75)
            if founded_cords:
                pg.click(founded_cords)
                found = True
            else:
                print("Изображение не найдено. Повторная попытка через 1 секунду...")
                time.sleep(1)
        except pg.ImageNotFoundException:
            print("Изображение не найдено. Повторная попытка через 1 секунду...")
            time.sleep(1)