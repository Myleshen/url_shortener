from url_shortner.shortener import Shortener


def main():
    shortener = Shortener()
    # input_url = input("Enter the URL to shorten: ")
    # short_url = shortener.create_unique_url(input_url)
    # print(short_url)
    list_urls(shortener)
    short_url = "www.sample.in/cb9e1c5"
    get_long(shortener, short_url)


def list_urls(shortener):
    print(shortener.list_urls_in_db())


def get_long(shortener, short_url):
    print(shortener.get_original_url(short_url))


if __name__ == "__main__":
    main()
