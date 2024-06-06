import uiautomator2 as u2


def main():
    # android device:
    device = "10.211.1.129:41941"

    # connect
    d = u2.connect(device)  # connect to device

    # device info
    print(d.info)


if __name__ == '__main__':
    main()
