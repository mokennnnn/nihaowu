#-*-  coding:utf-8 -*-
#主要用来测试selenium使用phantomJs

#导入webdriver
from selenium import webdriver
import time

#要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import hashlib
import pymysql.cursors
#调用环境变量指定的PhantomJS浏览器创建浏览器对象

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"
)
con = pymysql.connect(host="sdm399798644.my3w.com", port=3306, user="sdm399798644", password="523545286",
                      db="sdm399798644_db", charset='utf8', cursorclass=pymysql.cursors.DictCursor)

cursor = con.cursor()

try:
    driver = webdriver.PhantomJS(desired_capabilities=dcap)
except:
    print('error')
driver.set_window_size(1366, 768)
driver.set_page_load_timeout(3)
driver.set_script_timeout(1)

#如果没有在环境变量指定PhantomJS位置
#driver = webdriver.PhantomJS(executable_path = "./phantomjs")

#get方法会一直等到页面加载，然后才会继续程序，通常测试会在这里选择time.sleep(2)



#生成页面快照并保存
def insert():


    try:
        driver.get("https://www.nihaowua.com/")

        data = driver.find_element_by_xpath("/html/body/div[@class='container']/section/div/p");

        print(data.text)
        sql = "insert `nihaowu` (`url`,`content`) values ('%s','%s')" % (driver.current_url, data.text);
        print(sql)
        cursor.execute(sql);
        result = cursor.fetchone();
        sql = "select count(`content`) from `nihaowu`";
        cursor.execute(sql);
        result = cursor.fetchone();
        print(result);
    except:
        print('获取失败');




insert()

# # id="su"是百度搜索按钮，click()是模拟点击
# for index in range(0,40):
#     print(index)
#     driver.find_element_by_id('loadMore').click()
#     try:
#         element = WebDriverWait(driver, 20).until(
#             EC.text_to_be_present_in_element((By.ID, "loadMore"), '加载更多')
#         )
#     finally:
#        print('捕获成功');
#
#
# #获取新的页面快照
#
# fileObject = open('sampleList.txt', 'w')
#
# elem = driver.find_elements_by_class_name('upload-txt')
# for single in elem:
#     print(single.text)
#     new_context = single.text + '\n'
#     fileObject.write(new_context)
#
#
# fileObject.close()

#获取当前url
print(driver.current_url)

driver.quit()