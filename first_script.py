from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.python.org/")
    page.pause()
    page.get_by_role("menubar", name="Main Navigation").get_by_role("link", name="Downloads").click()
    page.get_by_role("banner").get_by_role("link", name="Windows").click()
    page.get_by_role("link", name="Latest Python 3 Release - Python 3.11.4").click()
    with page.expect_download() as download_info:
        page.get_by_role("link", name="Windows installer (64-bit)").click()
    download = download_info.value

    # ---------------------
    context.close()
    browser.close()
    print("konec...")

with sync_playwright() as playwright:
    run(playwright)
