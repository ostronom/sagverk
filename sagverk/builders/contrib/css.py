from sagverk.builders.simple import ShellBuilder

class LESSBuilder(ShellBuilder):
    """ Compiles given files via lessc compiler. """
    command = 'lessc'
    def get_command_args(self):
        return self.files

class YUICompressor(ShellBuilder):
    """ Compresses it's input via yui-compressor. """
    command = 'yuicompressor'
    def get_proc_input(self):
        return self.input
    def get_command_args(self):
        return ['--type', 'css']