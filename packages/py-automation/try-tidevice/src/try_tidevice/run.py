import wda


def main():
    c = wda.Client("http://localhost:8200")
    print(c.info)


if __name__ == '__main__':
    main()
