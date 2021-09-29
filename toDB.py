from selenium import webdriver

movieNo = 5411524
broswer = webdriver.Chrome("../../chromedriver.exe")
broswer.get("https://serieson.naver.com/movie/detail.nhn?productNo="+str(movieNo))
try:
    index = 1
    for e in range(1, 5):
        element = broswer.find_element_by_xpath('//*[@id="cbox_module"]/div/div[5]/ul/li['+str(index)+']/div[1]/div/div[2]')
        index += 1
        print(element.text)
except:
    print("error")

broswer.close()




