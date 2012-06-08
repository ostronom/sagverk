import os
import subprocess

from base import BaseBuilder, BuilderException

class ProxyBuilder(BaseBuilder):
	pass

class ConcatFilesBuilder(BaseBuilder):
	""" Simple builder that concatenates it's all input files into one and returns result as a string. """
	def build(self):
		out = []
		for filename in self.files:
			with open(filename, 'r') as f:
				out.append(f.read())
		return (self.kwargs.get('separator','')).join(out)

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
		kwargs = {'stdin': subprocess.PIPE, 'stderr': subprocess.PIPE, 'stdout': subprocess.PIPE, 'cwd': self.cwd}
		proc   = subprocess.Popen(args, **kwargs)
		out, err = proc.communicate(self.get_proc_input())
		if proc.returncode:
			raise BuilderException, u'%s returned:\n %s' % (self.command, err)
		if err:
			print 'There was STDERR output from %s:\n%s' % (self.command, err)
		return out