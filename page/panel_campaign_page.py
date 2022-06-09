import time

from base.page_base import BaseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from base import data


class PanelCampaignPage(BaseClass):
    """
    Campaign settings created in this class

    """
    SAVE_BUTTON = (By.ID, "save-and-next")
    PAGE_RULES_BUTTON = (By.CLASS_NAME, "qa-page-rules")
    PAGE_RULES_DROP_DOWN = (By.ID, "conditionList0")
    PAGE_TYPE_INPUT = (By.ID, "qa-drop-down")
    PAGE_TYPE_BUTTON = (By.CLASS_NAME, "conditionList0-page-type")
    ADD_NEW_VARIANT_BUTTON = (By.ID, "add-new-variation")
    VARIANT_SAVE_BUTTON = (By.CLASS_NAME, "btn-save")
    FIRST_TEMPLATE_OVERLAY = (By.CLASS_NAME, "overlay")
    FIRST_TEMPLATE_SELECT_BUTTON = (By.CLASS_NAME, "btn-select")
    INFORMATION_OK_BUTTON = (By.CLASS_NAME, "inline-select-notification-confirm")
    IFRAME_HEADER = (By.ID, "sticky-header")
    EDIT_IFRAME = (By.ID, "iframe-edit")
    INSERT_AFTER_BUTTON = (By.CLASS_NAME, "append-after")
    CAMPAIGN_SAVE_BUTTON = (By.CLASS_NAME, "btn-save")
    VARIANT_NAME_INPUT = (By.NAME, "variationName")
    LANGUAGE_DROP_DOWN = (By.ID, "personalization-language")
    ALL_LANGUAGES_BUTTON = (By.CLASS_NAME, "personalization-language-all-languages")
    END_DATE = (By.CLASS_NAME, "reportrange-text")
    YEAR_UP_BUTTON = (By.CLASS_NAME, "yearselect")
    END_TIME = (By.NAME, "endHour")
    SET_TIME_BUTTON = (By.CLASS_NAME, "option__0")
    NOTE_TEXT_AREA = (By.ID, "note")
    TEST_RADIO_BUTTON = (By.ID, "Test")
    RULES_ROUTER = (By.CLASS_NAME, "in-steps-wrapper__steps")
    IFRAME = (By.ID, "iframe-edit")
    ADD_GOAL_BUTTON = (By.ID, "add-new-goal")

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        super().__init__(self.driver)

    def create_campaign(self):
        """
        Create new campaign and edit settings

        """
        self.presence_for_element(self.SAVE_BUTTON).click()
        self.move_to_element(self.PAGE_RULES_BUTTON)
        self.presence_for_element(self.PAGE_RULES_DROP_DOWN).click()
        self.presence_for_element(self.PAGE_TYPE_BUTTON).click()
        data.rule = self.presence_for_element(self.PAGE_RULES_DROP_DOWN).text
        data.page_type = self.presence_for_element(self.PAGE_TYPE_INPUT).text
        self.presence_for_element(self.SAVE_BUTTON).click()
        self.presence_for_element(self.ADD_NEW_VARIANT_BUTTON).click()
        time.sleep(10)
        self.move_to_element(self.FIRST_TEMPLATE_OVERLAY)
        self.presence_for_element(self.FIRST_TEMPLATE_SELECT_BUTTON).click()
        self.clickable_for_element(self.INFORMATION_OK_BUTTON).click()
        self.driver.switch_to.frame("iframe-edit")
        self.presence_for_element(self.IFRAME_HEADER).click()
        self.driver.switch_to.default_content()
        self.presence_for_element(self.INSERT_AFTER_BUTTON).click()
        self.move_to_element(self.CAMPAIGN_SAVE_BUTTON)
        data.variant_name = self.presence_for_element(self.VARIANT_NAME_INPUT).get_attribute("id")
        self.presence_for_element(self.SAVE_BUTTON).click()
        self.presence_for_element(self.ADD_GOAL_BUTTON)
        self.presence_for_element(self.SAVE_BUTTON).click()
        self.presence_for_element(self.LANGUAGE_DROP_DOWN).click()
        self.presence_for_element(self.ALL_LANGUAGES_BUTTON).click()
        self.presence_for_all_elements(self.END_DATE)[1].click()
        self.presence_for_element(self.YEAR_UP_BUTTON).click()
        self.presence_for_element(self.YEAR_UP_BUTTON).clear()
        self.send_keys(self.YEAR_UP_BUTTON, "2023")
        self.send_keys(self.NOTE_TEXT_AREA, data.qa_note)
        self.driver.execute_script("arguments[0].click()", self.presence_for_element(self.TEST_RADIO_BUTTON))
        self.presence_for_element(self.SAVE_BUTTON).click()
