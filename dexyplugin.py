from dexy.reporters.output import OutputReporter

class Custom(OutputReporter):
    """
    Store output in separate gh-pages branch.
    """
    aliases = ['custom']
    _settings = {
            'dir' : '../learn-funcparserlib-output',
            'readme-filename' : None
            }
