import unittest
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # 自动管理 ChromeDriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestSignup(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument('--ignore-certificate-errors')  # 跳过 SSL 验证
        options.add_argument('--allow-insecure-localhost')  # 允许不安全的本地主机
        options.add_argument('--ignore-certificate-errors-spki-list')
        options.add_argument('--allow-http-screen-capture')



        # 不使用无头模式
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def test_1_signup_with_existing_email(self):
        # 模拟随机延迟
        time.sleep(random.uniform(1, 3))  # 随机延迟 1 到 3 秒
        self.driver.get("https://www.wizmarketplace.com/signup/form")

        # 读取数据文件
        with open('tests/data/invalidDataForSignup.txt', 'r') as file:
            lines = file.readlines()

            # 假设我们只需要第一组用户名和密码
        firstName = lines[0].strip()
        lastName = lines[1].strip()
        email = lines[2].strip()
        phone = lines[3].strip()
        password = lines[4].strip()

        # 使用显式等待，直到 "SIGN UP NOW!" 元素可见
        try:

            # # # 验证firstName是否存在
            firstName_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, ":r0:"))  # 根据 ID 查找输入框
            )

            # 输入firstName
            firstName_input.send_keys(firstName)


            # # # 验证lastName是否存在
            lastName_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, ":r1:"))  # 根据 ID 查找输入框
            )

            # 输入firstName
            lastName_input.send_keys(lastName)

           

            # # # 验证输入框是否存在
            email_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, ":r2:"))  # 根据 ID 查找输入框
            )

            # 输入用户名
            email_input.send_keys(email)


           
            
            ### 修改手机的区域号
            # phoneRegion_element = WebDriverWait(self.driver, 10).until(
            #     EC.visibility_of_element_located((By.XPATH, "//span[@class='notranslate' and text()='​+65']"))
            # )
    
            # 使用 JavaScript 修改元素的内容
            # self.driver.execute_script("arguments[0].textContent = '​+86';", phoneRegion_element)

            # 添加一些额外的代码，例如验证元素内容是否已更改等
            # assert phoneRegion_element.text == "​+86", "元素内容未更改为 '+86'"

            # 使用 WebDriverWait 等待元素变得可点击
            img_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//img[@alt and contains(@class, 'jss99')]"))
            )
    
            # 点击元素
            img_element.click()

            # 使用 WebDriverWait 等待输入框元素变得可见
            input_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search by country or code']"))
            )
    
            # 断言输入框存在
            assert input_element is not None, "输入框不存在"

            # 点击输入框
            input_element.click()

            # 输入文本"86"
            input_element.send_keys("86")

            # 等待搜索结果出现
            china_element = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'China')]"))
    )

            # 选中第一个匹配的搜索结果
            china_element.click()

            # 验证手机输入框是否存在
            phone_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, ":r3:"))  # 根据 ID 查找输入框
            )
            # 输入手机号码
            phone_input.send_keys(phone)


            # # # 验证密码输入框是否存在
            password_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, ":r4:"))  # 根据 ID 查找输入框
            )

            # 输入密码
            password_input.send_keys(password)


            # 使用 WebDriverWait 等待按钮变得可点击
            signup_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign up']"))
            )
    
            # 点击按钮
            signup_button.click()

            time.sleep(3)

            # 使用 WebDriverWait 等待 "Invalid email" 文本变得可见
            invalid_email_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'An account with this email address/phone number is already registered.')]"))
            )

            existing_email_text = 'An account with this email address/phone number is already registered.'
            # 断言 "Invalid email" 文本确实存在
            assert existing_email_text in invalid_email_element.text, "页面上不存在 'An account with this email address/phone number is already registered.' 元素"

        except Exception as e:
            self.fail(f"测试失败: {e}")
    

    def test_2_signup_with_valide_email_expired_code(self):
        # 模拟随机延迟
        time.sleep(random.uniform(1, 3))  # 随机延迟 1 到 3 秒
        self.driver.get("https://www.wizmarketplace.com/signup/form")

        # 读取数据文件
        with open('tests/data/validDataExpiredCodeForSignup.txt', 'r') as file:
            lines = file.readlines()

            # 假设我们只需要第一组用户名和密码
        firstName = lines[0].strip()
        lastName = lines[1].strip()
        email = lines[2].strip()
        phone = lines[3].strip()
        password = lines[4].strip()
        expiredCode = lines[5].strip()

        # 使用显式等待，直到 "SIGN UP NOW!" 元素可见
        try:

            # # # 验证firstName是否存在
            firstName_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, ":r0:"))  # 根据 ID 查找输入框
            )

            # 输入firstName
            firstName_input.send_keys(firstName)


            # # # 验证lastName是否存在
            lastName_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, ":r1:"))  # 根据 ID 查找输入框
            )

            # 输入firstName
            lastName_input.send_keys(lastName)

           

            # # # 验证输入框是否存在
            email_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, ":r2:"))  # 根据 ID 查找输入框
            )

            # 输入用户名
            email_input.send_keys(email)


           
            
            ### 修改手机的区域号
            # phoneRegion_element = WebDriverWait(self.driver, 10).until(
            #     EC.visibility_of_element_located((By.XPATH, "//span[@class='notranslate' and text()='​+65']"))
            # )
    
            # 使用 JavaScript 修改元素的内容
            # self.driver.execute_script("arguments[0].textContent = '​+86';", phoneRegion_element)

            # 添加一些额外的代码，例如验证元素内容是否已更改等
            # assert phoneRegion_element.text == "​+86", "元素内容未更改为 '+86'"

            # 使用 WebDriverWait 等待元素变得可点击
            # img_element = WebDriverWait(self.driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, "//slan[@class, 'notranslate']"))
            # )

                        #     EC.visibility_of_element_located((By.XPATH, "//span[@class='notranslate' and text()='​+65']"))
            img_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".MuiInputAdornment-root.MuiInputAdornment-positionStart"))
            )
    
            # 点击元素
            img_element.click()

            # 使用 WebDriverWait 等待输入框元素变得可见
            input_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search by country or code']"))
            )
    
            # 断言输入框存在
            assert input_element is not None, "输入框不存在"

            # 点击输入框
            input_element.click()

            # 输入文本"86"
            input_element.send_keys("86")

            # 等待搜索结果出现
            china_element = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'China')]"))
    )

            # 选中第一个匹配的搜索结果
            china_element.click()

            # 验证手机输入框是否存在
            phone_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, ":r3:"))  # 根据 ID 查找输入框
            )
            # 输入手机号码
            phone_input.send_keys(phone)


            # # # 验证密码输入框是否存在
            password_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, ":r4:"))  # 根据 ID 查找输入框
            )

            # 输入密码
            password_input.send_keys(password)


            # 使用 WebDriverWait 等待按钮变得可点击
            signup_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign up']"))
            )
    
            # 点击按钮
            signup_button.click()

            time.sleep(3)

            # 使用 WebDriverWait 等待 "Invalid email" 文本变得可见
            # activateCode_element = WebDriverWait(self.driver, 10).until(
            #     EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Enter Activation Code')]"))
            # )

            # activateCode_text = 'Enter Activation Code'
            # # 断言 "Invalid email" 文本确实存在
            # assert activateCode_text in activateCode_element.text, "没有发送验证码"


            # 使用 WebDriverWait 等待输入框容器元素变得可见
            pincode_container = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".pincode-input-container"))
            )
    
            # 验证输入框容器存在
            assert pincode_container is not None, "输入框容器不存在"

            # 定位所有输入框
            pincode_inputs = pincode_container.find_elements(By.CSS_SELECTOR, ".pincode-input-text")
    
            # 验证存在6个输入框
            assert len(pincode_inputs) == 6, "输入框数量不是6个"

            # 向每个输入框里输入数字
            for i, input_element in enumerate(pincode_inputs):
                input_element.clear()  # 清空输入框（如果需要）
                input_element.send_keys(expiredCode[i])  # 向每个输入框发送一个数字

            # 使用 WebDriverWait 等待按钮变得可点击
            activate_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Activate']"))
            )
    
            # 点击按钮
            activate_button.click()

            time.sleep(1)

            error_tip = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "notistack-snackbar"))
            )
            assert error_tip is not None, "Error tip element does not exist"

            # 获取 error tips 元素的文本内容
            error_text = error_tip.text
            assert "Invalid verification code entered" in error_text, "Error tip does not contain the expected text"



        except Exception as e:
            self.fail(f"测试失败: {e}")



    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
