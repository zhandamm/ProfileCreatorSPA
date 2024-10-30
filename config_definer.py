import configparser
import os

project_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(project_dir, "images")

def image_path(filename):
    return os.path.join(images_dir, filename)

def define_config(project_dir):
    # Define the file path within the project directory
    config_file_path = os.path.join(project_dir, "config.ini")

    # Create or load the configuration file
    config = configparser.ConfigParser()
    if not os.path.exists(config_file_path):
        with open(config_file_path, 'w') as configfile:
            config.add_section('SETTINGS')
            config.set('SETTING', 'aqum_path', '')  # Set an empty default value initially
            config.write(configfile)

    # Read the website URL from the configuration file
    config.read(config_file_path)
    aqum_path = config.get('SETTINGS', 'aqum_path')

    return config, aqum_path


def read_browser_path_from_config(config_file):
    with open(config_file, 'r') as f:
        browser_path = f.read().strip()
    return browser_path
