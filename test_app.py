import unittest
import csv
import os
import time 
import uuid
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException


class TestAutomation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        
        unique_user_data_dir = f"/tmp/chrome_{uuid.uuid4().hex}"
        options.add_argument(f"--user-data-dir={unique_user_data_dir}")
        
        cls.driver = webdriver.Chrome(options=options)
        cls.wait = WebDriverWait(cls.driver, 20)  
        cls.delay = 2 
        
        cls.base_dir = "/app"
        cls.index_url = f"file://{cls.base_dir}/index.html"
        cls.data_url = f"file://{cls.base_dir}/data-page.html"

    def _slow_down(self):
        """Adiciona uma pausa pequena entre ações"""
        time.sleep(self.delay)

    def test_01_login(self):
        """Teste de autenticação no sistema"""
        try:
            print("\nExecutando teste de login...")
            
            self._slow_down()
            self.driver.get(self.index_url)
            print(f"Página carregada: {self.driver.current_url}")
            self._slow_down()
            
            
            self.assertIn("index.html", self.driver.current_url)
            
            username = self.wait.until(
                EC.visibility_of_element_located((By.ID, "username"))
            )
            self._slow_down()
            username.send_keys("test_user")
            self._slow_down()
            
            password = self.driver.find_element(By.ID, "password")
            password.send_keys("secure_password")
            self._slow_down()
            
            self._slow_down()
            login_btn = self.driver.find_element(By.ID, "login-btn")
            login_btn.click()
            self._slow_down()
            
            self.wait.until(
                lambda driver: "home.html" in driver.current_url
            )
            self._slow_down()
            
            welcome_msg = self.wait.until(
                EC.visibility_of_element_located((By.ID, "welcome-message"))
            )
            self._slow_down()
            self.assertIn("Welcome, test_user", welcome_msg.text)
            print("Login realizado com sucesso!")
            self._slow_down()
            
        except Exception as e:
            self._take_screenshot("login_error")
            raise

    def test_02_data_extraction(self):
        """Teste de extração de dados da tabela"""
        try:
            print("\nExecutando teste de extração de dados...")
            self._slow_down()
            
            self.driver.get(self.index_url)
            self._slow_down()
            
            username = self.wait.until(EC.visibility_of_element_located((By.ID, "username")))
            username.send_keys("test_user")
            self._slow_down()
            
            password = self.driver.find_element(By.ID, "password")
            password.send_keys("secure_password")
            self._slow_down()
            
            login_btn = self.driver.find_element(By.ID, "login-btn")
            login_btn.click()
            self._slow_down()
            
            self.driver.get(self.data_url)
            print(f"Página carregada: {self.driver.current_url}")
            self._slow_down()
            
            self.assertIn("data-page.html", self.driver.current_url)
            self._slow_down()
            
            table = self.wait.until(
                EC.presence_of_element_located((By.ID, "data-table"))
            )
            self._slow_down()
            
            rows = table.find_elements(By.TAG_NAME, "tr")
            data = []
            
            for row in rows:
                cols = row.find_elements(By.TAG_NAME, "td")
                if cols:
                    data.append([col.text for col in cols])
                self._slow_down() 
            
            csv_path = os.path.join(self.base_dir, "extracted_data.csv")
            with open(csv_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(data)
            
            print(f"Dados extraídos e salvos em {csv_path}")
            self._slow_down()
            self.assertTrue(len(data) > 0, "Nenhum dado foi extraído da tabela")
            
        except Exception as e:
            self._take_screenshot("data_extraction_error")
            raise

    def _take_screenshot(self, name):
        """Método auxiliar para tirar screenshots"""
        try:
            screenshot_path = os.path.join(self.base_dir, f"{name}.png")
            self.driver.save_screenshot(screenshot_path)
            print(f"Erro capturado. Screenshot salvo em: {screenshot_path}")
        except WebDriverException as e:
            print(f"Falha ao tirar screenshot: {str(e)}")

    @classmethod
    def tearDownClass(cls):
        try:
            if cls.driver:
                time.sleep(1)  
                cls.driver.quit()
                print("\nNavegador fechado com sucesso")
        except Exception as e:
            print(f"Erro ao fechar o navegador: {str(e)}")


if __name__ == "__main__":
    unittest.main(verbosity=1)