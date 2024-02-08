import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

def look_for(image, directory):

  options = webdriver.ChromeOptions()
  options.add_experimental_option("detach", True)
  driver = webdriver.Chrome(options=options)

  driver.get("https://www.google.com")

  sleep(5)

  #Images button
  element = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/div[1]/div/div[2]/a")
  element.click()

  sleep(5)

  #Search bar
  element = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
  element.send_keys(image)

  sleep(5)

  #Search button
  element = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button")
  element.click()

  sleep(5)
  
  #Images
  images = driver.find_elements(By.TAG_NAME, "img")
  
  for i, image in enumerate(images):
    image_url = image.get_attribute("src")
    filename = os.path.join(directory, f"image{i+1}.jpg")
    try:
        urllib.request.urlretrieve(image_url, filename)
    except:
        print(f"Error al descargar la imagen")

  driver.quit()
  
look_for("guitarra electrica", "../train_images/guitarras")
look_for("bajo electrico", "../train_images/bajos")
look_for("ukelele instrument", "../train_images/ukeleles")
look_for("banjo instrument", "../train_images/banjos")
look_for("violin", "../train_images/violin")