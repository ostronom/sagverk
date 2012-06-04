from builders.simple import ProxyBuilder, ShellBuilder, ConcatFilesBuilder

class LESS(ShellBuilder):
	command = 'lessc'
	def get_command_args(self):
		return self.files

class CompressCSS(ShellBuilder):
	command = 'yuicompressor'
	def get_proc_input(self):
		return self.input
	def get_command_args(self):
		return ['--type', 'css']

BOOTSTRAP_LOC = 'assets/css/bootstrap/'
concatless = ConcatFilesBuilder(*map(lambda w: BOOTSTRAP_LOC+w, ['custom.less', 'custom2.less', 'bootstrap.less'])) > 'assets/css/bootstrap/concatenated.less'
less       = LESS('assets/css/bootstrap/concatenated.less')
corecss    = concatless ^ less | CompressCSS() > 'core.css'

# contribjs = CoffeeScriptBuilder('assets/js/contrib/*.coffee')
# vendorjs  = ProxyBuilder('assets/js/vendor/*.js', first='jquery.js')
# corecoffe = CoffeeScriptBuilder('assets/js/core.coffee')
# corejs    = (contribjs & vendorjs & corecoffe) | compressjs > 'core.js'