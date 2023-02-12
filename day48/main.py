from playwright.sync_api import sync_playwright



header={
    "Accept-Language":"fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3", "userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"
}

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    browser_context = browser.new_context(extra_http_headers=header)
    page = browser_context.new_page()
    page.goto("https://python.org/events")
    page.wait_for_timeout(1000)
    
    event_list=[]
    all_events = page.query_selector(".list-recent-events.menu")
    events = all_events.query_selector_all("li")
    for event in events:
        data = {}
        data["name"]=event.query_selector("h3").inner_text()
        data["date"]=event.query_selector("time").inner_text()
        data["location"]=event.query_selector("span").inner_text()
        event_list.append(data)
    
    print(event_list)
