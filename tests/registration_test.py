import time
import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from pages.other_pages import other_Page
from pages.registration_page import registratin_Form
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Форма регистрации")
@allure.story("Заполнение формы регистрации")
def test_registration(browser):
    with allure.step("Открываем главную страницу"):
        rForm = registratin_Form(browser)
        rForm.open()

    with allure.step("Заполняем поле ввода имени"):
        rForm.firstName_Area().send_keys("Ivan")

    with allure.step("Заполняем поле ввода фамилии"):
        rForm.lastName_Area().send_keys("Ivanov")

    with allure.step("Заполняем поле ввода email"):
        rForm.email_Area().click()
        rForm.email_Area().clear()
        rForm.email_Area().send_keys("Ivanov@gmail.com")


    with allure.step("Выбираем пол"):
        rForm.genderRB_Male().click()

    with allure.step("Заполняем поле ввода телефона"):
        rForm.phone_Area().send_keys("1234567890")

    with allure.step("Заполняем поле ввода даты рождения"):
        rForm.birthDate_Area().click()
        rForm.birthDate_Year().click()
        rForm.birthDate_Month().click()
        rForm.birthDate_Day().click()
        time.sleep(10)

    with allure.step("Заполняем поле ввода предметов"):
        rForm.subjects_Area().send_keys("Maths")
        rForm.subjects_Area().send_keys(Keys.RETURN)

    with allure.step("Выбираем хобби"):
        rForm.hobbiesCHB_Sports().click()
        rForm.hobbiesCHB_Reading().click()
        rForm.hobbiesCHB_Music().click()

    with allure.step("Загружаем картинку"):
        rForm.pictureUpload_Btn().send_keys("img/3.png")

    with allure.step("Заполняем поле ввода адреса"):
        rForm.currentAddress_Area().send_keys("Moscow")
        browser.execute_script("window.scrollBy(0, 1000);")

    with allure.step("Выбираем штат"):
        rForm.state_Selector().send_keys("NCR")
        rForm.state_Selector().send_keys(Keys.RETURN)

    with allure.step("Выбираем город"):
        rForm.city_Selector().send_keys("Delhi")
        rForm.city_Selector().send_keys(Keys.RETURN)

    with allure.step("Нажимаем на кнопку Submit"):
        rForm.submitBtn().click()
        time.sleep(2)

    with allure.step("Проверяем заголовок всплывающего окна"):
        assert rForm.title_popUp().text == "Thanks for submitting the form"
    
    with allure.step("Проверяем переданные данные в форму регистрации"):
        assert rForm.popUp_studentName().text == "Ivan Ivanov"
        assert rForm.popUp_studentEmail().text == "Ivanov@gmail.com"
        assert rForm.popUp_studentGender().text == "Male"
        assert rForm.popUp_studentBirthDate().text == "17 April,1992"
        assert rForm.popUp_studentSubjects().text == "Maths"
        assert rForm.popUp_studentHobbies().text == "Sports, Reading, Music"
        assert rForm.popUp_studentPicture().text == "3.png"
        assert rForm.popUp_studentAddress().text == "Moscow"
        assert rForm.popUp_studentStateAndCity().text == "NCR Delhi"