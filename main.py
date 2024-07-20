from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


#Loading Home Page

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://quora.com")
time.sleep(5)


#Sign in

print(os.environ['file'])
first_line=""
driver.find_element(By.ID, 'email').send_keys(os.environ['email'])
time.sleep(5)
driver.find_element(By.ID, 'password').send_keys(os.environ['password'])
time.sleep(5)
driver.find_element(By.XPATH,
                    '/html/body/div[2]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[4]/button/div').click()

#Loop to post 2 answers
for i in range(2):

    #reading file
    totalfile=open(os.environ['file'], 'r')
    first_line=totalfile.readline()
    totalfile.close()

    #Parsing question_url and answer file
    first_line=first_line.strip()
    question, answer = first_line.split(',')
    answer=answer
    print(question)
    print(answer)

    #reading answer text file
    answer_filetext = os.environ['answer_file']
    print(answer_filetext)
    print(os.path.join(answer_filetext + "\\"+answer))
    answerfile = open(os.path.join(answer_filetext+"\\"+answer), 'r')
    readanswer = answerfile.read()
    print(readanswer)
    answerfile.close()
    time.sleep(5)

    #Load question url
    driver.get(question)

    time.sleep(5)

    #Click on Answer
    driver.find_element(By.XPATH,
                        '//*[@id="mainContent"]/div[1]/div/div[2]/div/div/div[1]/button[1]/div/div[2]/div').click()
    time.sleep(5)

    #Typing Answer

    driver.find_element(By.XPATH,
                        '//*[@id="root"]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div[1]/div/div').send_keys(
        readanswer)
    time.sleep(5)

    #Click Post

    driver.find_element(By.XPATH,
                        '//*[@id="root"]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div/div[2]/button/div/div/div').click()
    time.sleep(5)

    #Get Current Url
    url = driver.current_url
    print(url)

    #Appending question,answer_file
    with open(os.environ['out_file'], 'a') as add:
        add.write(question)
        add.write(",")
        add.write(url)
        add.write("\n")

    #Deleting first line and adding remaining data to file
    with open(os.environ['file'], 'r+') as fp:
        lines = fp.readlines()
        fp.seek(0)
        fp.truncate()
        fp.writelines(lines[1:])


driver.quit()

