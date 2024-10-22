import unittest
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument('--ignore-certificate-errors')  # 跳过 SSL 验证
        options.add_argument('--allow-insecure-localhost')  # 允许不安全的本地主机
        options.add_argument('--ignore-certificate-errors-spki-list')
        options.add_argument('--allow-http-screen-capture')
        # 不使用无头模式
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    
    def test_1_login_with_invalid_data(self):
        # 模拟随机延迟
        time.sleep(random.uniform(1, 3))  # 随机延迟 1 到 3 秒
        self.driver.get("https://www.wizmarketplace.com")

        # 读取数据文件
        with open('tests/data/invalidData.txt', 'r') as file:
            lines = file.readlines()

            # 假设我们只需要第一组用户名和密码
        email = lines[0].strip()
        password = lines[1].strip()

        try:
           
            # 使用 XPath 定位 'Do not display again'框
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Do not display again')]"))
            )
    
            # 关闭'Do not display again' 框
            button.click()

            # 进入登录界面
            self.driver.get("https://www.wizmarketplace.com/login")


            # 验证输入框是否存在
            email_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, ":r0:"))  # 根据 ID 查找输入框
            )

            # 输入用户名
            email_input.send_keys(email)


            # 验证密码输入框是否存在
            password_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, ":r1:"))  # 根据 ID 查找输入框
            )

            # 输入密码
            password_input.send_keys(password)


            # 使用 WebDriverWait 等待按钮变得可点击
            login_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Log In']"))
            )
    
            # 点击Login按钮
            login_button.click()

            time.sleep(3)

            # 使用 WebDriverWait 等待 "Invalid email" 文本变得可见
            invalid_email_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Invalid email')]"))
            )
    
            # 断言 "Invalid email" 文本确实存在
            assert "Invalid email" in invalid_email_element.text, "'Invalid email' not exist"
          
        except Exception as e:
            self.fail(f"测试失败: {e}")
    
    def test_2_login_with_valid_data(self):

        # 模拟随机延迟
        time.sleep(random.uniform(1, 3))  
        self.driver.get("https://www.wizmarketplace.com/login")

        # 读取数据文件
        with open('tests/data/validData.txt', 'r') as file:
            lines = file.readlines()

        email = lines[0].strip()
        password = lines[1].strip()

        try:
            # 验证输入框是否存在
            email_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, ":r0:"))  # 根据 ID 查找输入框
            )

            # 输入用户名
            email_input.send_keys(email)


            # 验证密码输入框是否存在
            password_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, ":r1:"))  # 根据 ID 查找输入框
            )

            # 输入密码
            password_input.send_keys(password)


            # 使用 WebDriverWait 等待按钮变得可点击
            login_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Log In']"))
            )
    
            # 点击Login按钮
            login_button.click()

            time.sleep(5)

            # 获取所有cookie
            cookies = self.driver.get_cookies()
            # print("cookies after login is:",cookies)

            # 遍历cookie列表以查找token
            token = None
            for cookie in cookies:
                if cookie['name'] == 'token':  # 假设token存储在名为'access_token'的cookie中
                    token = cookie['value']
                    print("token in cookies is:",token)
                    break

            # 打印获取到的token
            # print("Token:", token)

            # 断言登录后就会有 token
            assert token is not None, "Token is None"

            time.sleep(3)

            return token


        except Exception as e:
            self.fail(f"测试失败: {e}")

    def test_7_profile_change_password(self):
        # 模拟随机延迟
        time.sleep(random.uniform(1, 3))  

        # 进入profile修改password
        self.driver.get("https://www.wizmarketplace.com/user/my-profile")

        # 读取数据文件
        with open('tests/data/validData.txt', 'r') as file:
            lines = file.readlines()

        current_password = lines[1].strip()


        try:    

            changePassword_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//p[text()='Change password']"))
            )
            assert changePassword_link is not None, "Change password not exist"

            changePassword_link.click()


            current_password_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.NAME, "password"))
            )

            current_password_input.send_keys(current_password)

            # 使用 By.NAME 选择器来定位元素
            new_password_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.NAME, "newPassword"))
            )
        
            # 断言元素存在
            assert new_password_input is not None, "new password does not exist"

            new_password_input.send_keys("Test123456")


            confirm_password_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.NAME, "confirmPassword"))
            )

            confirm_password_input.send_keys("Test123456")

            save_changes_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='SAVE CHANGES']"))
            )
    
            # 点击按钮
            save_changes_button.click()

            time.sleep(1)

            # 修改password成功后会有tip
            success_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "notistack-snackbar"))
            )
    
            # 获取元素的文本内容
            message_text = success_message.text.strip()

            # 断言元素存在，并且文案是 "Password has been updated successfully"
            assert success_message is not None, "tips not exist"
            assert message_text == "Password has been updated successfully", "tips text wrong"
        
        
        except Exception as e:
            self.fail(f"测试失败: {e}")

    def test_8_login_with_new_password(self):

       
        time.sleep(5)     

        # Logout
        logout_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Log out')]"))
        )
    
        # 点击 "Log out" 元素
        logout_element.click()

        time.sleep(5) 

        logout_page = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'You’re now logged out')]"))  # 根据 ID 查找输入框
        )

        # 断言 logout 成功
        assert logout_page is not None, ' logout fail'

    
        
        # 模拟随机延迟
        time.sleep(random.uniform(1, 3))  # 随机延迟 1 到 3 秒

        # 再次登录，change password back
        self.driver.get("https://www.wizmarketplace.com/login")

        # 读取数据文件
        with open('tests/data/validData.txt', 'r') as file:
            lines = file.readlines()

            # 假设我们只需要第一组用户名和密码
        email = lines[0].strip()
        password = "Test123456"

        try:
            # 验证输入框是否存在
            email_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, ":r0:"))  # 根据 ID 查找输入框
            )

            # 输入用户名
            email_input.send_keys(email)


            # # # 验证密码输入框是否存在
            password_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, ":r1:"))  # 根据 ID 查找输入框
            )

            # 输入密码
            password_input.send_keys(password)


            # 使用 WebDriverWait 等待按钮变得可点击
            login_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Log In']"))
            )
    
            # 点击按钮
            login_button.click()

            time.sleep(5)

            # 获取所有cookie
            cookies = self.driver.get_cookies() 
            
            token = None
            for cookie in cookies:
                if cookie['name'] == 'token':  # 假设token存储在名为'access_token'的cookie中
                    token = cookie['value']
                    print("token in cookies is:",token)
                    break

            # 断言token不为None
            assert token is not None, "Token is None"

            return token


        except Exception as e:
            self.fail(f"测试失败: {e}")

    def test_3_filter_product_by_featured(self):
        
        # 进入产品Sale页面
        self.driver.get("https://www.wizmarketplace.com/listing")


        try:

            # 点击 Featured 筛选产品
            featured_filter_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Featured')]"))
            )

            featured_filter_button.click()

            # 有时候筛选会不生效，再次刷新页面
            self.driver.refresh()

            # 找到属于 Featured的唯一产品
            element_xpath = "//a[contains(@href, '1679756265905917953')]"

            # 滚动到页面底部，是产品可见
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            product_link = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, element_xpath))
            )

            # print("target_element is:",product_link)

            assert product_link is not None, "no featured products"
    
            # 进入产品详情页
            product_link.click()

            # 为产品选一个 color: Beige
            style_attribute = "background-color: rgb(239, 223, 202); border: 0.5px solid transparent;"
            locator = (By.XPATH, f"//div[contains(@style, '{style_attribute}')]")

            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            element.click()

            # 定位 Add to cart 元素并点击
            add_to_cart_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add to cart')]"))
            )

            assert add_to_cart_element is not None, "Add to cart button does not exist"

            add_to_cart_element.click()

            time.sleep(1)

            # 验证Add to cart 成功后会有一个tip 
            successful_tip = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "notistack-snackbar"))
            )
            assert successful_tip is not None, "add to cart fail"

            # 断言该 tip 的文本内容是'Added to cart successfully'
            successful_text = successful_tip.text
            assert "Added to cart successfully" in successful_text, "add to cart fail"


        except Exception as e:
            self.fail(f"测试失败: {e}")

    def test_4_view_cart(self):

        time.sleep(random.uniform(1, 3))  # 随机延迟 1 到 3 秒

        try:
            # 获取右上角的购物车图标
            view_cart_locator = (By.XPATH, '//*[@data-testid="ShoppingCartIcon"]')

            # 点击购物车图标，打开购物车侧边栏
            view_cart_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(view_cart_locator))
            view_cart_element.click()


            # 点击View Cart按钮
            view_cart_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'View Cart')]"))
            )

            view_cart_button.click()

            time.sleep(5)


            cart_item_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Cart Items')]")))

            assert cart_item_element is not None, "not View Cart page"


            # 增加数量
            # add_icon_locator = '//*[@data-testid="AddIcon"]'

            # 滚动到元素可见
            # self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element(By.XPATH, add_icon_locator))

            # 等待元素可见
            add_icon_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@data-testid="AddIcon"]'))
            )

            # 增加数量至 2
            add_icon_element.click()

            time.sleep(5)

            # 验证数量为2
            quantity_locator = (By.XPATH, "//p[text()='2']")
            quantity_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(quantity_locator))

            assert quantity_element is not None, 'quantity is not 2'

        except Exception as e:
            self.fail(f"测试失败: {e}")


    def test_5_checkout(self):

        time.sleep(random.uniform(1, 3))  # 随机延迟 1 到 3 秒

        # 还是在购物车页面
        # self.driver.get("https://www.wizmarketplace.com/cart")
        
        try:

            # 点击Checkout按钮
            checkout_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//button[@type="button"]'))
            )

            checkout_button.click()

           
            # 断言Order页面存在 Customer Information字段
            customer_information_text = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Customer Information')]"))
            )

            assert customer_information_text is not None, 'Not order page'

            # change delivery address
            change_delivery_address_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//button[contains(@type, 'primary') and contains(text(), 'Change')]"))
            )

            change_delivery_address_button.click()

            time.sleep(3)

           

            # Add a New Address
            element_xpath = "//p[contains(text(), 'Add New Address')]"

            # 滚动到元素可见
            self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element(By.XPATH, element_xpath))

            # 等待元素可见
            add_new_address_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, element_xpath))
            )

            add_new_address_element.click()

            # 验证firstName是否存在
            Name_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, ":ro:"))  # 根据 ID 查找输入框
            )

            # 输入firstName
            Name_input.send_keys("Aroma1")


            # 验证 phone是否存在
            phone_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, ":rp:"))  # 根据 ID 查找输入框
            )

            # 输入phone
            phone_input.send_keys("00000000000")


            # 验证streete是否存在
            street_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, ":rq:"))  # 根据 ID 查找输入框
            )

            # 输入 street
            street_input.send_keys("my address")


            # 验证code是否存在
            code_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, ":rr:"))  # 根据 ID 查找输入框
            )

            # 输入code
            code_input.send_keys("100087")


            # default_checkbox = WebDriverWait(self.driver, 10).until(
            #     EC.visibility_of_element_located((By.XPATH, '//input[@ype="checkbox")]'))
            # )

            # 使用XPath定位类型为checkbox的<input>元素
            # default_checkbox_locator = (By.XPATH, "//input[@type='checkbox']")

            # 使用WebDriverWait等待元素可见
            # default_checkbox = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@type='checkbox']")))

            # default_checkbox = (By.XPATH, '//*[@data-testid="CheckBoxOutlineBlankIcon"]')


            # default_checkbox.click()

            # default_checkbox.click()

            # 保存新建的address
            save_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//button[contains(@type, 'primary') and contains(text(), 'Save')]"))
            )

            save_button.click()

            time.sleep(1)

            # 断言保存成功后会有成功的tips
            successful_tip = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "notistack-snackbar"))
            )
            assert successful_tip is not None, "add to cart fail"

            # 断言tips 元素的文本内容为 'New delivery address added'
            successful_text = successful_tip.text
            assert "New delivery address added" in successful_text, "添加地址不成功"


        except Exception as e:
            self.fail(f"测试失败: {e}")

    def test_6_clear_cart(self):
        # 模拟随机延迟
        time.sleep(random.uniform(1, 3))  # 随机延迟 1 到 3 秒

        # 清除购物车
        self.driver.get("https://www.wizmarketplace.com/cart")

        try:

            delete_selected_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Delete Selected')]"))
            )
            delete_selected_element.click()

            empty_text_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Your cart is empty.')]"))
            )

            assert empty_text_element is not None, "cart it not null"
            
        except Exception as e:
            self.fail(f"测试失败: {e}")


    def test_9_change_password_back(self):
        # 模拟随机延迟
        time.sleep(random.uniform(1, 3))  # 随机延迟 1 到 3 秒
        self.driver.get("https://www.wizmarketplace.com/user/my-profile")

        # # 读取数据文件
        with open('tests/data/validData.txt', 'r') as file:
            lines = file.readlines()

        new_password = lines[1].strip()

        # # 读取数据文件
        
        changePassword_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[text()='Change password']"))
        )
        assert changePassword_link is not None, "找不到 Change password 链接"

        changePassword_link.click()


        current_password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "password"))
        )

        current_password_input.send_keys("Test123456")

        # # 使用 By.NAME 选择器来定位元素
        new_password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "newPassword"))
        )
        
        # # 断言元素存在
        assert new_password_input is not None, "新密码输入框不存在"

        new_password_input.send_keys(new_password)


        confirm_password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "confirmPassword"))
        )

        confirm_password_input.send_keys(new_password)

        save_changes_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='SAVE CHANGES']"))
        )
    
        # # 点击按钮
        save_changes_button.click()

        time.sleep(1)

        # # 使用 WebDriverWait 等待元素变得可见
        success_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "notistack-snackbar"))
        )
    
        # # 获取元素的文本内容
        message_text = success_message.text.strip()

        # # 断言元素存在，并且文案是 "Password has been updated successfully"
        assert success_message is not None, "成功提示元素不存在"
        assert message_text == "Password has been updated successfully", "成功提示文案不符合预期"

        
             


    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        cls.driver.quit()
        
        

if __name__ == "__main__":
    unittest.main()
