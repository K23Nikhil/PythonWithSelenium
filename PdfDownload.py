from selenium import webdriver
from selenium.webdriver.support.select import Select
import selenium.webdriver.support.ui as UI
from selenium.webdriver.common.keys import  Keys
import time
import os
url = "https://jharbhoomi.nic.in/jhrlrmsmis/MISROR_REG2/MISROR_REG2.aspx"
driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://jharbhoomi.nic.in/jhrlrmsmis/MISROR_REG2/MISROR_REG2.aspx")
driver.maximize_window()
inputElement = driver.find_element_by_id("ctl00_ContentPlaceHolder1_rdbtnOption_0").click()
#Select The Jila from dropdown Menu
time.sleep(2)
#select = Select(driver.find_elements_by_id('ctl00_ContentPlaceHolder1_cbo_District_Code'))
distElements = len(driver.find_elements_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$cbo_District_Code']/option"))
print(distElements)

#missingKhata.close()

#Get the All Distict Name and itterate 1....last
for distElement in range(1, distElements):
    #Select The Drop Down Menu
    Select(driver.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$cbo_District_Code']")).select_by_index(distElement)

    time.sleep(2)   #Wait for 2 second

    #Check if distict is 1 then it will add 1 as i am getting Select One on 1 index
    if distElement == 1:
        distdir = driver.find_element_by_xpath("//select[@name = 'ctl00$ContentPlaceHolder1$cbo_District_Code']/option" + "[" + str(distElement + 1) + "]").get_attribute('text')
    else:
        distdir = driver.find_element_by_xpath( "//select[@name = 'ctl00$ContentPlaceHolder1$cbo_District_Code']/option" + "[" + str(distElement ) + "]").get_attribute('text')

    # Select Distict  Name in text
    Select(driver.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$cbo_District_Code']")).select_by_index(distElement)
    time.sleep(2)

    # Get the Anchal Lenth for itterate the loop
    AnchalElements = len(driver.find_elements_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$cbo_Circle_Code']/option"))
    time.sleep(2)

    # Start the loop for Anchal
    for anchalElement in range(2, AnchalElements):
        Select(driver.find_element_by_xpath( "//select[@name='ctl00$ContentPlaceHolder1$cbo_Circle_Code']")).select_by_index(anchalElement)
        time.sleep(2)
        # Get the path to create the Sub directory
        anchaldir = driver.find_element_by_xpath("//select[@name = 'ctl00$ContentPlaceHolder1$cbo_Circle_Code']/option" + "[" + str(anchalElement) + "]").get_attribute('text')
        #Get the Halka Element length
        halkaElements = len(driver.find_elements_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ddlHalkaCode']/option"))


        #Start Loop For Halka
        for halkaElement in range(1, halkaElements):
            Select(driver.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ddlHalkaCode']")).select_by_index(halkaElement)
            time.sleep(2)
            halkaDir = driver.find_element_by_xpath( "//select[@name = 'ctl00$ContentPlaceHolder1$ddlHalkaCode']/option" + "[" + str(anchalElement) + "]").get_attribute('text')

            time.sleep(2)
            #Start Loop for mauja
            maijaElements = len(driver.find_elements_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ddlHalkaCode']/option"))
            for mujaElement in range(1, maijaElements):
                Select(driver.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ddlMaujaCode']")).select_by_index(mujaElement)
                time.sleep(2)
                if mujaElement == 1:
                    maujaDir = driver.find_element_by_xpath("//select[@name = 'ctl00$ContentPlaceHolder1$ddlMaujaCode']/option" + "[" + str(mujaElement + 1 ) + "]").get_attribute('text')
                else:
                    maujaDir = driver.find_element_by_xpath("//select[@name = 'ctl00$ContentPlaceHolder1$ddlMaujaCode']/option" + "[" + str(mujaElement + 1) + "]").get_attribute('text')

                #Khata Element
                khataElements = len(driver.find_elements_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ddlKhataNo']/option"))
                print("mauja Directory Name",maujaDir)

                for khataElement in range(1, khataElements):
                    Select(driver.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ddlKhataNo']")).select_by_index(khataElement)
                    time.sleep(2)
                    Select(driver.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ddlLandType']")).select_by_visible_text("रैयती")
                    time.sleep(2)
                    driver.find_element_by_xpath("//input[@name='ctl00$ContentPlaceHolder1$btnKhatiyan']").click()
                    time.sleep(2)
                    print("Khata Element calll.............!!")

                    #Check if page is time to load
                    if len(driver.find_elements_by_xpath("//img[normalize-space(text())='Updating Page ......']")) >0:
                        time.sleep(2)
                    #Check if record is doesn't exit it will continue for other loop
                    if len(driver.find_elements_by_xpath("//span[text()='Record does not exist']")) > 0:
                        print("JIla is:" + str(distdir) + "  "
                                               "Anchal Name:" + str(anchaldir) +
                                               "Halka Name:"+ str(halkaDir) +
                                               "Maija Name  :" + str(maujaDir) +
                                               "Khata Number :"+ str(khataElement))
                        with open('MissingKhata.txt', 'a', encoding='utf-8') as missingKhata:
                            missingKhata.write("JIla is:" + str(distdir) + "  "
                                               "Anchal Name:" + str(anchaldir) +
                                               "Halka Name:"+ str(halkaDir) +
                                               "Maija Name  :" + str(maujaDir) +
                                               "Khata Number :"+ str(khataElement))
                            missingKhata.close()
                        continue

                    else:
                            dir = os.getcwd() + "\\" + str(distdir) + "\\" + str(anchaldir) + "\\" + str(halkaDir) + "\\" + str(maujaDir)
                            if os.path.exists(dir):
                                print("Directory Already exists..........!!")
                                pass
                            else:
                                os.makedirs(dir)
                                print("Dir created...........!!")


                        #findele = driver.find_element_by_xpath("//input[@id = 'ImagePrint']").click()
                            fileName = dir + "\\" +str(khataElement) +".html"
                            print("File Name ", fileName)
                            time.sleep(2)
                            with open(fileName, 'w', encoding='utf-8') as file:
                                file.write(driver.page_source)
                                print("File Created........!!")
                            driver.switch_to_window(driver.window_handles[1])
                            time.sleep(2)
                            driver.find_element_by_xpath("//input[@id = 'Imageback']").click()
                            driver.switch_to_window(driver.window_handles[0])


driver.quit()
missingKhata.close()