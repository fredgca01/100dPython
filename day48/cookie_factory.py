from playwright.sync_api import sync_playwright, ElementHandle
import threading

HEADERS={
    "Accept-Language":"fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3", 
    "userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"
}

CONTINUE_CLICK=True

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    browser_context = browser.new_context(extra_http_headers=HEADERS)
    page = browser_context.new_page()
    page.goto("http://orteil.dashnet.org/experiments/cookie/")
    page.wait_for_timeout(1000)
    cookier = page.locator("#cookie")
    money = page.locator("#money")
    shop = page.query_selector("#store")

    def buy_items(shop: ElementHandle) -> None:
        global CONTINUE_CLICK
        CONTINUE_CLICK=True
        desks = shop.query_selector_all("div")
        desks.reverse()
        items = []
        for desk in desks :
            if desk.get_attribute("class") != "grayed": 
                result = desk.query_selector("b")
                if result != None:
                    try:
                        desk.click()
                        page.wait_for_timeout(100)
                    except Exception as e :
                        print(e)
                        print(desk.inner_html())

    def buyer():
        global CONTINUE_CLICK
        CONTINUE_CLICK=False

    while True:
        timer = threading.Timer(5,buyer)
        timer.start()
        while CONTINUE_CLICK:
            cookier.click()
            page.wait_for_timeout(100)
        buy_items(shop)
        #timer.cancel()
