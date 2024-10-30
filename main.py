import os
import time
import config_definer
import gui_actions
import pyautogui as pg
import catch_proxy




def main(amount = 1):
    global driver, get_another_button, ip_element

    count = 1


    project_dir = os.path.dirname(os.path.abspath(__file__))


    config, aqum_path = config_definer.define_config(config_definer.project_dir)

    # amount = input("Пожалуйста, введите число профилей: ")
    # amount = int(amount)

    config_file_path = aqum_path

    # browser_exe_path = config_definer.read_browser_path_from_config(config_file_path)

    while count <= amount:
        os.startfile(config_file_path)
        time.sleep(1)

        gui_actions.click_on_image(config_definer.image_path("createNewProfile.png"), 0.1)
        time.sleep(1)

        gui_actions.click_on_image(
            config_definer.image_path("selectFromTemplate.png"), 0.1)
        time.sleep(1)

        gui_actions.click_on_image(config_definer.image_path("profileNameField.png"), 0.1)
        time.sleep(1)
        pg.hotkey('alt', '2')
        time.sleep(1)

        # gui_actions.clickOnImage.clickOnImage(r"C:\Users\Nitro 5\PycharmProjects\ProfileCreator3\ProfileCreator3\images\create.png", 0.1)
        # time.sleep(1)


        gui_actions.click_on_image(
            config_definer.image_path("connectionField.png"), 0.1)
        time.sleep(1)

        gui_actions.click_on_image(
            config_definer.image_path("pinnedToProfile.png"), 0.1)
        time.sleep(1)

        gui_actions.click_on_image(
            config_definer.image_path("socks5Arrow.png"), 0.1)
        time.sleep(1)

        gui_actions.click_on_image(
            config_definer.image_path("socks5.png"), 0.1)
        time.sleep(1)

        gui_actions.click_on_image(
            config_definer.image_path("hostOrAutofill.png"), 0.1)
        time.sleep(1)
        pg.hotkey('alt', '1')
        time.sleep(1)

        # gui_actions.click_on_image(
        #     config_definer.image_path("proxyTest.png"), 0.1)
        # time.sleep(1)

        gui_actions.click_on_image(
            config_definer.image_path("create.png"), 0.1)
        time.sleep(1)

        count = count + 1


if __name__ == "__main__":
    amount = input("Пожалуйста, введите кол-во профилей: ")


    main(int(amount))
    exit()

