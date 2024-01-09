import commonSetup
driver = commonSetup.driver

driver.get('https://www.google.co.kr/')
# driver.find_element_by_css_selector()




# static void waitForLoad(WebDriver driver) {
#     new WebDriverWait(driver, 30).until((ExpectedCondition<Boolean>) wd ->
# ((JavascriptExecutor) wd).executeScript("return document.readyState").equals("complete"));
# }
