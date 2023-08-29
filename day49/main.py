from playwright.sync_api import sync_playwright

header={
    "Accept-Language":"fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3", "userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"
}

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    browser_context = browser.new_context(extra_http_headers=header)
    page = browser_context.new_page()
    page.goto("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
    page.wait_for_timeout(1000) 
    page.type('#session_key',"test")
    page.type('#session_password',"pwd")
    page.wait_for_timeout(1000) 
    
    page.goto("https://www.linkedin.com/jobs/search?keywords=Head%20of%20Engineering&location=Ville%20de%20Paris%2C%20%C3%8Ele-de-France%2C%20France&geoId=106383538&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0")
    page.wait_for_timeout(1000)
    #dialog = page.ge
    #print(dialog)