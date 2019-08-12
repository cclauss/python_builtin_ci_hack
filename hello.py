def hello(who="world"):
    return "Hello {}!".format(who)


def test_hello():
    assert hello() == "Hello world!"
    assert hello("test") == "Hello test!"    


if __name__ == "__main__":
    print()
