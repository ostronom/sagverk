from sagverk.builders.simple import ShellBuilder, ConcatFilesBuilder

class CoffeeScriptBuilder(ShellBuilder):
    """ Compiles input via coffee compiler. """
    command = 'coffee'
    def get_command_args(self):
        return ['--compile', '--stdio']
    def get_proc_input(self):
        return self.input

class ClosureCompiler(ShellBuilder):
    """ Compresses & optimizes input via google closure compiler. """
    command = 'closure'
    def get_command_args(self):
        return [
            '--compilation_level', 'ADVANCED_OPTIMIZATIONS',
            '--logging_level', 'ALL',
            '--process_jquery_primitives'
        ]
    def get_proc_input(self):
        return self.input