from main import multiply


def test_multiply():
    # testing out multiply function
    assert multiply(4, 6) == 24
    assert multiply(17, 12) == 204


if __name__ == "__main__":
    test_multiply()
