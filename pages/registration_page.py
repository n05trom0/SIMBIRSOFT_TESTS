from pages.other_pages import other_Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

firstName_Area = (By.ID, "firstName")
lastName_Area = (By.CSS_SELECTOR, "input#lastName")
email_Area = (By.XPATH, "//input[@class='mr-sm-2 form-control']")

genderRB_Male = (By.XPATH, "//label[@for='gender-radio-1']")
genderRB_Female = (By.XPATH, "//label[@for='gender-radio-2']")
genderRB_Other = (By.XPATH, "//label[@for='gender-radio-3']")

phone_Area = (By.ID, "userNumber")
birthDate_Area = (By.ID, "dateOfBirthInput")
birthDate_Year = (By.XPATH, "//select[@class='react-datepicker__year-select']//option[@value='1992']")
birthDate_Month = (By.XPATH, "//select[@class='react-datepicker__month-select']//option[@value='3']")
birthDate_Day = (By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='17']")
subjects_Area = (By.ID, "subjectsInput")

hobbiesCHB_Sports = (By.XPATH, "//label[@for='hobbies-checkbox-1']")
hobbiesCHB_Reading = (By.XPATH, "//label[@for='hobbies-checkbox-2']")
hobbiesCHB_Music = (By.XPATH, "//label[@for='hobbies-checkbox-3']")

pictureUpload_Btn = (By.ID, "uploadPicture")

currentAddress_Area = (By.ID, "currentAddress")

state_Selector = (By.ID, "react-select-3-input")
stateOptions = (By.XPATH, "//div[@class=' css-1wa3eu0-placeholder']")

city_Selector = (By.ID, "react-select-4-input")
cityOptions = (By.XPATH, "//div[@class=' css-1wa3eu0-placeholder']")

submitBtn = (By.ID, "submit")

popUp = (By.XPATH, "//div[@class='modal-content']")
title_popUp = (By.ID, "example-modal-sizes-title-lg")

popUp_studentName = (By.XPATH, "//td[text()='Ivan Ivanov']")
popUp_studentEmail = (By.XPATH, "//td[text()='Ivanov@gmail.com']")
popUp_studentGender = (By.XPATH, "//td[text()='Male']")
popUp_studentBirthDate = (By.XPATH, "//td[text()='17 April,1992']")
popUp_studentSubjects = (By.XPATH, "//td[text()='Maths']")
popUp_studentHobbies = (By.XPATH, "//td[text()='Sports, Reading, Music']")
popUp_studentPicture = (By.XPATH, "//td[text()='3.png']")
popUp_studentAddress = (By.XPATH, "//td[text()='Moscow']")
popUp_studentStateAndCity = (By.XPATH, "//td[text()='NCR Delhi']")


class registratin_Form(other_Page):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://demoqa.com/automation-practice-form')

    def firstName_Area(self):
        return self.find(firstName_Area)
    
    def lastName_Area(self):
        return self.find(lastName_Area)

    def email_Area(self):
        return self.find(email_Area)

    def genderRB_Male(self):
        return self.find(genderRB_Male)

    def genderRB_Female(self):
        return self.find(genderRB_Female)

    def genderRB_Other(self):
        return self.find(genderRB_Other)

    def phone_Area(self):
        return self.find(phone_Area)

    def birthDate_Area(self):
        return self.find(birthDate_Area)
    
    def birthDate_Year(self):
        return self.find(birthDate_Year)

    def birthDate_Month(self):
        return self.find(birthDate_Month)

    def birthDate_Day(self):
        return self.find(birthDate_Day)

    def subjects_Area(self):
        return self.find(subjects_Area)

    def hobbiesCHB_Sports(self):
        return self.find(hobbiesCHB_Sports)

    def hobbiesCHB_Reading(self):
        return self.find(hobbiesCHB_Reading)

    def hobbiesCHB_Music(self):
        return self.find(hobbiesCHB_Music)

    def pictureUpload_Btn(self):
        return self.find(pictureUpload_Btn)

    def currentAddress_Area(self):
        return self.find(currentAddress_Area)

    def state_Selector(self):
        return self.find(state_Selector)

    def city_Selector(self):
        return self.find(city_Selector)

    def submitBtn(self):
        return self.find(submitBtn)

    def popUp(self):
        return self.find(popUp)

    def title_popUp(self):
        return self.find(title_popUp)
    
    def popUp_studentName(self):
        return self.find(popUp_studentName)

    def popUp_studentEmail(self):
        return self.find(popUp_studentEmail)

    def popUp_studentGender(self):
        return self.find(popUp_studentGender)

    def popUp_studentBirthDate(self):
        return self.find(popUp_studentBirthDate)

    def popUp_studentSubjects(self):
        return self.find(popUp_studentSubjects)

    def popUp_studentHobbies(self):
        return self.find(popUp_studentHobbies)

    def popUp_studentPicture(self):
        return self.find(popUp_studentPicture)

    def popUp_studentAddress(self):
        return self.find(popUp_studentAddress)

    def popUp_studentStateAndCity(self):
        return self.find(popUp_studentStateAndCity)