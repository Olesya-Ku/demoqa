def test_example(browser):
    browser.get('http://example.com')
    assert 'Example Domain' in browser.title