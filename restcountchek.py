from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)


driver.get("https://touchcasinop:x*oVqmY3Jb!I@touchcasino.com/en")
driver.maximize_window()
time.sleep(4)
driver.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[@class='Button__StyledButton-wbaydb-0 Button__PrimaryButtonSidebar-wbaydb-27 bfFcdk hysRUR btn btn-primary']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("andrija.mihaljevic@igamingplatform.com")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Casino1!")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@name='password_confirm']").send_keys("Casino1!")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@name='phone']").send_keys("123123123")
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='registration-form-cta']/button").click()
time.sleep(2)
countries = driver.find_elements(By.XPATH, "//select[@name='countrycode']/option")
print(countries)
restricted_countries = ["af","al","dz","as","ao","ai","ag","au","at","bs","bb","by","be","bj","bm","bt","bo","ba","bw","bv","io","bn","bg","bf","bi","kh","cv","ky","cf","td","cn","cx","cc","km","cg","cd","ck","ci","cu","cw","cz","dj","do","tl","eg","gq","er","et","fr","gf","pf","tf","ga","gh","gr","gp","gn","gw","gy","ht","hm","hk","hu","ir","iq","il","it","jm","jo","ke","ki","kp","kr","xk","kg","la","lv","lb","ls","lr","ly","lt","mo","mg","mw","ml","mq","mr","mu","yt","fm","md","mc","mn","me","mz","mm","nr","nc","ni","ne","ng","nu","nf","mk","pk","ps","pa","ph","pn","pl","pt","re","ro","ru","rw","sh","mf","pm","sn","rs","sl","sg","sk","so","ss","es","lk","sd","sr","sy","tw","tz","tg","to","tt","tn","tr","tc","ug","ua","gb","us","um","uz","vu","ve","vn","vg","vi","wf","eh","ye","zm","zw"]

for country in countries:
    print(country.get_attribute('value'))
    if country.get_attribute('value') in restricted_countries:
        print(f"FAIL / Found restricted country: {country.get_attribute('value')}")
    else:
        print("TestCase pass")

driver.close()
