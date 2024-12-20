import os
import time
import config_definer
import gui_actions
import pyautogui as pg
import catch_proxy


def wait_for_image_to_disappear(image_path):
    while True:
        try:
            # Пытаемся найти координаты изображения
            founded_cords = pg.locateOnScreen(image_path, confidence=0.75)

            # Если изображение найдено, ждем и повторяем проверку
            if founded_cords:
                print("Вкладка не закрылась. Ждем 1 секунду")
                time.sleep(1)
            # Если изображение не найдено, выходим из цикла
            else:
                print("Изображение исчезло с экрана.")
                break
        except pg.ImageNotFoundException:
            print("Изображение исчезло с экрана.")
            break


def wait_for_image_to_appear(image_path):
    while True:
        try:
            # Attempt to locate the image on the screen
            found_cords = pg.locateOnScreen(image_path, confidence=0.75)

            # If the image is found, exit the loop
            if found_cords:
                print("Изображение появилось на экране.")
                break
            # If the image is not found, wait and repeat the check
            else:
                print("Изображение не найдено. Ждем 1 секунду.")
                time.sleep(1)
        except pg.ImageNotFoundException:
            print("Изображение не найдено. Ждем 1 секунду.")
            time.sleep(1)


def create_profiles(amount=1):
    global driver, get_another_button, ip_element

    count = 1

    config, aqum_path = config_definer.define_config(config_definer.project_dir)

    config_file_path = aqum_path

    while count <= amount:
        os.startfile(config_file_path)
        time.sleep(1)

        gui_actions.click_on_image(config_definer.image_path("createNewProfile.png"))
        time.sleep(0.05)

        gui_actions.click_on_image(config_definer.image_path("profileNameField.png"))
        time.sleep(0.05)
        pg.hotkey('alt', '2')
        time.sleep(0.05)

        gui_actions.click_on_image(
            config_definer.image_path("connectionField.png"))
        time.sleep(0.05)

        gui_actions.click_on_image(
            config_definer.image_path("pinnedToProfile.png"))
        time.sleep(0.05)

        gui_actions.click_on_image(
            config_definer.image_path("socks5Arrow.png"))
        time.sleep(0.05)

        gui_actions.click_on_image(
            config_definer.image_path("socks5.png"))
        time.sleep(0.05)

        gui_actions.click_on_image(
            config_definer.image_path("hostOrAutofill.png"))
        time.sleep(0.05)
        pg.hotkey('alt', '1')
        time.sleep(0.05)

        gui_actions.click_on_image(
            config_definer.image_path("create.png"))
        time.sleep(0.05)

        count = count + 1


if __name__ == "__main__":
    amount = input("Пожалуйста, введите кол-во профилей: ")

    create_profiles(int(amount))
    exit()
