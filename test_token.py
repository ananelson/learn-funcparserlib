from token_class import Token

### "test-strings"
def test_strings():
    token = Token(51, '*')
    assert str(token) == "0,0-0,0 OP  '*'"
    assert unicode(token) == u"0,0-0,0 OP  '*'"

### "test-repr"
def test_repr():
    token = Token(51, '*')
    assert repr(token) ==  "Token(51, '*', (0, 0), (0, 0), '')"

### "test-eq"
def test_equality():
    token1 = Token(51, '*', (1,1), (2,1))
    token2 = Token(51, '*', (2,1), (3,1))
    token3 = Token(2, '3', (2,1), (3,1))

    assert token1 == token1
    assert token1 == token2

    assert token1 != token3
    assert token2 != token3
