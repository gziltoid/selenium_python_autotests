from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_card(self):
        add_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CARD)
        add_button.click()

    def should_be_correct_total_price_in_message(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), "Message about adding item to card " \
                                                                                   "is not present. "
        assert self.is_element_present(*ProductPageLocators.ITEM_PRICE), "Item price is not present."
        assert self.is_element_present(*ProductPageLocators.CARD_TOTAL_PRICE), "Total price is not present."
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        card_total_price = self.browser.find_element(*ProductPageLocators.CARD_TOTAL_PRICE).text
        assert item_price == card_total_price, f"Item price doesn't equal to total price in card. Expected {item_price}, got {card_total_price}. "

    def should_be_correct_item_title_in_message(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_WITH_CARD_TOTAL), "Message with total price is not " \
                                                                                      "present. "
        assert self.is_element_present(*ProductPageLocators.ITEM_TITLE), "Item title is not present."
        assert self.is_element_present(*ProductPageLocators.ADDED_TO_CARD_ITEM_TITLE), "Added item title is " \
                                                                                       "not present. "
        title = self.browser.find_element(*ProductPageLocators.ITEM_TITLE).text
        added_title = self.browser.find_element(*ProductPageLocators.ADDED_TO_CARD_ITEM_TITLE).text
        assert title == added_title, f"Item title isn't equal to item title in card. Expected {title}, got {added_title}."

    def should_be_add_to_card_button(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_CARD), "Add to card button is not present."
