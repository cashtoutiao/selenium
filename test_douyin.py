import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestDouyin():
  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_douyin(self):
    self.driver.get("https://www.douyin.com/")
    self.driver.set_window_size(1440, 790)
    time.sleep(5)
    self.driver.find_element(By.CSS_SELECTOR, ".dy-account-close").click()
    self.driver.find_element(By.CSS_SELECTOR, ".igFQqPKs").click()
    self.driver.find_element(By.CSS_SELECTOR, ".igFQqPKs").send_keys("德云社")
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, ".igFQqPKs").send_keys(Keys.ENTER)
    time.sleep(5)
    # 获取当前浏览器所有窗口句柄
    handles = self.driver.window_handles
    # 切换最新窗口句柄
    self.driver.switch_to.window(handles[-1])
    self.vars["win1576"] = self.wait_for_window(2000)
    # 实际结果
    res = self.driver.find_element(By.CSS_SELECTOR,".Nu66P_ba")
    #获取实际结果是否是预期结果
    assert "PP大咖剧院"==res.text





