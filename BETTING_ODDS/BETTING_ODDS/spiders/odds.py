# -*- coding: utf-8 -*-
import scrapy
import json
import os

from BETTING_ODDS import settings
from BETTING_ODDS.items import BettingOddsItem
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from scrapy import signals
import time
from scrapy.xlib.pydispatch import dispatcher
from collections import OrderedDict


class OddsSpider(scrapy.Spider):
	name = "odds"
	start_urls = settings.START_URL
	
	def __init__(self):
		dispatcher.connect(self.spider_closed, signals.spider_closed)
		self.driver = webdriver.PhantomJS()
		self.driver.maximize_window()
		if not os.path.exists('RESULTS'):
			os.makedirs('RESULTS')
		return
		
	def spider_closed(self, spider):
		# self.json_file.close()
		return
		
		
	def parse(self, response):
		game = []
		game = OrderedDict([('gameID',[]), ('oddsFlow',[])])
		gameID = response.url
		gameID = gameID.strip('/').split('-')[-1]
		
		# Create JSON file for current Game
		self.json_file = open('./RESULTS/' + gameID + '.json', 'wb')
		

		pinnacle = []
		pinnacle = OrderedDict([('full', []), ('1stHalf', []), ('2ndHalf', []), ('1stQuarter', []), ('2ndQuarter', []), ('3rdQuarter', []), ('4thQuarter', [])])
		FiveDimes = []
		FiveDimes = OrderedDict([('full', []), ('1stHalf', []), ('2ndHalf', []), ('1stQuarter', []), ('2ndQuarter', []), ('3rdQuarter', []), ('4thQuarter', [])])
		BookMaker = []
		BookMaker = OrderedDict([('full', []), ('1stHalf', []), ('2ndHalf', []), ('1stQuarter', []), ('2ndQuarter', []), ('3rdQuarter', []), ('4thQuarter', [])])
		BetOnline = []
		BetOnline = OrderedDict([('full', []), ('1stHalf', []), ('2ndHalf', []), ('1stQuarter', []), ('2ndQuarter', []), ('3rdQuarter', []), ('4thQuarter', [])])
		oddsFlow = []
		oddsFlow = OrderedDict([('5Dimes', []), ('pinnacle', []), ('BookMaker', []), ('BetOnline', [])])
		
		First_spread1 = []
		First_spread2 = []
		First_spread3 = []
		First_spread4 = []
		First_spread5 = []
		First_spread6 = []
		First_spread7 = []
		
		Sec_spread1 = []
		Sec_spread2 = []
		Sec_spread3 = []
		Sec_spread4 = []
		Sec_spread5 = []
		Sec_spread6 = []
		Sec_spread7 = []
		
		Third_spread1 = []
		Third_spread2 = []
		Third_spread3 = []
		Third_spread4 = []
		Third_spread5 = []
		Third_spread6 = []
		Third_spread7 = []
		
		spread1 = []
		spread2 = []
		spread3 = []
		spread4 = []
		spread5 = []
		spread6 = []
		spread7 = []
		
		First_moneyLine1 = []
		First_moneyLine2 = []
		First_moneyLine3 = []
		First_moneyLine4 = []
		First_moneyLine5 = []
		First_moneyLine6 = []
		First_moneyLine7 = []
		
		Sec_moneyLine1 = []
		Sec_moneyLine2 = []
		Sec_moneyLine3 = []
		Sec_moneyLine4 = []
		Sec_moneyLine5 = []
		Sec_moneyLine6 = []
		Sec_moneyLine7 = []
		
		Third_moneyLine1 = []
		Third_moneyLine2 = []
		Third_moneyLine3 = []
		Third_moneyLine4 = []
		Third_moneyLine5 = []
		Third_moneyLine6 = []
		Third_moneyLine7 = []
		
		moneyLine1 = []
		moneyLine2 = []
		moneyLine3 = []
		moneyLine4 = []
		moneyLine5 = []
		moneyLine6 = []
		moneyLine7 = []
		
		First_totalPoint1 = []
		First_totalPoint2 = []
		First_totalPoint3 = []
		First_totalPoint4 = []
		First_totalPoint5 = []
		First_totalPoint6 = []
		First_totalPoint7 = []
		
		Sec_totalPoint1 = []
		Sec_totalPoint2 = []
		Sec_totalPoint3 = []
		Sec_totalPoint4 = []
		Sec_totalPoint5 = []
		Sec_totalPoint6 = []
		Sec_totalPoint7 = []
		
		
		Third_totalPoint1 = []
		Third_totalPoint2 = []
		Third_totalPoint3 = []
		Third_totalPoint4 = []
		Third_totalPoint5 = []
		Third_totalPoint6 = []
		Third_totalPoint7 = []
		
		totalPoint1 = []
		totalPoint2 = []
		totalPoint3 = []
		totalPoint4 = []
		totalPoint5 = []
		totalPoint6 = []
		totalPoint7 = []
		
		Five_Dimes = "4"
		PINN_ACLE = "5"
		Book_Maker = "6"
		BET_ONLINE = "7"
		
		i = "7"
		i = str(i)
		
		full1 = []
		full1 = OrderedDict([('SPREAD', []), ('MONEY LINE', []), ('TOTAL POINT', [])])
		FirstHalf1 = []
		FirstHalf1 = OrderedDict([('SPREAD', []), ('MONEY LINE', []), ('TOTAL POINT', [])])
		SecondHalf1 = []
		SecondHalf1 = OrderedDict([('SPREAD', []), ('MONEY LINE', []), ('TOTAL POINT', [])])
		FirstQuarter1 = []
		FirstQuarter1 = OrderedDict([('SPREAD', []), ('MONEY LINE', []), ('TOTAL POINT', [])])
		SecondQuarter1 = []
		SecondQuarter1 = OrderedDict([('SPREAD', []), ('MONEY LINE', []), ('TOTAL POINT', [])])
		ThirdQuarter1 = []
		ThirdQuarter1 = OrderedDict([('SPREAD', []), ('MONEY LINE', []), ('TOTAL POINT', [])])
		FourthQuarter1 = []
		FourthQuarter1 = OrderedDict([('SPREAD', []), ('MONEY LINE', []), ('TOTAL POINT', [])])
		self.driver.get(response.url)
		self.driver.find_element_by_xpath('//div[@class="event-grid event-category"][1]/div[2]/div/div/div/div/div/div/div/div[1]/div[' + i + ']/div[1]').click()
		time.sleep(4)
		self.driver.current_window_handle
		for spreads in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[2]/div[2]/div/div[@class="jspPane"]/table//tr'):
			spreads_name = {}
			spreads_name = OrderedDict([('date', []), ('Time', []), ('homeSpread', []), ('awaySpread', [])])
			Time_Table = spreads.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = spreads.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = spreads.find_element_by_xpath('./td[3]').get_attribute('textContent')
			spreads_name['date'] = date
			spreads_name['Time'] = Time
			spreads_name['homeSpread'] = homeSpread
			spreads_name['awaySpread'] = awaySpread
			First_spread1.append(spreads_name)
		for money_Line in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[3]/div[2]/div/div[@class="jspPane"]/table//tr'):
			moneyLine_name = {}
			moneyLine_name = OrderedDict([('date', []), ('Time', []), ('homeMoneyLine', []), ('awayMoneyLine', [])])
			Time_Table = money_Line.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = money_Line.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = money_Line.find_element_by_xpath('./td[3]').get_attribute('textContent')
			moneyLine_name['date'] = date
			moneyLine_name['Time'] = Time
			moneyLine_name['homeMoneyLine'] = homeSpread
			moneyLine_name['awayMoneyLine'] = awaySpread
			First_moneyLine1.append(moneyLine_name)
		for total_Point in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[4]/div[2]/div/div[@class="jspPane"]/table//tr'):
			totalPoint_name = {}
			totalPoint_name = OrderedDict([('date', []), ('Time', []), ('underTotalPoint', []), ('overTotalPoint', [])])
			Time_Table = total_Point.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = total_Point.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = total_Point.find_element_by_xpath('./td[3]').get_attribute('textContent')
			totalPoint_name['date'] = date
			totalPoint_name['Time'] = Time
			totalPoint_name['underTotalPoint'] = homeSpread
			totalPoint_name['overTotalPoint'] = awaySpread
			First_totalPoint1.append(totalPoint_name)
		
		self.driver.get(response.url)
		self.driver.find_element_by_xpath('//div[@class="event-grid event-category"][2]/div[2]/div/div/div/div/div/div/div/div[1]/div[' + i + ']/div[1]').click()
		time.sleep(4)
		self.driver.current_window_handle
		for spreads in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[2]/div[2]/div/div[@class="jspPane"]/table//tr'):
			spreads_name = {}
			spreads_name = OrderedDict([('date', []), ('Time', []), ('homeSpread', []), ('awaySpread', [])])
			Time_Table = spreads.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = spreads.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = spreads.find_element_by_xpath('./td[3]').get_attribute('textContent')
			spreads_name['date'] = date
			spreads_name['Time'] = Time
			spreads_name['homeSpread'] = homeSpread
			spreads_name['awaySpread'] = awaySpread
			First_spread2.append(spreads_name)
		for money_Line in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[3]/div[2]/div/div[@class="jspPane"]/table//tr'):
			moneyLine_name = {}
			moneyLine_name = OrderedDict([('date', []), ('Time', []), ('homeMoneyLine', []), ('awayMoneyLine', [])])
			Time_Table = money_Line.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = money_Line.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = money_Line.find_element_by_xpath('./td[3]').get_attribute('textContent')
			moneyLine_name['date'] = date
			moneyLine_name['Time'] = Time
			moneyLine_name['homeMoneyLine'] = homeSpread
			moneyLine_name['awayMoneyLine'] = awaySpread
			First_moneyLine2.append(moneyLine_name)
		for total_Point in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[4]/div[2]/div/div[@class="jspPane"]/table//tr'):
			totalPoint_name = {}
			totalPoint_name = OrderedDict([('date', []), ('Time', []), ('underTotalPoint', []), ('overTotalPoint', [])])
			Time_Table = total_Point.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = total_Point.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = total_Point.find_element_by_xpath('./td[3]').get_attribute('textContent')
			totalPoint_name['date'] = date
			totalPoint_name['Time'] = Time
			totalPoint_name['underTotalPoint'] = homeSpread
			totalPoint_name['overTotalPoint'] = awaySpread
			First_totalPoint2.append(totalPoint_name)
			
		self.driver.get(response.url)
		self.driver.find_element_by_xpath('//div[@class="event-grid event-category"][3]/div[2]/div/div/div/div/div/div/div/div[1]/div[' + i + ']/div[1]').click()
		time.sleep(4)
		self.driver.current_window_handle
		for spreads in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[2]/div[2]/div/div[@class="jspPane"]/table//tr'):
			spreads_name = {}
			spreads_name = OrderedDict([('date', []), ('Time', []), ('homeSpread', []), ('awaySpread', [])])
			Time_Table = spreads.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = spreads.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = spreads.find_element_by_xpath('./td[3]').get_attribute('textContent')
			spreads_name['date'] = date
			spreads_name['Time'] = Time
			spreads_name['homeSpread'] = homeSpread
			spreads_name['awaySpread'] = awaySpread
			First_spread3.append(spreads_name)
		for money_Line in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[3]/div[2]/div/div[@class="jspPane"]/table//tr'):
			moneyLine_name = {}
			moneyLine_name = OrderedDict([('date', []), ('Time', []), ('homeMoneyLine', []), ('awayMoneyLine', [])])
			Time_Table = money_Line.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = money_Line.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = money_Line.find_element_by_xpath('./td[3]').get_attribute('textContent')
			moneyLine_name['date'] = date
			moneyLine_name['Time'] = Time
			moneyLine_name['homeMoneyLine'] = homeSpread
			moneyLine_name['awayMoneyLine'] = awaySpread
			First_moneyLine3.append(moneyLine_name)
		for total_Point in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[4]/div[2]/div/div[@class="jspPane"]/table//tr'):
			totalPoint_name = {}
			totalPoint_name = OrderedDict([('date', []), ('Time', []), ('underTotalPoint', []), ('overTotalPoint', [])])
			Time_Table = total_Point.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = total_Point.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = total_Point.find_element_by_xpath('./td[3]').get_attribute('textContent')
			totalPoint_name['date'] = date
			totalPoint_name['Time'] = Time
			totalPoint_name['underTotalPoint'] = homeSpread
			totalPoint_name['overTotalPoint'] = awaySpread
			First_totalPoint3.append(totalPoint_name)
			
		self.driver.get(response.url)
		self.driver.find_element_by_xpath('//div[@class="event-grid event-category"][4]/div[2]/div/div/div/div/div/div/div/div[1]/div[' + i + ']/div[1]').click()
		time.sleep(4)
		self.driver.current_window_handle
		for spreads in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[2]/div[2]/div/div[@class="jspPane"]/table//tr'):
			spreads_name = {}
			spreads_name = OrderedDict([('date', []), ('Time', []), ('homeSpread', []), ('awaySpread', [])])
			Time_Table = spreads.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = spreads.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = spreads.find_element_by_xpath('./td[3]').get_attribute('textContent')
			spreads_name['date'] = date
			spreads_name['Time'] = Time
			spreads_name['homeSpread'] = homeSpread
			spreads_name['awaySpread'] = awaySpread
			First_spread4.append(spreads_name)
		for money_Line in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[3]/div[2]/div/div[@class="jspPane"]/table//tr'):
			moneyLine_name = {}
			moneyLine_name = OrderedDict([('date', []), ('Time', []), ('homeMoneyLine', []), ('awayMoneyLine', [])])
			Time_Table = money_Line.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = money_Line.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = money_Line.find_element_by_xpath('./td[3]').get_attribute('textContent')
			moneyLine_name['date'] = date
			moneyLine_name['Time'] = Time
			moneyLine_name['homeMoneyLine'] = homeSpread
			moneyLine_name['awayMoneyLine'] = awaySpread
			First_moneyLine4.append(moneyLine_name)
		for total_Point in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[4]/div[2]/div/div[@class="jspPane"]/table//tr'):
			totalPoint_name = {}
			totalPoint_name = OrderedDict([('date', []), ('Time', []), ('underTotalPoint', []), ('overTotalPoint', [])])
			Time_Table = total_Point.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = total_Point.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = total_Point.find_element_by_xpath('./td[3]').get_attribute('textContent')
			totalPoint_name['date'] = date
			totalPoint_name['Time'] = Time
			totalPoint_name['underTotalPoint'] = homeSpread
			totalPoint_name['overTotalPoint'] = awaySpread
			First_totalPoint4.append(totalPoint_name)
			
		self.driver.get(response.url)
		self.driver.find_element_by_xpath('//div[@class="event-grid event-category"][5]/div[2]/div/div/div/div/div/div/div/div[1]/div[' + i + ']/div[1]').click()
		time.sleep(4)
		self.driver.current_window_handle
		for spreads in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[2]/div[2]/div/div[@class="jspPane"]/table//tr'):
			spreads_name = {}
			spreads_name = OrderedDict([('date', []), ('Time', []), ('homeSpread', []), ('awaySpread', [])])
			Time_Table = spreads.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = spreads.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = spreads.find_element_by_xpath('./td[3]').get_attribute('textContent')
			spreads_name['date'] = date
			spreads_name['Time'] = Time
			spreads_name['homeSpread'] = homeSpread
			spreads_name['awaySpread'] = awaySpread
			First_spread5.append(spreads_name)
		for money_Line in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[3]/div[2]/div/div[@class="jspPane"]/table//tr'):
			moneyLine_name = {}
			moneyLine_name = OrderedDict([('date', []), ('Time', []), ('homeMoneyLine', []), ('awayMoneyLine', [])])
			Time_Table = money_Line.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = money_Line.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = money_Line.find_element_by_xpath('./td[3]').get_attribute('textContent')
			moneyLine_name['date'] = date
			moneyLine_name['Time'] = Time
			moneyLine_name['homeMoneyLine'] = homeSpread
			moneyLine_name['awayMoneyLine'] = awaySpread
			First_moneyLine5.append(moneyLine_name)
		for total_Point in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[4]/div[2]/div/div[@class="jspPane"]/table//tr'):
			totalPoint_name = {}
			totalPoint_name = OrderedDict([('date', []), ('Time', []), ('underTotalPoint', []), ('overTotalPoint', [])])
			Time_Table = total_Point.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = total_Point.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = total_Point.find_element_by_xpath('./td[3]').get_attribute('textContent')
			totalPoint_name['date'] = date
			totalPoint_name['Time'] = Time
			totalPoint_name['underTotalPoint'] = homeSpread
			totalPoint_name['overTotalPoint'] = awaySpread
			First_totalPoint5.append(totalPoint_name)
			
		self.driver.get(response.url)
		self.driver.find_element_by_xpath('//div[@class="event-grid event-category"][6]/div[2]/div/div/div/div/div/div/div/div[1]/div[' + i + ']/div[1]').click()
		time.sleep(4)
		self.driver.current_window_handle
		for spreads in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[2]/div[2]/div/div[@class="jspPane"]/table//tr'):
			spreads_name = {}
			spreads_name = OrderedDict([('date', []), ('Time', []), ('homeSpread', []), ('awaySpread', [])])
			Time_Table = spreads.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = spreads.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = spreads.find_element_by_xpath('./td[3]').get_attribute('textContent')
			spreads_name['date'] = date
			spreads_name['Time'] = Time
			spreads_name['homeSpread'] = homeSpread
			spreads_name['awaySpread'] = awaySpread
			First_spread6.append(spreads_name)
		for money_Line in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[3]/div[2]/div/div[@class="jspPane"]/table//tr'):
			moneyLine_name = {}
			moneyLine_name = OrderedDict([('date', []), ('Time', []), ('homeMoneyLine', []), ('awayMoneyLine', [])])
			Time_Table = money_Line.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = money_Line.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = money_Line.find_element_by_xpath('./td[3]').get_attribute('textContent')
			moneyLine_name['date'] = date
			moneyLine_name['Time'] = Time
			moneyLine_name['homeMoneyLine'] = homeSpread
			moneyLine_name['awayMoneyLine'] = awaySpread
			First_moneyLine6.append(moneyLine_name)
		for total_Point in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[4]/div[2]/div/div[@class="jspPane"]/table//tr'):
			totalPoint_name = {}
			totalPoint_name = OrderedDict([('date', []), ('Time', []), ('underTotalPoint', []), ('overTotalPoint', [])])
			Time_Table = total_Point.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = total_Point.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = total_Point.find_element_by_xpath('./td[3]').get_attribute('textContent')
			totalPoint_name['date'] = date
			totalPoint_name['Time'] = Time
			totalPoint_name['underTotalPoint'] = homeSpread
			totalPoint_name['overTotalPoint'] = awaySpread
			First_totalPoint6.append(totalPoint_name)
			
		self.driver.get(response.url)
		self.driver.find_element_by_xpath('//div[@class="event-grid event-category"][7]/div[2]/div/div/div/div/div/div/div/div[1]/div[' + i + ']/div[1]').click()
		time.sleep(4)
		self.driver.current_window_handle
		for spreads in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[2]/div[2]/div/div[@class="jspPane"]/table//tr'):
			spreads_name = {}
			spreads_name = OrderedDict([('date', []), ('Time', []), ('homeSpread', []), ('awaySpread', [])])
			Time_Table = spreads.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = spreads.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = spreads.find_element_by_xpath('./td[3]').get_attribute('textContent')
			spreads_name['date'] = date
			spreads_name['Time'] = Time
			spreads_name['homeSpread'] = homeSpread
			spreads_name['awaySpread'] = awaySpread
			First_spread7.append(spreads_name)
		for money_Line in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[3]/div[2]/div/div[@class="jspPane"]/table//tr'):
			moneyLine_name = {}
			moneyLine_name = OrderedDict([('date', []), ('Time', []), ('homeMoneyLine', []), ('awayMoneyLine', [])])
			Time_Table = money_Line.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = money_Line.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = money_Line.find_element_by_xpath('./td[3]').get_attribute('textContent')
			moneyLine_name['date'] = date
			moneyLine_name['Time'] = Time
			moneyLine_name['homeMoneyLine'] = homeSpread
			moneyLine_name['awayMoneyLine'] = awaySpread
			First_moneyLine7.append(moneyLine_name)
		for total_Point in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[4]/div[2]/div/div[@class="jspPane"]/table//tr'):
			totalPoint_name = {}
			totalPoint_name = OrderedDict([('date', []), ('Time', []), ('underTotalPoint', []), ('overTotalPoint', [])])
			Time_Table = total_Point.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = total_Point.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = total_Point.find_element_by_xpath('./td[3]').get_attribute('textContent')
			totalPoint_name['date'] = date
			totalPoint_name['Time'] = Time
			totalPoint_name['underTotalPoint'] = homeSpread
			totalPoint_name['overTotalPoint'] = awaySpread
			First_totalPoint7.append(totalPoint_name)
	
		full1.update({'SPREAD':First_spread1, 'MONEY LINE':First_moneyLine1, 'TOTAL POINT':First_totalPoint1})
		FirstHalf1.update({'SPREAD':First_spread2, 'MONEY LINE':First_moneyLine2, 'TOTAL POINT':First_totalPoint2})
		SecondHalf1.update({'SPREAD':First_spread3, 'MONEY LINE':First_moneyLine3, 'TOTAL POINT':First_totalPoint3})
		FirstQuarter1.update({'SPREAD':First_spread4, 'MONEY LINE':First_moneyLine4, 'TOTAL POINT':First_totalPoint4})
		SecondQuarter1.update({'SPREAD':First_spread5, 'MONEY LINE':First_moneyLine5, 'TOTAL POINT':First_totalPoint5})
		ThirdQuarter1.update({'SPREAD':First_spread6, 'MONEY LINE':First_moneyLine6, 'TOTAL POINT':First_totalPoint6})
		FourthQuarter1.update({'SPREAD':First_spread7, 'MONEY LINE':First_moneyLine7, 'TOTAL POINT':First_totalPoint7})
		BetOnline.update({'full':[full1], '1stHalf':[FirstHalf1], '2ndHalf':[SecondHalf1], '1stQuarter':[FirstQuarter1],'2ndQuarter':[SecondQuarter1],'3rdQuarter':[ThirdQuarter1], '4thQuarter':[FourthQuarter1]})
		#####################################################################
		
		
		
		
		i = "5"
		i = str(i)
		full2 = []
		full2 = OrderedDict([('SPREAD', []), ('MONEY LINE', []), ('TOTAL POINT', [])])
		FirstHalf2 = []
		FirstHalf2 = OrderedDict([('SPREAD', []), ('MONEY LINE', []), ('TOTAL POINT', [])])
		SecondHalf2 = []
		SecondHalf2 = OrderedDict([('SPREAD', []), ('MONEY LINE', []), ('TOTAL POINT', [])])
		FirstQuarter2 = []
		FirstQuarter2 = OrderedDict([('SPREAD', []), ('MONEY LINE', []), ('TOTAL POINT', [])])
		SecondQuarter2 = []
		SecondQuarter2 = OrderedDict([('SPREAD', []), ('MONEY LINE', []), ('TOTAL POINT', [])])
		ThirdQuarter2 = []
		ThirdQuarter2 = OrderedDict([('SPREAD', []), ('MONEY LINE', []), ('TOTAL POINT', [])])
		FourthQuarter2 = []
		FourthQuarter2 = OrderedDict([('SPREAD', []), ('MONEY LINE', []), ('TOTAL POINT', [])])
		self.driver.get(response.url)
		self.driver.find_element_by_xpath('//div[@class="event-grid event-category"][1]/div[2]/div/div/div/div/div/div/div/div[1]/div[' + i + ']/div[1]').click()
		time.sleep(4)
		self.driver.current_window_handle
		for spreads in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[2]/div[2]/div/div[@class="jspPane"]/table//tr'):
			spreads_name = {}
			spreads_name = OrderedDict([('date', []), ('Time', []), ('homeSpread', []), ('awaySpread', [])])
			Time_Table = spreads.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = spreads.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = spreads.find_element_by_xpath('./td[3]').get_attribute('textContent')
			spreads_name['date'] = date
			spreads_name['Time'] = Time
			spreads_name['homeSpread'] = homeSpread
			spreads_name['awaySpread'] = awaySpread
			spread1.append(spreads_name)
		for money_Line in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[3]/div[2]/div/div[@class="jspPane"]/table//tr'):
			moneyLine_name = {}
			moneyLine_name = OrderedDict([('date', []), ('Time', []), ('homeMoneyLine', []), ('awayMoneyLine', [])])
			Time_Table = money_Line.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = money_Line.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = money_Line.find_element_by_xpath('./td[3]').get_attribute('textContent')
			moneyLine_name['date'] = date
			moneyLine_name['Time'] = Time
			moneyLine_name['homeMoneyLine'] = homeSpread
			moneyLine_name['awayMoneyLine'] = awaySpread
			moneyLine1.append(moneyLine_name)
		for total_Point in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[4]/div[2]/div/div[@class="jspPane"]/table//tr'):
			totalPoint_name = {}
			totalPoint_name = OrderedDict([('date', []), ('Time', []), ('underTotalPoint', []), ('overTotalPoint', [])])
			Time_Table = total_Point.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = total_Point.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = total_Point.find_element_by_xpath('./td[3]').get_attribute('textContent')
			totalPoint_name['date'] = date
			totalPoint_name['Time'] = Time
			totalPoint_name['underTotalPoint'] = homeSpread
			totalPoint_name['overTotalPoint'] = awaySpread
			totalPoint1.append(totalPoint_name)
		
		self.driver.get(response.url)
		self.driver.find_element_by_xpath('//div[@class="event-grid event-category"][2]/div[2]/div/div/div/div/div/div/div/div[1]/div[' + i + ']/div[1]').click()
		time.sleep(4)
		self.driver.current_window_handle
		for spreads in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[2]/div[2]/div/div[@class="jspPane"]/table//tr'):
			spreads_name = {}
			spreads_name = OrderedDict([('date', []), ('Time', []), ('homeSpread', []), ('awaySpread', [])])
			Time_Table = spreads.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = spreads.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = spreads.find_element_by_xpath('./td[3]').get_attribute('textContent')
			spreads_name['date'] = date
			spreads_name['Time'] = Time
			spreads_name['homeSpread'] = homeSpread
			spreads_name['awaySpread'] = awaySpread
			spread2.append(spreads_name)
		for money_Line in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[3]/div[2]/div/div[@class="jspPane"]/table//tr'):
			moneyLine_name = {}
			moneyLine_name = OrderedDict([('date', []), ('Time', []), ('homeMoneyLine', []), ('awayMoneyLine', [])])
			Time_Table = money_Line.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = money_Line.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = money_Line.find_element_by_xpath('./td[3]').get_attribute('textContent')
			moneyLine_name['date'] = date
			moneyLine_name['Time'] = Time
			moneyLine_name['homeMoneyLine'] = homeSpread
			moneyLine_name['awayMoneyLine'] = awaySpread
			moneyLine2.append(moneyLine_name)
		for total_Point in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[4]/div[2]/div/div[@class="jspPane"]/table//tr'):
			totalPoint_name = {}
			totalPoint_name = OrderedDict([('date', []), ('Time', []), ('underTotalPoint', []), ('overTotalPoint', [])])
			Time_Table = total_Point.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = total_Point.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = total_Point.find_element_by_xpath('./td[3]').get_attribute('textContent')
			totalPoint_name['date'] = date
			totalPoint_name['Time'] = Time
			totalPoint_name['underTotalPoint'] = homeSpread
			totalPoint_name['overTotalPoint'] = awaySpread
			totalPoint2.append(totalPoint_name)
			
		self.driver.get(response.url)
		self.driver.find_element_by_xpath('//div[@class="event-grid event-category"][3]/div[2]/div/div/div/div/div/div/div/div[1]/div[' + i + ']/div[1]').click()
		time.sleep(4)
		self.driver.current_window_handle
		for spreads in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[2]/div[2]/div/div[@class="jspPane"]/table//tr'):
			spreads_name = {}
			spreads_name = OrderedDict([('date', []), ('Time', []), ('homeSpread', []), ('awaySpread', [])])
			Time_Table = spreads.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = spreads.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = spreads.find_element_by_xpath('./td[3]').get_attribute('textContent')
			spreads_name['date'] = date
			spreads_name['Time'] = Time
			spreads_name['homeSpread'] = homeSpread
			spreads_name['awaySpread'] = awaySpread
			spread3.append(spreads_name)
		for money_Line in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[3]/div[2]/div/div[@class="jspPane"]/table//tr'):
			moneyLine_name = {}
			moneyLine_name = OrderedDict([('date', []), ('Time', []), ('homeMoneyLine', []), ('awayMoneyLine', [])])
			Time_Table = money_Line.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = money_Line.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = money_Line.find_element_by_xpath('./td[3]').get_attribute('textContent')
			moneyLine_name['date'] = date
			moneyLine_name['Time'] = Time
			moneyLine_name['homeMoneyLine'] = homeSpread
			moneyLine_name['awayMoneyLine'] = awaySpread
			moneyLine3.append(moneyLine_name)
		for total_Point in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[4]/div[2]/div/div[@class="jspPane"]/table//tr'):
			totalPoint_name = {}
			totalPoint_name = OrderedDict([('date', []), ('Time', []), ('underTotalPoint', []), ('overTotalPoint', [])])
			Time_Table = total_Point.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = total_Point.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = total_Point.find_element_by_xpath('./td[3]').get_attribute('textContent')
			totalPoint_name['date'] = date
			totalPoint_name['Time'] = Time
			totalPoint_name['underTotalPoint'] = homeSpread
			totalPoint_name['overTotalPoint'] = awaySpread
			totalPoint3.append(totalPoint_name)
			
		self.driver.get(response.url)
		self.driver.find_element_by_xpath('//div[@class="event-grid event-category"][4]/div[2]/div/div/div/div/div/div/div/div[1]/div[' + i + ']/div[1]').click()
		time.sleep(4)
		self.driver.current_window_handle
		for spreads in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[2]/div[2]/div/div[@class="jspPane"]/table//tr'):
			spreads_name = {}
			spreads_name = OrderedDict([('date', []), ('Time', []), ('homeSpread', []), ('awaySpread', [])])
			Time_Table = spreads.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = spreads.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = spreads.find_element_by_xpath('./td[3]').get_attribute('textContent')
			spreads_name['date'] = date
			spreads_name['Time'] = Time
			spreads_name['homeSpread'] = homeSpread
			spreads_name['awaySpread'] = awaySpread
			spread4.append(spreads_name)
		for money_Line in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[3]/div[2]/div/div[@class="jspPane"]/table//tr'):
			moneyLine_name = {}
			moneyLine_name = OrderedDict([('date', []), ('Time', []), ('homeMoneyLine', []), ('awayMoneyLine', [])])
			Time_Table = money_Line.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = money_Line.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = money_Line.find_element_by_xpath('./td[3]').get_attribute('textContent')
			moneyLine_name['date'] = date
			moneyLine_name['Time'] = Time
			moneyLine_name['homeMoneyLine'] = homeSpread
			moneyLine_name['awayMoneyLine'] = awaySpread
			moneyLine4.append(moneyLine_name)
		for total_Point in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[4]/div[2]/div/div[@class="jspPane"]/table//tr'):
			totalPoint_name = {}
			totalPoint_name = OrderedDict([('date', []), ('Time', []), ('underTotalPoint', []), ('overTotalPoint', [])])
			Time_Table = total_Point.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = total_Point.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = total_Point.find_element_by_xpath('./td[3]').get_attribute('textContent')
			totalPoint_name['date'] = date
			totalPoint_name['Time'] = Time
			totalPoint_name['underTotalPoint'] = homeSpread
			totalPoint_name['overTotalPoint'] = awaySpread
			totalPoint4.append(totalPoint_name)
			
		self.driver.get(response.url)
		self.driver.find_element_by_xpath('//div[@class="event-grid event-category"][5]/div[2]/div/div/div/div/div/div/div/div[1]/div[' + i + ']/div[1]').click()
		time.sleep(4)
		self.driver.current_window_handle
		for spreads in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[2]/div[2]/div/div[@class="jspPane"]/table//tr'):
			spreads_name = {}
			spreads_name = OrderedDict([('date', []), ('Time', []), ('homeSpread', []), ('awaySpread', [])])
			Time_Table = spreads.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = spreads.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = spreads.find_element_by_xpath('./td[3]').get_attribute('textContent')
			spreads_name['date'] = date
			spreads_name['Time'] = Time
			spreads_name['homeSpread'] = homeSpread
			spreads_name['awaySpread'] = awaySpread
			spread5.append(spreads_name)
		for money_Line in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[3]/div[2]/div/div[@class="jspPane"]/table//tr'):
			moneyLine_name = {}
			moneyLine_name = OrderedDict([('date', []), ('Time', []), ('homeMoneyLine', []), ('awayMoneyLine', [])])
			Time_Table = money_Line.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = money_Line.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = money_Line.find_element_by_xpath('./td[3]').get_attribute('textContent')
			moneyLine_name['date'] = date
			moneyLine_name['Time'] = Time
			moneyLine_name['homeMoneyLine'] = homeSpread
			moneyLine_name['awayMoneyLine'] = awaySpread
			moneyLine5.append(moneyLine_name)
		for total_Point in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[4]/div[2]/div/div[@class="jspPane"]/table//tr'):
			totalPoint_name = {}
			totalPoint_name = OrderedDict([('date', []), ('Time', []), ('underTotalPoint', []), ('overTotalPoint', [])])
			Time_Table = total_Point.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = total_Point.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = total_Point.find_element_by_xpath('./td[3]').get_attribute('textContent')
			totalPoint_name['date'] = date
			totalPoint_name['Time'] = Time
			totalPoint_name['underTotalPoint'] = homeSpread
			totalPoint_name['overTotalPoint'] = awaySpread
			totalPoint5.append(totalPoint_name)
			
		self.driver.get(response.url)
		self.driver.find_element_by_xpath('//div[@class="event-grid event-category"][6]/div[2]/div/div/div/div/div/div/div/div[1]/div[' + i + ']/div[1]').click()
		time.sleep(4)
		self.driver.current_window_handle
		for spreads in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[2]/div[2]/div/div[@class="jspPane"]/table//tr'):
			spreads_name = {}
			spreads_name = OrderedDict([('date', []), ('Time', []), ('homeSpread', []), ('awaySpread', [])])
			Time_Table = spreads.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = spreads.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = spreads.find_element_by_xpath('./td[3]').get_attribute('textContent')
			spreads_name['date'] = date
			spreads_name['Time'] = Time
			spreads_name['homeSpread'] = homeSpread
			spreads_name['awaySpread'] = awaySpread
			spread6.append(spreads_name)
		for money_Line in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[3]/div[2]/div/div[@class="jspPane"]/table//tr'):
			moneyLine_name = {}
			moneyLine_name = OrderedDict([('date', []), ('Time', []), ('homeMoneyLine', []), ('awayMoneyLine', [])])
			Time_Table = money_Line.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = money_Line.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = money_Line.find_element_by_xpath('./td[3]').get_attribute('textContent')
			moneyLine_name['date'] = date
			moneyLine_name['Time'] = Time
			moneyLine_name['homeMoneyLine'] = homeSpread
			moneyLine_name['awayMoneyLine'] = awaySpread
			moneyLine6.append(moneyLine_name)
		for total_Point in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[4]/div[2]/div/div[@class="jspPane"]/table//tr'):
			totalPoint_name = {}
			totalPoint_name = OrderedDict([('date', []), ('Time', []), ('underTotalPoint', []), ('overTotalPoint', [])])
			Time_Table = total_Point.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = total_Point.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = total_Point.find_element_by_xpath('./td[3]').get_attribute('textContent')
			totalPoint_name['date'] = date
			totalPoint_name['Time'] = Time
			totalPoint_name['underTotalPoint'] = homeSpread
			totalPoint_name['overTotalPoint'] = awaySpread
			totalPoint6.append(totalPoint_name)
			
		self.driver.get(response.url)
		self.driver.find_element_by_xpath('//div[@class="event-grid event-category"][7]/div[2]/div/div/div/div/div/div/div/div[1]/div[' + i + ']/div[1]').click()
		time.sleep(4)
		self.driver.current_window_handle
		for spreads in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[2]/div[2]/div/div[@class="jspPane"]/table//tr'):
			spreads_name = {}
			spreads_name = OrderedDict([('date', []), ('Time', []), ('homeSpread', []), ('awaySpread', [])])
			Time_Table = spreads.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = spreads.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = spreads.find_element_by_xpath('./td[3]').get_attribute('textContent')
			spreads_name['date'] = date
			spreads_name['Time'] = Time
			spreads_name['homeSpread'] = homeSpread
			spreads_name['awaySpread'] = awaySpread
			spread7.append(spreads_name)
		for money_Line in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[3]/div[2]/div/div[@class="jspPane"]/table//tr'):
			moneyLine_name = {}
			moneyLine_name = OrderedDict([('date', []), ('Time', []), ('homeMoneyLine', []), ('awayMoneyLine', [])])
			Time_Table = money_Line.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = money_Line.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = money_Line.find_element_by_xpath('./td[3]').get_attribute('textContent')
			moneyLine_name['date'] = date
			moneyLine_name['Time'] = Time
			moneyLine_name['homeMoneyLine'] = homeSpread
			moneyLine_name['awayMoneyLine'] = awaySpread
			moneyLine7.append(moneyLine_name)
		for total_Point in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[4]/div[2]/div/div[@class="jspPane"]/table//tr'):
			totalPoint_name = {}
			totalPoint_name = OrderedDict([('date', []), ('Time', []), ('underTotalPoint', []), ('overTotalPoint', [])])
			Time_Table = total_Point.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = total_Point.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = total_Point.find_element_by_xpath('./td[3]').get_attribute('textContent')
			totalPoint_name['date'] = date
			totalPoint_name['Time'] = Time
			totalPoint_name['underTotalPoint'] = homeSpread
			totalPoint_name['overTotalPoint'] = awaySpread
			totalPoint7.append(totalPoint_name)
	
		full2.update({'SPREAD':spread1, 'MONEY LINE':moneyLine1, 'TOTAL POINT':totalPoint1})
		FirstHalf2.update({'SPREAD':spread2, 'MONEY LINE':moneyLine2, 'TOTAL POINT':totalPoint2})
		SecondHalf2.update({'SPREAD':spread3, 'MONEY LINE':moneyLine3, 'TOTAL POINT':totalPoint3})
		FirstQuarter2.update({'SPREAD':spread4, 'MONEY LINE':moneyLine4, 'TOTAL POINT':totalPoint4})
		SecondQuarter2.update({'SPREAD':spread5, 'MONEY LINE':moneyLine5, 'TOTAL POINT':totalPoint5})
		ThirdQuarter2.update({'SPREAD':spread6, 'MONEY LINE':moneyLine6, 'TOTAL POINT':totalPoint6})
		FourthQuarter2.update({'SPREAD':spread7, 'MONEY LINE':moneyLine7, 'TOTAL POINT':totalPoint7})
		pinnacle.update({'full':[full2], '1stHalf':[FirstHalf2], '2ndHalf':[SecondHalf2], '1stQuarter':[FirstQuarter2],'2ndQuarter':[SecondQuarter2],'3rdQuarter':[ThirdQuarter2], '4thQuarter':[FourthQuarter2]})
		##########################################################################
		
		
		
		i = "4"
		i = str(i)
		
		full3 = []
		full3 = OrderedDict([('SPREAD', []), ('MONEY LINE', []), ('TOTAL POINT', [])])
		FirstHalf3 = []
		FirstHalf3 = OrderedDict([('SPREAD', []), ('MONEY LINE', []), ('TOTAL POINT', [])])
		SecondHalf3 = []
		SecondHalf3 = OrderedDict([('SPREAD', []), ('MONEY LINE', []), ('TOTAL POINT', [])])
		FirstQuarter3 = []
		FirstQuarter3 = OrderedDict([('SPREAD', []), ('MONEY LINE', []), ('TOTAL POINT', [])])
		SecondQuarter3 = []
		SecondQuarter3 = OrderedDict([('SPREAD', []), ('MONEY LINE', []), ('TOTAL POINT', [])])
		ThirdQuarter3 = []
		ThirdQuarter3 = OrderedDict([('SPREAD', []), ('MONEY LINE', []), ('TOTAL POINT', [])])
		FourthQuarter3 = []
		FourthQuarter3 = OrderedDict([('SPREAD', []), ('MONEY LINE', []), ('TOTAL POINT', [])])
		self.driver.get(response.url)
		self.driver.find_element_by_xpath('//div[@class="event-grid event-category"][1]/div[2]/div/div/div/div/div/div/div/div[1]/div[' + i + ']/div[1]').click()
		time.sleep(4)
		self.driver.current_window_handle
		for spreads in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[2]/div[2]/div/div[@class="jspPane"]/table//tr'):
			spreads_name = {}
			spreads_name = OrderedDict([('date', []), ('Time', []), ('homeSpread', []), ('awaySpread', [])])
			Time_Table = spreads.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = spreads.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = spreads.find_element_by_xpath('./td[3]').get_attribute('textContent')
			spreads_name['date'] = date
			spreads_name['Time'] = Time
			spreads_name['homeSpread'] = homeSpread
			spreads_name['awaySpread'] = awaySpread
			Sec_spread1.append(spreads_name)
		for money_Line in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[3]/div[2]/div/div[@class="jspPane"]/table//tr'):
			moneyLine_name = {}
			moneyLine_name = OrderedDict([('date', []), ('Time', []), ('homeMoneyLine', []), ('awayMoneyLine', [])])
			Time_Table = money_Line.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = money_Line.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = money_Line.find_element_by_xpath('./td[3]').get_attribute('textContent')
			moneyLine_name['date'] = date
			moneyLine_name['Time'] = Time
			moneyLine_name['homeMoneyLine'] = homeSpread
			moneyLine_name['awayMoneyLine'] = awaySpread
			Sec_moneyLine1.append(moneyLine_name)
		for total_Point in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[4]/div[2]/div/div[@class="jspPane"]/table//tr'):
			totalPoint_name = {}
			totalPoint_name = OrderedDict([('date', []), ('Time', []), ('underTotalPoint', []), ('overTotalPoint', [])])
			Time_Table = total_Point.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = total_Point.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = total_Point.find_element_by_xpath('./td[3]').get_attribute('textContent')
			totalPoint_name['date'] = date
			totalPoint_name['Time'] = Time
			totalPoint_name['underTotalPoint'] = homeSpread
			totalPoint_name['overTotalPoint'] = awaySpread
			Sec_totalPoint1.append(totalPoint_name)
		
		self.driver.get(response.url)
		self.driver.find_element_by_xpath('//div[@class="event-grid event-category"][2]/div[2]/div/div/div/div/div/div/div/div[1]/div[' + i + ']/div[1]').click()
		time.sleep(4)
		self.driver.current_window_handle
		for spreads in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[2]/div[2]/div/div[@class="jspPane"]/table//tr'):
			spreads_name = {}
			spreads_name = OrderedDict([('date', []), ('Time', []), ('homeSpread', []), ('awaySpread', [])])
			Time_Table = spreads.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = spreads.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = spreads.find_element_by_xpath('./td[3]').get_attribute('textContent')
			spreads_name['date'] = date
			spreads_name['Time'] = Time
			spreads_name['homeSpread'] = homeSpread
			spreads_name['awaySpread'] = awaySpread
			Sec_spread2.append(spreads_name)
		for money_Line in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[3]/div[2]/div/div[@class="jspPane"]/table//tr'):
			moneyLine_name = {}
			moneyLine_name = OrderedDict([('date', []), ('Time', []), ('homeMoneyLine', []), ('awayMoneyLine', [])])
			Time_Table = money_Line.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = money_Line.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = money_Line.find_element_by_xpath('./td[3]').get_attribute('textContent')
			moneyLine_name['date'] = date
			moneyLine_name['Time'] = Time
			moneyLine_name['homeMoneyLine'] = homeSpread
			moneyLine_name['awayMoneyLine'] = awaySpread
			Sec_moneyLine2.append(moneyLine_name)
		for total_Point in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[4]/div[2]/div/div[@class="jspPane"]/table//tr'):
			totalPoint_name = {}
			totalPoint_name = OrderedDict([('date', []), ('Time', []), ('underTotalPoint', []), ('overTotalPoint', [])])
			Time_Table = total_Point.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = total_Point.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = total_Point.find_element_by_xpath('./td[3]').get_attribute('textContent')
			totalPoint_name['date'] = date
			totalPoint_name['Time'] = Time
			totalPoint_name['underTotalPoint'] = homeSpread
			totalPoint_name['overTotalPoint'] = awaySpread
			Sec_totalPoint2.append(totalPoint_name)
			
		self.driver.get(response.url)
		self.driver.find_element_by_xpath('//div[@class="event-grid event-category"][3]/div[2]/div/div/div/div/div/div/div/div[1]/div[' + i + ']/div[1]').click()
		time.sleep(4)
		self.driver.current_window_handle
		for spreads in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[2]/div[2]/div/div[@class="jspPane"]/table//tr'):
			spreads_name = {}
			spreads_name = OrderedDict([('date', []), ('Time', []), ('homeSpread', []), ('awaySpread', [])])
			Time_Table = spreads.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = spreads.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = spreads.find_element_by_xpath('./td[3]').get_attribute('textContent')
			spreads_name['date'] = date
			spreads_name['Time'] = Time
			spreads_name['homeSpread'] = homeSpread
			spreads_name['awaySpread'] = awaySpread
			Sec_spread3.append(spreads_name)
		for money_Line in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[3]/div[2]/div/div[@class="jspPane"]/table//tr'):
			moneyLine_name = {}
			moneyLine_name = OrderedDict([('date', []), ('Time', []), ('homeMoneyLine', []), ('awayMoneyLine', [])])
			Time_Table = money_Line.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = money_Line.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = money_Line.find_element_by_xpath('./td[3]').get_attribute('textContent')
			moneyLine_name['date'] = date
			moneyLine_name['Time'] = Time
			moneyLine_name['homeMoneyLine'] = homeSpread
			moneyLine_name['awayMoneyLine'] = awaySpread
			Sec_moneyLine3.append(moneyLine_name)
		for total_Point in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[4]/div[2]/div/div[@class="jspPane"]/table//tr'):
			totalPoint_name = {}
			totalPoint_name = OrderedDict([('date', []), ('Time', []), ('underTotalPoint', []), ('overTotalPoint', [])])
			Time_Table = total_Point.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = total_Point.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = total_Point.find_element_by_xpath('./td[3]').get_attribute('textContent')
			totalPoint_name['date'] = date
			totalPoint_name['Time'] = Time
			totalPoint_name['underTotalPoint'] = homeSpread
			totalPoint_name['overTotalPoint'] = awaySpread
			Sec_totalPoint3.append(totalPoint_name)
			
		self.driver.get(response.url)
		self.driver.find_element_by_xpath('//div[@class="event-grid event-category"][4]/div[2]/div/div/div/div/div/div/div/div[1]/div[' + i + ']/div[1]').click()
		time.sleep(4)
		self.driver.current_window_handle
		for spreads in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[2]/div[2]/div/div[@class="jspPane"]/table//tr'):
			spreads_name = {}
			spreads_name = OrderedDict([('date', []), ('Time', []), ('homeSpread', []), ('awaySpread', [])])
			Time_Table = spreads.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = spreads.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = spreads.find_element_by_xpath('./td[3]').get_attribute('textContent')
			spreads_name['date'] = date
			spreads_name['Time'] = Time
			spreads_name['homeSpread'] = homeSpread
			spreads_name['awaySpread'] = awaySpread
			Sec_spread4.append(spreads_name)
		for money_Line in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[3]/div[2]/div/div[@class="jspPane"]/table//tr'):
			moneyLine_name = {}
			moneyLine_name = OrderedDict([('date', []), ('Time', []), ('homeMoneyLine', []), ('awayMoneyLine', [])])
			Time_Table = money_Line.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = money_Line.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = money_Line.find_element_by_xpath('./td[3]').get_attribute('textContent')
			moneyLine_name['date'] = date
			moneyLine_name['Time'] = Time
			moneyLine_name['homeMoneyLine'] = homeSpread
			moneyLine_name['awayMoneyLine'] = awaySpread
			Sec_moneyLine4.append(moneyLine_name)
		for total_Point in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[4]/div[2]/div/div[@class="jspPane"]/table//tr'):
			totalPoint_name = {}
			totalPoint_name = OrderedDict([('date', []), ('Time', []), ('underTotalPoint', []), ('overTotalPoint', [])])
			Time_Table = total_Point.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = total_Point.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = total_Point.find_element_by_xpath('./td[3]').get_attribute('textContent')
			totalPoint_name['date'] = date
			totalPoint_name['Time'] = Time
			totalPoint_name['underTotalPoint'] = homeSpread
			totalPoint_name['overTotalPoint'] = awaySpread
			Sec_totalPoint4.append(totalPoint_name)
			
		self.driver.get(response.url)
		self.driver.find_element_by_xpath('//div[@class="event-grid event-category"][5]/div[2]/div/div/div/div/div/div/div/div[1]/div[' + i + ']/div[1]').click()
		time.sleep(4)
		self.driver.current_window_handle
		for spreads in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[2]/div[2]/div/div[@class="jspPane"]/table//tr'):
			spreads_name = {}
			spreads_name = OrderedDict([('date', []), ('Time', []), ('homeSpread', []), ('awaySpread', [])])
			Time_Table = spreads.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = spreads.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = spreads.find_element_by_xpath('./td[3]').get_attribute('textContent')
			spreads_name['date'] = date
			spreads_name['Time'] = Time
			spreads_name['homeSpread'] = homeSpread
			spreads_name['awaySpread'] = awaySpread
			Sec_spread5.append(spreads_name)
		for money_Line in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[3]/div[2]/div/div[@class="jspPane"]/table//tr'):
			moneyLine_name = {}
			moneyLine_name = OrderedDict([('date', []), ('Time', []), ('homeMoneyLine', []), ('awayMoneyLine', [])])
			Time_Table = money_Line.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = money_Line.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = money_Line.find_element_by_xpath('./td[3]').get_attribute('textContent')
			moneyLine_name['date'] = date
			moneyLine_name['Time'] = Time
			moneyLine_name['homeMoneyLine'] = homeSpread
			moneyLine_name['awayMoneyLine'] = awaySpread
			First_moneyLine5.append(moneyLine_name)
		for total_Point in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[4]/div[2]/div/div[@class="jspPane"]/table//tr'):
			totalPoint_name = {}
			totalPoint_name = OrderedDict([('date', []), ('Time', []), ('underTotalPoint', []), ('overTotalPoint', [])])
			Time_Table = total_Point.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = total_Point.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = total_Point.find_element_by_xpath('./td[3]').get_attribute('textContent')
			totalPoint_name['date'] = date
			totalPoint_name['Time'] = Time
			totalPoint_name['underTotalPoint'] = homeSpread
			totalPoint_name['overTotalPoint'] = awaySpread
			Sec_totalPoint5.append(totalPoint_name)
			
		self.driver.get(response.url)
		self.driver.find_element_by_xpath('//div[@class="event-grid event-category"][6]/div[2]/div/div/div/div/div/div/div/div[1]/div[' + i + ']/div[1]').click()
		time.sleep(4)
		self.driver.current_window_handle
		for spreads in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[2]/div[2]/div/div[@class="jspPane"]/table//tr'):
			spreads_name = {}
			spreads_name = OrderedDict([('date', []), ('Time', []), ('homeSpread', []), ('awaySpread', [])])
			Time_Table = spreads.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = spreads.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = spreads.find_element_by_xpath('./td[3]').get_attribute('textContent')
			spreads_name['date'] = date
			spreads_name['Time'] = Time
			spreads_name['homeSpread'] = homeSpread
			spreads_name['awaySpread'] = awaySpread
			Sec_spread6.append(spreads_name)
		for money_Line in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[3]/div[2]/div/div[@class="jspPane"]/table//tr'):
			moneyLine_name = {}
			moneyLine_name = OrderedDict([('date', []), ('Time', []), ('homeMoneyLine', []), ('awayMoneyLine', [])])
			Time_Table = money_Line.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = money_Line.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = money_Line.find_element_by_xpath('./td[3]').get_attribute('textContent')
			moneyLine_name['date'] = date
			moneyLine_name['Time'] = Time
			moneyLine_name['homeMoneyLine'] = homeSpread
			moneyLine_name['awayMoneyLine'] = awaySpread
			Sec_moneyLine6.append(moneyLine_name)
		for total_Point in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[4]/div[2]/div/div[@class="jspPane"]/table//tr'):
			totalPoint_name = {}
			totalPoint_name = OrderedDict([('date', []), ('Time', []), ('underTotalPoint', []), ('overTotalPoint', [])])
			Time_Table = total_Point.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = total_Point.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = total_Point.find_element_by_xpath('./td[3]').get_attribute('textContent')
			totalPoint_name['date'] = date
			totalPoint_name['Time'] = Time
			totalPoint_name['underTotalPoint'] = homeSpread
			totalPoint_name['overTotalPoint'] = awaySpread
			Sec_totalPoint6.append(totalPoint_name)
			
		self.driver.get(response.url)
		self.driver.find_element_by_xpath('//div[@class="event-grid event-category"][7]/div[2]/div/div/div/div/div/div/div/div[1]/div[' + i + ']/div[1]').click()
		time.sleep(4)
		self.driver.current_window_handle
		for spreads in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[2]/div[2]/div/div[@class="jspPane"]/table//tr'):
			spreads_name = {}
			spreads_name = OrderedDict([('date', []), ('Time', []), ('homeSpread', []), ('awaySpread', [])])
			Time_Table = spreads.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = spreads.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = spreads.find_element_by_xpath('./td[3]').get_attribute('textContent')
			spreads_name['date'] = date
			spreads_name['Time'] = Time
			spreads_name['homeSpread'] = homeSpread
			spreads_name['awaySpread'] = awaySpread
			Sec_spread7.append(spreads_name)
		for money_Line in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[3]/div[2]/div/div[@class="jspPane"]/table//tr'):
			moneyLine_name = {}
			moneyLine_name = OrderedDict([('date', []), ('Time', []), ('homeMoneyLine', []), ('awayMoneyLine', [])])
			Time_Table = money_Line.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = money_Line.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = money_Line.find_element_by_xpath('./td[3]').get_attribute('textContent')
			moneyLine_name['date'] = date
			moneyLine_name['Time'] = Time
			moneyLine_name['homeMoneyLine'] = homeSpread
			moneyLine_name['awayMoneyLine'] = awaySpread
			Sec_moneyLine7.append(moneyLine_name)
		for total_Point in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[4]/div[2]/div/div[@class="jspPane"]/table//tr'):
			totalPoint_name = {}
			totalPoint_name = OrderedDict([('date', []), ('Time', []), ('underTotalPoint', []), ('overTotalPoint', [])])
			Time_Table = total_Point.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = total_Point.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = total_Point.find_element_by_xpath('./td[3]').get_attribute('textContent')
			totalPoint_name['date'] = date
			totalPoint_name['Time'] = Time
			totalPoint_name['underTotalPoint'] = homeSpread
			totalPoint_name['overTotalPoint'] = awaySpread
			Sec_totalPoint7.append(totalPoint_name)
	
		full3.update({'SPREAD':Sec_spread1, 'MONEY LINE':Sec_moneyLine1, 'TOTAL POINT':Sec_totalPoint1})
		FirstHalf3.update({'SPREAD':Sec_spread2, 'MONEY LINE':Sec_moneyLine2, 'TOTAL POINT':Sec_totalPoint2})
		SecondHalf3.update({'SPREAD':Sec_spread3, 'MONEY LINE':Sec_moneyLine3, 'TOTAL POINT':Sec_totalPoint3})
		FirstQuarter3.update({'SPREAD':Sec_spread4, 'MONEY LINE':Sec_moneyLine4, 'TOTAL POINT':Sec_totalPoint4})
		SecondQuarter3.update({'SPREAD':Sec_spread5, 'MONEY LINE':Sec_moneyLine5, 'TOTAL POINT':Sec_totalPoint5})
		ThirdQuarter3.update({'SPREAD':Sec_spread6, 'MONEY LINE':Sec_moneyLine6, 'TOTAL POINT':Sec_totalPoint6})
		FourthQuarter3.update({'SPREAD':Sec_spread7, 'MONEY LINE':Sec_moneyLine7, 'TOTAL POINT':Sec_totalPoint7})
		FiveDimes.update({'full':[full3], '1stHalf':[FirstHalf3], '2ndHalf':[SecondHalf3], '1stQuarter':[FirstQuarter3],'2ndQuarter':[SecondQuarter3],'3rdQuarter':[ThirdQuarter3], '4thQuarter':[FourthQuarter3]})
		################################################
		
		
		
		i = "6"
		i = str(i)
		
		full4 = []
		full4 = OrderedDict([('SPREAD', []), ('MONEY LINE', []), ('TOTAL POINT', [])])
		FirstHalf4 = []
		FirstHalf4 = OrderedDict([('SPREAD', []), ('MONEY LINE', []), ('TOTAL POINT', [])])
		SecondHalf4 = []
		SecondHalf4 = OrderedDict([('SPREAD', []), ('MONEY LINE', []), ('TOTAL POINT', [])])
		FirstQuarter4 = []
		FirstQuarter4 = OrderedDict([('SPREAD', []), ('MONEY LINE', []), ('TOTAL POINT', [])])
		SecondQuarter4 = []
		SecondQuarter4 = OrderedDict([('SPREAD', []), ('MONEY LINE', []), ('TOTAL POINT', [])])
		ThirdQuarter4 = []
		ThirdQuarter4 = OrderedDict([('SPREAD', []), ('MONEY LINE', []), ('TOTAL POINT', [])])
		FourthQuarter4 = []
		FourthQuarter4 = OrderedDict([('SPREAD', []), ('MONEY LINE', []), ('TOTAL POINT', [])])
		self.driver.get(response.url)
		self.driver.find_element_by_xpath('//div[@class="event-grid event-category"][1]/div[2]/div/div/div/div/div/div/div/div[1]/div[' + i + ']/div[1]').click()
		time.sleep(4)
		self.driver.current_window_handle
		for spreads in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[2]/div[2]/div/div[@class="jspPane"]/table//tr'):
			spreads_name = {}
			spreads_name = OrderedDict([('date', []), ('Time', []), ('homeSpread', []), ('awaySpread', [])])
			Time_Table = spreads.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = spreads.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = spreads.find_element_by_xpath('./td[3]').get_attribute('textContent')
			spreads_name['date'] = date
			spreads_name['Time'] = Time
			spreads_name['homeSpread'] = homeSpread
			spreads_name['awaySpread'] = awaySpread
			Third_spread1.append(spreads_name)
		for money_Line in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[3]/div[2]/div/div[@class="jspPane"]/table//tr'):
			moneyLine_name = {}
			moneyLine_name = OrderedDict([('date', []), ('Time', []), ('homeMoneyLine', []), ('awayMoneyLine', [])])
			Time_Table = money_Line.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = money_Line.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = money_Line.find_element_by_xpath('./td[3]').get_attribute('textContent')
			moneyLine_name['date'] = date
			moneyLine_name['Time'] = Time
			moneyLine_name['homeMoneyLine'] = homeSpread
			moneyLine_name['awayMoneyLine'] = awaySpread
			Third_moneyLine1.append(moneyLine_name)
		for total_Point in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[4]/div[2]/div/div[@class="jspPane"]/table//tr'):
			totalPoint_name = {}
			totalPoint_name = OrderedDict([('date', []), ('Time', []), ('underTotalPoint', []), ('overTotalPoint', [])])
			Time_Table = total_Point.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = total_Point.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = total_Point.find_element_by_xpath('./td[3]').get_attribute('textContent')
			totalPoint_name['date'] = date
			totalPoint_name['Time'] = Time
			totalPoint_name['underTotalPoint'] = homeSpread
			totalPoint_name['overTotalPoint'] = awaySpread
			Third_totalPoint1.append(totalPoint_name)
		
		self.driver.get(response.url)
		self.driver.find_element_by_xpath('//div[@class="event-grid event-category"][2]/div[2]/div/div/div/div/div/div/div/div[1]/div[' + i + ']/div[1]').click()
		time.sleep(4)
		self.driver.current_window_handle
		for spreads in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[2]/div[2]/div/div[@class="jspPane"]/table//tr'):
			spreads_name = {}
			spreads_name = OrderedDict([('date', []), ('Time', []), ('homeSpread', []), ('awaySpread', [])])
			Time_Table = spreads.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = spreads.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = spreads.find_element_by_xpath('./td[3]').get_attribute('textContent')
			spreads_name['date'] = date
			spreads_name['Time'] = Time
			spreads_name['homeSpread'] = homeSpread
			spreads_name['awaySpread'] = awaySpread
			Third_spread2.append(spreads_name)
		for money_Line in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[3]/div[2]/div/div[@class="jspPane"]/table//tr'):
			moneyLine_name = {}
			moneyLine_name = OrderedDict([('date', []), ('Time', []), ('homeMoneyLine', []), ('awayMoneyLine', [])])
			Time_Table = money_Line.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = money_Line.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = money_Line.find_element_by_xpath('./td[3]').get_attribute('textContent')
			moneyLine_name['date'] = date
			moneyLine_name['Time'] = Time
			moneyLine_name['homeMoneyLine'] = homeSpread
			moneyLine_name['awayMoneyLine'] = awaySpread
			Third_moneyLine2.append(moneyLine_name)
		for total_Point in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[4]/div[2]/div/div[@class="jspPane"]/table//tr'):
			totalPoint_name = {}
			totalPoint_name = OrderedDict([('date', []), ('Time', []), ('underTotalPoint', []), ('overTotalPoint', [])])
			Time_Table = total_Point.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = total_Point.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = total_Point.find_element_by_xpath('./td[3]').get_attribute('textContent')
			totalPoint_name['date'] = date
			totalPoint_name['Time'] = Time
			totalPoint_name['underTotalPoint'] = homeSpread
			totalPoint_name['overTotalPoint'] = awaySpread
			Third_totalPoint2.append(totalPoint_name)
			
		self.driver.get(response.url)
		self.driver.find_element_by_xpath('//div[@class="event-grid event-category"][3]/div[2]/div/div/div/div/div/div/div/div[1]/div[' + i + ']/div[1]').click()
		time.sleep(4)
		self.driver.current_window_handle
		for spreads in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[2]/div[2]/div/div[@class="jspPane"]/table//tr'):
			spreads_name = {}
			spreads_name = OrderedDict([('date', []), ('Time', []), ('homeSpread', []), ('awaySpread', [])])
			Time_Table = spreads.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = spreads.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = spreads.find_element_by_xpath('./td[3]').get_attribute('textContent')
			spreads_name['date'] = date
			spreads_name['Time'] = Time
			spreads_name['homeSpread'] = homeSpread
			spreads_name['awaySpread'] = awaySpread
			Third_spread3.append(spreads_name)
		for money_Line in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[3]/div[2]/div/div[@class="jspPane"]/table//tr'):
			moneyLine_name = {}
			moneyLine_name = OrderedDict([('date', []), ('Time', []), ('homeMoneyLine', []), ('awayMoneyLine', [])])
			Time_Table = money_Line.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = money_Line.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = money_Line.find_element_by_xpath('./td[3]').get_attribute('textContent')
			moneyLine_name['date'] = date
			moneyLine_name['Time'] = Time
			moneyLine_name['homeMoneyLine'] = homeSpread
			moneyLine_name['awayMoneyLine'] = awaySpread
			Third_moneyLine3.append(moneyLine_name)
		for total_Point in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[4]/div[2]/div/div[@class="jspPane"]/table//tr'):
			totalPoint_name = {}
			totalPoint_name = OrderedDict([('date', []), ('Time', []), ('underTotalPoint', []), ('overTotalPoint', [])])
			Time_Table = total_Point.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = total_Point.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = total_Point.find_element_by_xpath('./td[3]').get_attribute('textContent')
			totalPoint_name['date'] = date
			totalPoint_name['Time'] = Time
			totalPoint_name['underTotalPoint'] = homeSpread
			totalPoint_name['overTotalPoint'] = awaySpread
			Third_totalPoint3.append(totalPoint_name)
			
		self.driver.get(response.url)
		self.driver.find_element_by_xpath('//div[@class="event-grid event-category"][4]/div[2]/div/div/div/div/div/div/div/div[1]/div[' + i + ']/div[1]').click()
		time.sleep(4)
		self.driver.current_window_handle
		for spreads in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[2]/div[2]/div/div[@class="jspPane"]/table//tr'):
			spreads_name = {}
			spreads_name = OrderedDict([('date', []), ('Time', []), ('homeSpread', []), ('awaySpread', [])])
			Time_Table = spreads.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = spreads.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = spreads.find_element_by_xpath('./td[3]').get_attribute('textContent')
			spreads_name['date'] = date
			spreads_name['Time'] = Time
			spreads_name['homeSpread'] = homeSpread
			spreads_name['awaySpread'] = awaySpread
			Third_spread4.append(spreads_name)
		for money_Line in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[3]/div[2]/div/div[@class="jspPane"]/table//tr'):
			moneyLine_name = {}
			moneyLine_name = OrderedDict([('date', []), ('Time', []), ('homeMoneyLine', []), ('awayMoneyLine', [])])
			Time_Table = money_Line.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = money_Line.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = money_Line.find_element_by_xpath('./td[3]').get_attribute('textContent')
			moneyLine_name['date'] = date
			moneyLine_name['Time'] = Time
			moneyLine_name['homeMoneyLine'] = homeSpread
			moneyLine_name['awayMoneyLine'] = awaySpread
			Third_moneyLine4.append(moneyLine_name)
		for total_Point in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[4]/div[2]/div/div[@class="jspPane"]/table//tr'):
			totalPoint_name = {}
			totalPoint_name = OrderedDict([('date', []), ('Time', []), ('underTotalPoint', []), ('overTotalPoint', [])])
			Time_Table = total_Point.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = total_Point.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = total_Point.find_element_by_xpath('./td[3]').get_attribute('textContent')
			totalPoint_name['date'] = date
			totalPoint_name['Time'] = Time
			totalPoint_name['underTotalPoint'] = homeSpread
			totalPoint_name['overTotalPoint'] = awaySpread
			Third_totalPoint4.append(totalPoint_name)
			
		self.driver.get(response.url)
		self.driver.find_element_by_xpath('//div[@class="event-grid event-category"][5]/div[2]/div/div/div/div/div/div/div/div[1]/div[' + i + ']/div[1]').click()
		time.sleep(4)
		self.driver.current_window_handle
		for spreads in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[2]/div[2]/div/div[@class="jspPane"]/table//tr'):
			spreads_name = {}
			spreads_name = OrderedDict([('date', []), ('Time', []), ('homeSpread', []), ('awaySpread', [])])
			Time_Table = spreads.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = spreads.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = spreads.find_element_by_xpath('./td[3]').get_attribute('textContent')
			spreads_name['date'] = date
			spreads_name['Time'] = Time
			spreads_name['homeSpread'] = homeSpread
			spreads_name['awaySpread'] = awaySpread
			Third_spread5.append(spreads_name)
		for money_Line in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[3]/div[2]/div/div[@class="jspPane"]/table//tr'):
			moneyLine_name = {}
			moneyLine_name = OrderedDict([('date', []), ('Time', []), ('homeMoneyLine', []), ('awayMoneyLine', [])])
			Time_Table = money_Line.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = money_Line.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = money_Line.find_element_by_xpath('./td[3]').get_attribute('textContent')
			moneyLine_name['date'] = date
			moneyLine_name['Time'] = Time
			moneyLine_name['homeMoneyLine'] = homeSpread
			moneyLine_name['awayMoneyLine'] = awaySpread
			First_moneyLine5.append(moneyLine_name)
		for total_Point in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[4]/div[2]/div/div[@class="jspPane"]/table//tr'):
			totalPoint_name = {}
			totalPoint_name = OrderedDict([('date', []), ('Time', []), ('underTotalPoint', []), ('overTotalPoint', [])])
			Time_Table = total_Point.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = total_Point.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = total_Point.find_element_by_xpath('./td[3]').get_attribute('textContent')
			totalPoint_name['date'] = date
			totalPoint_name['Time'] = Time
			totalPoint_name['underTotalPoint'] = homeSpread
			totalPoint_name['overTotalPoint'] = awaySpread
			Third_totalPoint5.append(totalPoint_name)
			
		self.driver.get(response.url)
		self.driver.find_element_by_xpath('//div[@class="event-grid event-category"][6]/div[2]/div/div/div/div/div/div/div/div[1]/div[' + i + ']/div[1]').click()
		time.sleep(4)
		self.driver.current_window_handle
		for spreads in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[2]/div[2]/div/div[@class="jspPane"]/table//tr'):
			spreads_name = {}
			spreads_name = OrderedDict([('date', []), ('Time', []), ('homeSpread', []), ('awaySpread', [])])
			Time_Table = spreads.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = spreads.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = spreads.find_element_by_xpath('./td[3]').get_attribute('textContent')
			spreads_name['date'] = date
			spreads_name['Time'] = Time
			spreads_name['homeSpread'] = homeSpread
			spreads_name['awaySpread'] = awaySpread
			Third_spread6.append(spreads_name)
		for money_Line in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[3]/div[2]/div/div[@class="jspPane"]/table//tr'):
			moneyLine_name = {}
			moneyLine_name = OrderedDict([('date', []), ('Time', []), ('homeMoneyLine', []), ('awayMoneyLine', [])])
			Time_Table = money_Line.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = money_Line.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = money_Line.find_element_by_xpath('./td[3]').get_attribute('textContent')
			moneyLine_name['date'] = date
			moneyLine_name['Time'] = Time
			moneyLine_name['homeMoneyLine'] = homeSpread
			moneyLine_name['awayMoneyLine'] = awaySpread
			Third_moneyLine6.append(moneyLine_name)
		for total_Point in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[4]/div[2]/div/div[@class="jspPane"]/table//tr'):
			totalPoint_name = {}
			totalPoint_name = OrderedDict([('date', []), ('Time', []), ('underTotalPoint', []), ('overTotalPoint', [])])
			Time_Table = total_Point.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = total_Point.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = total_Point.find_element_by_xpath('./td[3]').get_attribute('textContent')
			totalPoint_name['date'] = date
			totalPoint_name['Time'] = Time
			totalPoint_name['underTotalPoint'] = homeSpread
			totalPoint_name['overTotalPoint'] = awaySpread
			Third_totalPoint6.append(totalPoint_name)
			
		self.driver.get(response.url)
		self.driver.find_element_by_xpath('//div[@class="event-grid event-category"][7]/div[2]/div/div/div/div/div/div/div/div[1]/div[' + i + ']/div[1]').click()
		time.sleep(4)
		self.driver.current_window_handle
		for spreads in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[2]/div[2]/div/div[@class="jspPane"]/table//tr'):
			spreads_name = {}
			spreads_name = OrderedDict([('date', []), ('Time', []), ('homeSpread', []), ('awaySpread', [])])
			Time_Table = spreads.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = spreads.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = spreads.find_element_by_xpath('./td[3]').get_attribute('textContent')
			spreads_name['date'] = date
			spreads_name['Time'] = Time
			spreads_name['homeSpread'] = homeSpread
			spreads_name['awaySpread'] = awaySpread
			Third_spread7.append(spreads_name)
		for money_Line in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[3]/div[2]/div/div[@class="jspPane"]/table//tr'):
			moneyLine_name = {}
			moneyLine_name = OrderedDict([('date', []), ('Time', []), ('homeMoneyLine', []), ('awayMoneyLine', [])])
			Time_Table = money_Line.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = money_Line.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = money_Line.find_element_by_xpath('./td[3]').get_attribute('textContent')
			moneyLine_name['date'] = date
			moneyLine_name['Time'] = Time
			moneyLine_name['homeMoneyLine'] = homeSpread
			moneyLine_name['awayMoneyLine'] = awaySpread
			Third_moneyLine7.append(moneyLine_name)
		for total_Point in self.driver.find_elements_by_xpath('//*[@id="dialogPop"]/div[4]/div[2]/div/div[@class="jspPane"]/table//tr'):
			totalPoint_name = {}
			totalPoint_name = OrderedDict([('date', []), ('Time', []), ('underTotalPoint', []), ('overTotalPoint', [])])
			Time_Table = total_Point.find_element_by_xpath('./td[1]').get_attribute('textContent')
			date = Time_Table[:Time_Table.find(' ')]
			Time = Time_Table[Time_Table.find(' ') + 1:]
			homeSpread = total_Point.find_element_by_xpath('./td[2]').get_attribute('textContent')
			awaySpread = total_Point.find_element_by_xpath('./td[3]').get_attribute('textContent')
			totalPoint_name['date'] = date
			totalPoint_name['Time'] = Time
			totalPoint_name['underTotalPoint'] = homeSpread
			totalPoint_name['overTotalPoint'] = awaySpread
			Third_totalPoint7.append(totalPoint_name)
	
		full4.update({'SPREAD':Third_spread1, 'MONEY LINE':Third_moneyLine1, 'TOTAL POINT':Third_totalPoint1})
		FirstHalf4.update({'SPREAD':Third_spread2, 'MONEY LINE':Third_moneyLine2, 'TOTAL POINT':Third_totalPoint2})
		SecondHalf4.update({'SPREAD':Third_spread3, 'MONEY LINE':Third_moneyLine3, 'TOTAL POINT':Third_totalPoint3})
		FirstQuarter4.update({'SPREAD':Third_spread4, 'MONEY LINE':Third_moneyLine4, 'TOTAL POINT':Third_totalPoint4})
		SecondQuarter4.update({'SPREAD':Third_spread5, 'MONEY LINE':Third_moneyLine5, 'TOTAL POINT':Third_totalPoint5})
		ThirdQuarter4.update({'SPREAD':Third_spread6, 'MONEY LINE':Third_moneyLine6, 'TOTAL POINT':Third_totalPoint6})
		FourthQuarter4.update({'SPREAD':Third_spread7, 'MONEY LINE':Third_moneyLine7, 'TOTAL POINT':Third_totalPoint7})
		BookMaker.update({'full':[full4], '1stHalf':[FirstHalf4], '2ndHalf':[SecondHalf4], '1stQuarter':[FirstQuarter4],'2ndQuarter':[SecondQuarter4],'3rdQuarter':[ThirdQuarter4], '4thQuarter':[FourthQuarter4]})
		
		oddsFlow.update({'BetOnline':[BetOnline],'pinnacle':[pinnacle],'5Dimes':[FiveDimes], 'BookMaker':[BookMaker]})
		game.update({"gameID":gameID, "oddsFlow": [oddsFlow]})
		output = json.dumps(game, indent=4, separators=(',', ': '))
		output = output.encode('utf-8').replace('\u00a0',' ').replace('\u00bd','½')
		self.json_file.write(output)