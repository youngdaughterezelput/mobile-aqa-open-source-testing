# UI-tests Android

Python, pytest, Appium and Page Object

## Start-up

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Start

Start appium server:

```bash
python -m pytest -v
```

## Structure

## Header tests

`components.header.Header` models the catalog header; `PageFactory` creates page objects for the current driver. `tests/test_header.py` checks the four visible header controls, opening the menu and returning to the catalog, and the four sort choices. The selectors use accessibility IDs observed in Appium Inspector.

Run from the catalog screen with an Appium server and Android device available:

```bash
python -m pytest tests/test_header.py -v
```

Reusable UI components live in `components/`; element selectors live in `locators/`, grouped by component or screen. Pages and components use these selectors, while `PageFactory` creates them with the same driver.
