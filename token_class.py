### "import-tok-name"
from token import tok_name

### "init"
class Token(object):
    def __init__(self, code, value, start=None, stop=None, line=None):
        self.code = code
        self.value = value
        self.start = start or (0,0)
        self.stop = stop or (0,0)
        self.line = line or ''

### "name"
    @property
    def name(self):
        return tok_name[self.code]

### "unicode"
    def __unicode__(self):
        pos = u'-'.join(u'%d,%d' % x for x in [self.start, self.stop])
        return u"%s %s  '%s'" % (pos, self.name, self.value)

### "str"
    def __str__(self):
        return str(unicode(self))

### "repr"
    def __repr__(self):
        args = (self.code, self.value, self.start, self.stop, self.line)
        return "Token(%r, %r, %r, %r, %r)" % args

### "eq"
    def __eq__(self, other):
        return (self.code, self.value) == (other.code, other.value)
