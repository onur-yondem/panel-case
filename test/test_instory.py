import time
import unittest
from selenium import webdriver
from page.panel_login_page import PanelLoginPage
from page.panel_main_page import PanelMainPage
from page.panel_campaign_page import PanelCampaignPage
from base import data


class AmazonHappyPath(unittest.TestCase):
    website = "https://seleniumautomation.inone.useinsider.com/instory-all"
    executable_path = "/home/onuryondem/automation/panel-case/chromedriver"

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--allow-running-insecure-content")
        self.driver = webdriver.Chrome(self.executable_path, options=options)
        self.driver.maximize_window()
        self.driver.get(self.website)
        self.login_page = PanelLoginPage(self.driver)
        self.main_page = PanelMainPage(self.driver)
        self.campaign_page = PanelCampaignPage(self.driver)

    def test_case(self):
        """Test case is:
        1. Go to Inone page
        2. A new campaign is created
        3. Campaign details are checked
        4. API is generated
        5. Go to the campaign with the test link
        6. Verify that the campaign is running

        """

        self.login_page.login()
        self.main_page.create_base_campaign()
        self.campaign_page.create_campaign()
        check_details = self.main_page.check_details()
        self.assertTrue(check_details, "There is a problem.Details is wrong")
        self.main_page.generate_check()
        self.main_page.navigate_to_test_link()
        check_campaign_visible = self.main_page.check_campaign_visible(data.var_id)
        self.assertTrue(check_campaign_visible, "There is a problem. Campaign not visible")

    def tearDown(self):
        self.driver.quit()
