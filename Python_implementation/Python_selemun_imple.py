#此版本为暴力直接模拟点击法，为初版，尔后再来完善

import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

#//Warning由于vpn网页有检查步骤，因此开启无头模式可能无法正常运行
# chrome_options=webdriver.Chrome.add_argument(headless') 

chrome_driver = webdriver.Chrome()
wait = WebDriverWait(chrome_driver, 3)
#username为个人的用户名
#password为个人用户密码
username = "xxxxxx"
password = "xxxxxx"


def vpn_login():
	site = "https://webvpn1.jiangnan.edu.cn/login"
	chrome_driver.get(site)
	username_site = chrome_driver.find_element_by_id("user_name")
	username_site.send_keys(username)
	password_site = chrome_driver.find_element_by_xpath("//*[@id=\"form\"]/div[3]/div/input")
	password_site.send_keys(password)
	Clk = chrome_driver.find_element_by_xpath('//*[@id="login"]')
	Clk.click()

#不要忘记登出
def vpn_logout():
	site="https://webvpn1.jiangnan.edu.cn/logout"
	chrome_driver.get(site)


#登陆返校通每日打卡，site为登陆返校通的网址，可以抓包获得，中间"xxxxxx"目测是通过对每个人信息进行加密运算获得的一个长字符串
def fxt_login():
	site = "https://webvpn1.jiangnan.edu.cn/http/xxxxxx/passport/login"
	chrome_driver.get(site)
	username_site = chrome_driver.find_element_by_xpath(
		'/html/body/div[2]/div/div/div/div/div/div/div/div/form/div[1]/div/input')
	username_site.send_keys(username)
	password_site = chrome_driver.find_element_by_xpath(
		'/html/body/div[2]/div/div/div/div/div/div/div/div/form/div[2]/div/input')
	password_site.send_keys(password)
	Clk = chrome_driver.find_element_by_xpath(
		'/html/body/div[2]/div/div/div/div/div/div/div/div/form/div[3]/div/button')
	Clk.click()

#"xxxxxx"意义同上
def fxt_fill():
	site = "https://webvpn1.jiangnan.edu.cn/http/xxxxxx/daily/fill"
	chrome_driver.get(site)
	Clk = chrome_driver.find_element_by_xpath('//*[@id="form"]/div[20]/div/button')
	Clk.click()


if __name__ == '__main__':
	vpn_login()
	time.sleep(1)
	fxt_login()

	fxt_fill()
	vpn_logout()
  #记得关闭Chrome窗口，以免窗口堆积
	chrome_driver.close()
	print("签到成功！")
