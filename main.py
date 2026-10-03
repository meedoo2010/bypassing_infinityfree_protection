from playwright.sync_api import sync_playwright

SITE = "URL_YOU_WANT_TO_SCRAPE"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    context = browser.new_context(
        user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/153.0.0.0 Safari/537.36"
        )
    )

    page = context.new_page()

    page.goto(SITE, wait_until="networkidle")

    rendered_html = page.content()

    raw_html = context.request.get(SITE).text()

    with open("rendered.html", "w", encoding="utf-8") as f:
        f.write(rendered_html)

    with open("raw.html", "w", encoding="utf-8") as f:
        f.write(raw_html)

    print(rendered_html)

    browser.close()
