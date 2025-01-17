from Playwright_automation import oop

def test_oop():
    iphone = oop.MobileDevice("iphone", "iOS", 14, True, 6000)
    iphone.print_parameters()