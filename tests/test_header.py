import pytest
from locators.header_locators import HeaderLocators
from locators.shop_locators import ShopLocators


@pytest.mark.parametrize("control", ["MENU", "LOGO", "SORT", "CART"])
def test_header_controls_are_visible(pages, control):
    header = pages.header()
    assert header.visible(getattr(HeaderLocators, control))


def test_menu_opens_and_returns_to_catalog(pages):
    header = pages.header()
    header.open_menu()
    assert header.visible(HeaderLocators.CATALOG_ITEM)
    header.open_catalog_from_menu()
    assert header.visible(ShopLocators.PRODUCTS_SCREEN)


def test_sort_menu_shows_all_options(pages):
    header = pages.header()
    header.open_sort()
    for option in HeaderLocators.SORT_OPTIONS.values():
        assert header.visible(option)
