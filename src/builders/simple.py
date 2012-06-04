import os
import subprocess
import tempfile

from base import BaseBuilder, BuilderException

class ProxyBuilder(BaseBuilder):
	pass

class ConcatFilesBuilder(BaseBuilder):
	def build(self):
		out = ''
		for filename in self.files:
			with open(filename, 'r') as f:
				out += f.read()
		return out

class ShellBuilder(BaseBuilder):
	def get_command_args(self):
		return []
	def get_proc_input(self):
		return None
	def build(self):
		args = [self.command]
		args.extend(self.get_command_args())
		kwargs = {'stdin': subprocess.PIPE, 'stderr': subprocess.STDOUT, 'stdout': subprocess.PIPE, 'cwd': self.get_cwd()}
		proc   = subprocess.Popen(args, **kwargs)
		out, _ = proc.communicate(self.get_proc_input())
		if proc.returncode:
			raise BuilderException, u'%s returned:\n %s' % (self.command, out)
		return out