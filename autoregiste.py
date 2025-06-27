import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def register_voice_generator(mail):
# Замените путь к драйверу на свой собственный
    driver = webdriver.Chrome()

    # Открываем сайт, на котором нужно зарегистрироваться
    driver.get('https://elevenlabs.io/sign-up')  # Замените на адрес сайта

    # Находим и заполняем поле с электронной почтой
    email_field = driver.find_element(By.NAME, 'email')  # Замените на соответствующий селектор
    email_field.send_keys(mail)

    # Находим и заполняем поле с паролем
    password_field = driver.find_element(By.NAME, 'password')  # Замените на соответствующий селектор
    password_field.send_keys(mail + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))

    # Находим и нажимаем кнопку "Зарегистрироваться" или "Отправить"
    register_button = driver.find_element(By.ID, 'sign-up-button')  # Замените на соответствующий селектор
    register_button.click()

register_voice_generator("mail")