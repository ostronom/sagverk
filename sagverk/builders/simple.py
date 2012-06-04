import os
import subprocess

from base import BaseBuilder, BuilderException

class ProxyBuilder(BaseBuilder):
	pass

class ConcatFilesBuilder(BaseBuilder):
	""" Simple builder that concatenates it's all input files into one and returns result as a string. """
	def build(self):
		out = ''
		for filename in self.files:
			with open(filename, 'r') as f:
				out += f.read()
		return out

class ShellBuilder(BaseBuilder):
	""" Shell builder --- produces it's output using external applications. """
	def get_command_args(self):
		""" Should return external program arguments as list. """ 
		return []
	def get_proc_input(self):
		""" Should return string, that will be sent to external application's stdin. """ 
		return None
	def build(self):
		""" Executes command and returns it's output, of fails with exception if external application returned non-zero exit code. """
		args = [self.command]
		args.extend(self.get_command_args())
		kwargs = {'stdin': subprocess.PIPE, 'stderr': subprocess.STDOUT, 'stdout': subprocess.PIPE, 'cwd': self.get_cwd()}
		proc   = subprocess.Popen(args, **kwargs)
		out, _ = proc.communicate(self.get_proc_input())
		if proc.returncode:
			raise BuilderException, u'%s returned:\n %s' % (self.command, out)
		return out