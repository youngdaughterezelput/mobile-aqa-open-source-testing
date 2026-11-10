from pages.shop_page import ShopPage


def test_recorded_add_to_cart_flow(driver):
    shop = ShopPage(driver)
    shop.open_first_image()
    shop.select_view_group()
    shop.open_second_image()
    shop.add_to_cart()
