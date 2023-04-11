from selenium import webdriver
import os.path
import time

os.system("cls")
os.system("title Made By J_AFF#1652")

token = ""
while True:
    if not token:
        os.system("cls")
        token = input("\n Enter Token : ")
    else:
        break

driver_path = "msedgedriver.exe"

# Optionen zum Starten des Edge-Browsers
options = webdriver.EdgeOptions()
options.use_chromium = True
options.add_experimental_option("detach", True)
driver = webdriver.Edge(executable_path=driver_path, options=options)
driver.maximize_window()

script = """
        function login(token) {
        setInterval(() => {
        document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
        }, 50);
        setTimeout(() => {
        location.reload();
        }, 2500);
        }   
        """

driver.get("https://discordapp.com/login")
driver.execute_script(script + f'\nlogin("{token}")')

while True:
    time.sleep(10)
    os.system("cls")
    os.system("echo Dont close the window!")
    os.system("echo If you are not logged in then the token is invalid..")
