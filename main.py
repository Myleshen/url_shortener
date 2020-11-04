from url_shortner.shortener import Shortener


def main():
    shortener = Shortener()
    input_url = input("Enter the URL to shorten: ")
    short_url = shortener.create_unique_url(input_url)
    print(short_url)
    list_urls(shortener)


def list_urls(shortener):
    print(shortener.list_urls_in_db())


if __name__ == "__main__":
    main()
