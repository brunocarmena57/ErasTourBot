import asyncio
import concurrent.futures
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

# Define your selenium task as a function
def selenium_task(i, posx, posy):
    driver = webdriver.Chrome(options=options)
    driver.get("https://taylor-swift-sp.sales.ticketsforfun.com.br")
    driver.set_window_position(posx, posy)
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
    return driver

# Create a coroutine that uses a ThreadPoolExecutor to run the selenium task
async def main():
    posx = 0
    posy = 0
    with concurrent.futures.ThreadPoolExecutor() as executor:
        loop = asyncio.get_event_loop()
        futures = []
        for i in range(number_of_windows):
            futures.append(loop.run_in_executor(executor, selenium_task, i, posx, posy))
            posx += 470
            if posx + 470 > 1450:
                posx = 0
                posy += 400
                if posy + 400 > 1280:
                    posy = 0
        for response in await asyncio.gather(*futures):
            pass  # Do something with the response

# Run the asyncio event loop
asyncio.run(main())
