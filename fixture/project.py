import re
from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    project_cache = None

    def get_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_projects_page()
            self.project_cache = []
            for row in wd.find_elements_by_xpath("//table[@class='width100']/tbody/tr[starts-with(@class,'row-')]"):
                cells = row.find_elements_by_xpath("td")
                if cells[2].text != 'Włączone':
                    href_text = cells[0].find_element_by_css_selector("a").get_attribute("href")
                    id = re.search("\d+$", href_text).group(0)
                    name = cells[0].text
                    status = cells[1].text
                    self.project_cache.append(
                        Project(name=name, status=status, id=id))
        return list(self.project_cache)

    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Zarządzanie").click()
        wd.find_element_by_link_text("Zarządzanie projektami").click()

    def add(self, name, description):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_css_selector('input[value="Stwórz nowy projekt"]').click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(name)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(description)
        wd.find_element_by_css_selector('input[value="Dodaj projekt"]').click()
        wd.find_element_by_link_text("Dalej").click()
        self.project_cache = None
