import material_research.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from prettytable import PrettyTable



class Research(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Research, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()    

    def acessar_pag(self):
        self.get(const.URL_BASE)

    def search_type(self, type='property'):
        if type == 'property':
            property_search = self.find_element(
            By.LINK_TEXT, value="Material Property Search"
            )
        property_search.click()
    
    def property_type(self):
        prop_list_box = self.find_element(
        By.ID, value="ctl00_ContentMain_ucPropertyDropdown1_drpPropertyList"
        )
        prop_list_box.click()
        prop_list = prop_list_box.find_elements(
            By.TAG_NAME, 'option'
            )
        for element in prop_list:
            print (prop_list.index(element))
            print(element.get_attribute('innerHTML'))
        prop_selected_index = int(input('Digite o número correspondente a propriedade: '))
        prop_selected = prop_list[prop_selected_index]
        prop_selected.click()
    
    def property_value(self):
        min_value = self.find_element(
            By.XPATH, '/html/body/form[2]/div[4]/table[2]/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/table/tbody/tr[2]/td/span[1]/a'
            ).get_attribute('innerHTML')
        max_value = self.find_element(
            By.XPATH, '/html/body/form[2]/div[4]/table[2]/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/table/tbody/tr[2]/td/span[2]/a'
        ).get_attribute('innerHTML')

        print(min_value)
        print(max_value)

        first_value = int(input(f'Digite uma propriedade mínima entre {min_value} e {max_value}: '))
        second_value = int(input(f'Digite uma propriedade máxima entre {min_value} e {max_value}: '))
        
        self.find_element(
            By.ID, 'ctl00_ContentMain_ucPropertyEdit1_txtpMin'
            ).send_keys(first_value)

        self.find_element(
            By.ID, 'ctl00_ContentMain_ucPropertyEdit1_txtpMax'
            ).send_keys(second_value)
        
    def search(self):
        self.find_element(
            By.ID, 'ctl00_ContentMain_btnSubmit'
        ).click()

    def get_materials_attributes(self):
        collection = []
        table_results = self.find_element(
            By.ID, 'tblResults'
            ).find_elements(By.TAG_NAME, 'tr')
        for result in table_results:
            i = table_results.index(result) + 1
            if i > 1:
                mat_name = result.find_element(
                    By.XPATH, '/html/body/form[2]/div[4]/div[2]/div/table[3]/tbody/tr[{}]/td[3]/a'.format(i)
                    ).get_attribute(
                        'innerHTML'
                        )
                if 'Overview of materials for' in mat_name:
                    mat_name = mat_name[25:]
                else:
                    mat_name = mat_name

                mat_prop = result.find_element(
                    By.XPATH, '/html/body/form[2]/div[4]/div[2]/div/table[3]/tbody/tr[{}]/td[4]'.format(i)
                    ).get_attribute(
                        'innerHTML'
                        )
                prop = ''        
                for c in mat_prop:
                    if c.isdigit() or c in "-":
                        prop = prop + c
                #print(mat_prop)
                collection.append(
                    [mat_name, prop]
                    )
        
        table = PrettyTable(
            field_names = ['Material', 'Property']
        )
        table.add_rows(collection)
        print(table)


    


