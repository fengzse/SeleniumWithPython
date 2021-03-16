from main import TestSelenium

amazon_url = "http://www.amazon.com"
amazon = TestSelenium(amazon_url)

print(amazon)
amazon.func('selenium book', 'java', 'python')
amazon.break_connection()

