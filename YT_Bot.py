from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time as t
import playsound
import speech_recognition as sr
from gtts import gTTS
import os


PATH  = "C:\Program Files (x86)\chromedriver.exe"

def speak(text):
		tts = gTTS(text=text, lang="en")
		fliename = "voice.mp3"
		tts.save(fliename)
		playsound.playsound(fliename)
		os.remove("voice.mp3")

def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
		said = ''
		try:
			said = r.recognize_google(audio)
			print(said)
		except Exception as e:
			print("Sorry I didn't get that", e)
		return said

def main():
	speak("Please tell what you want to see or get ")
	word = get_audio()

	driver = webdriver.Chrome(PATH)
		
	driver.get("https:youtube.com")

	search_box  =  driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input")

	search_box.send_keys(word)
	search_box.send_keys(Keys.RETURN)
	t.sleep(2)

	vid = driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a")

	vid.click()


	t.sleep(200)

	driver.quit()

for i in range(300):
	main()










































