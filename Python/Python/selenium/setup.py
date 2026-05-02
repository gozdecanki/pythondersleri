from selenium import webdriver

chrome_driver_path = "D:\myworkspace\drivers\chromedriver_win64"
# chrome_driver_path = "c:\Drivers"

#driver = webdriver.Chrome(executable_path=chrome_driver_path) eski yöntem
driver = webdriver.Chrome()
driver.get("https://sadikturan.com")

driver.close()# sayfa açılır sonra kendisi kapanır

