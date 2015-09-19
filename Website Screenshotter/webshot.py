import spynner

def takeSnapshot(website):
    browser = spynner.Browser()
    browser.load(website)
    browser.snapshot().save('test.png')
    browser.close()

website = raw_input("URL: ")
takeSnapshot(website)
