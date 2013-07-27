### @export "generate-tokens"
from tokenize import generate_tokens

### @export "readline"
from StringIO import StringIO
ts = list(generate_tokens(StringIO('3 * (4 + 5)').readline))
ts

### @export "pprint"
from pprint import pformat
print pformat(ts)
