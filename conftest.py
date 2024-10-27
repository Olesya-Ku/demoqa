import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def browser():
    """Создает экземпляр браузера для тестов."""
    print("Запускаем браузер...")
    driver = webdriver.Chrome()
    yield driver
    print("Закрываем браузер...")
    driver.quit()