[TOC]

## Lexing with `tokenize`

Python's [`tokenize`](http://docs.python.org/2/library/tokenize.html) library
was designed to lex Python source code and turn the elements into tokens, but
because tokens can be very generic, this tokenizer can be used for parsing
elements other than python source code too.

To begin to tokenize input, we import the [`generate_tokens`](http://docs.python.org/2/library/tokenize.html#tokenize.generate_tokens) method:

{{ d['basic-tokenizing.py|idio|pycon|pyg']['generate-tokens'] }}

This method should be called with an argument which acts like the `readline`
function on a file object. In order to call this on a string, we need to create
a StringIO instance and pass its readline function:

{{ d['basic-tokenizing.py|idio|pycon|pyg']['readline'] }}

We'll use `pprint` to make this easier to read:

{{ d['basic-tokenizing.py|idio|pycon|pyg']['pprint'] }}

Each token is a 5-tuple of the token code, the token string, the beginning and
ending of the token, and the line on which it was found.

## A Token Class

To make the output from the tokenizer easier to work with, we'll create a Token
class.

{{ d['token_class.py|idio']['init'] }}

The name corresponding to the `code` in the tuple returned from the tokenizer
can be deciphered from the `tok_name` dict in the built-in
[`token`](http://docs.python.org/2/library/token.html#token.tok_name) module.

We define a `name` property to retrieve this:

{{ d['token_class.py|idio']['name'] }}

And we use this in the `__unicode__` and `__str__` methods:

{{ d['token_class.py|idio']['unicode'] }}

{{ d['test_token.py|idio']['test-strings'] }}

We implement a `__repr__` method:

{{ d['token_class.py|idio']['repr'] }}

{{ d['test_token.py|idio']['test-repr'] }}

And an `__eq__` method:

{{ d['token_class.py|idio']['eq'] }}

{{ d['test_token.py|idio']['test-eq'] }}
