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


def main(amount=1):
    global driver, get_another_button, ip_element

    count = 1

    config, aqum_path = config_definer.define_config(config_definer.project_dir)

    config_file_path = aqum_path

    while count <= amount:
        os.startfile(config_file_path)
        time.sleep(1)

        gui_actions.click_on_image(config_definer.image_path("quickProfile.png"), 0.1)
        time.sleep(1)

        gui_actions.click_on_image(config_definer.image_path("noProxy.png"), 0.1)
        time.sleep(1)

        gui_actions.click_on_image(config_definer.image_path("chainToProfile.png"), 0.1)
        time.sleep(1)

        gui_actions.click_on_image(config_definer.image_path("protocol.png"), 0.1)
        time.sleep(1)

        gui_actions.click_on_image(config_definer.image_path("socks5.png"), 0.1)
        time.sleep(1)

        gui_actions.click_on_image(config_definer.image_path("hostOrAutofill.png"), 0.1)
        time.sleep(1)
        pg.hotkey('alt', '1')
        time.sleep(1)

        gui_actions.click_on_image(config_definer.image_path("confirm.png"), 0.1)
        time.sleep(1)

        wait_for_image_to_disappear(config_definer.image_path("editProxy.png"))
        time.sleep(1)

        count = count + 1


if __name__ == "__main__":
    amount = input("Пожалуйста, введите кол-во профилей: ")

    main(int(amount))
    exit()
