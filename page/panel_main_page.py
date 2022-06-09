import time

from base.page_base import BaseClass
from selenium.webdriver.common.by import By
from datetime import datetime
from base import data


class PanelMainPage(BaseClass):
    """
    Campaign details and statuses are checked

    """
    CREATE_BUTTON = (By.ID, "create-mobile-campaign")
    CAMPAIGN_NAME_INPUT = (By.ID, "campaign-name")
    ACCEPT_BUTTON = (By.ID, "accept")
    SEARCH_BAR = (By.ID, "search-value")
    CAMPAIGN_ROW = (By.CLASS_NAME, "vuetable-body")
    TEST_LINK_BUTTON = (By.CLASS_NAME, "test-link")
    TEST_LINK_WRAPPER_BUTTON = (By.CLASS_NAME, "test-link-wrapper_menu")
    TEST_LINK_SUB_BUTTON = (By.CSS_SELECTOR, ".test-link-wrapper_sub-menu a")
    VARIATION_BUTTON = (By.CLASS_NAME, "test-link-wrapper_menu")
    DETAILS_BUTTON = (By.CSS_SELECTOR, ".button > p")
    PERSONALIZATION_NOTE = (By.CLASS_NAME, "personalization-note")
    PERSONALIZATION_RULE = (By.CLASS_NAME, "personalization-rule-0")
    DETAILS_CLOSE_BUTTON = (By.CLASS_NAME, "qa-close")
    VAR_ID_ELEMENT = (By.CLASS_NAME, "personalization-id")
    GENERATE_MENU = (By.ID, "dropDownList")
    GENERATE_BUTTON = (By.CLASS_NAME, "in-header-wrapper__links")
    SORT_TABLE_ELEMENT = (By.CLASS_NAME, "sortable")
    INSPECTOR_TITLE = (By.CLASS_NAME, "inspector-title")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)
        date_time = datetime.now()
        data.campaign_name = "selenium-" + str(datetime.timestamp(date_time))

    def create_base_campaign(self):
        """
        Campaign name is written

        """
        self.presence_for_element(self.CREATE_BUTTON).click()
        time.sleep(3)
        self.send_keys(self.CAMPAIGN_NAME_INPUT, data.campaign_name)
        self.presence_for_element(self.ACCEPT_BUTTON).click()

    def check_status(self):
        """
        Campaign status is checked

        """
        self.send_keys(self.SEARCH_BAR, data.campaign_name)
        self.presence_for_element(self.SORT_TABLE_ELEMENT)
        row_data = self.presence_for_element(self.CAMPAIGN_ROW).text
        new_row_data = row_data.split("\n")
        return new_row_data[0] == "Test"

    def generate_check(self):
        """
        API is Generated

        """
        self.driver.execute_script("arguments[0].click()", self.presence_for_element(self.GENERATE_MENU))
        self.driver.execute_script("arguments[0].click()", self.presence_for_all_elements(self.GENERATE_BUTTON)[1])
        time.sleep(20)

    def check_variation_link(self):
        """
        Variation link is checked

        """
        self.presence_for_element(self.TEST_LINK_BUTTON).click()
        variation_text = self.presence_for_all_elements(self.VARIATION_BUTTON)[0].text
        return variation_text == data.variant_name

    def check_details(self):
        """
        Campaign details are checked

        """
        self.presence_for_element(self.DETAILS_BUTTON).click()
        personalization_text = self.presence_for_element(self.PERSONALIZATION_NOTE).text
        personalization_rule_text = self.presence_for_element(self.PERSONALIZATION_RULE).text
        data.var_id = self.presence_for_element(self.VAR_ID_ELEMENT).text
        self.presence_for_element(self.DETAILS_CLOSE_BUTTON).click()
        return personalization_text == data.qa_note and personalization_rule_text == data.rule + " is " + data.page_type

    def navigate_to_test_link(self):
        """
        Go to test link

        """
        self.move_to_element(self.TEST_LINK_BUTTON)
        self.move_to_element(self.TEST_LINK_WRAPPER_BUTTON, False)
        self.move_to_element(self.TEST_LINK_SUB_BUTTON)

    def check_campaign_visible(self, campaign_id):
        """
        Campaign presence is checked
        :param campaign_id: ID of the campaign on the panel

        """
        self.driver.switch_to.window(self.driver.window_handles[1])
        campaign = self.driver.execute_script("return JSON.parse(window.localStorage.getItem(arguments[0]))",
                                              "sp-camp-" + campaign_id)
        return campaign.get("data").get("step1-displayed")
