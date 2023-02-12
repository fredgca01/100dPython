from playwright.sync_api import sync_playwright


header={
    "Accept-Language":"fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3", "userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"
}

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    browser_context = browser.new_context(extra_http_headers=header)
    page = browser_context.new_page()
    page.goto("https://www.wikipedia.org/")
    page.query_selector("#js-link-box-fr").click()
    page.wait_for_timeout(1000)
    result = page.get_by_title("Spécial:Statistiques")
    print(result.inner_text())
    search = page.get_by_placeholder("Rechercher sur Wikipédia")
    search.fill("Python")
    page.keyboard.press(key="Enter")
    page.wait_for_timeout(10000)