from url_shortner.shortener import Shortener


demo = Shortener()
print(demo.create_unique_url(f"https://www.google.com/search?q="))
