import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

number_of_windows = int(input("number of windows "))
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--window-size=400,400")

print("ncs")

driver_list = []
posx = 0
posy = 0


for i in range(number_of_windows):
    driver = webdriver.Chrome(options=options)
    driver.get("https://taylor-swift-sp.sales.ticketsforfun.com.br")
    driver.set_window_position(posx, posy)
    
    posx += 470
    if posx + 470 > 1450:
        posx = 0
        posy += 400
        if posy + 400 > 1280:
            posy = 0

        click_x = 100
    click_y = 200
    pyautogui.click(click_x, click_y)
    
    driver_list.append(driver)
    cookies = driver.get_cookie("Queue-it")
    if cookies is not None:
        print("--------------------")
        print("Browser ID "+str(i+1)+": " + cookies["value"])
        print("--------------------")
    else:
        print("--------------------")
        print("Browser ID "+str(i+1)+": Cookie not found")
        print("--------------------")
