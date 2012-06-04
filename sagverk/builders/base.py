import os

class BuilderException(Exception):
	pass

class BaseBuilder(object):
	"""
	Base class for all builders.
	Defines all pipelined operators, input/output properties and their evaulation.
	"""
	_input  = None
	_output = None
	def __init__(self, *files, **kwargs):
		self.files = files

	@property
	def input(self):
		return self._input

	@input.setter
	def input(self, value):
		self._input = value

	@property
	def output(self):
		"""
		Evaluates builder (runs it's :py:meth:`build` function) and returns it's output.
		Runs once, every other run will return result of the first run.
		""" 
		if self._output is None:
			self._output = self.build()
		return self._output

	def get_cwd(self):
		"""
		Returns current working directory.
		"""
		return os.getcwd()

	def __lt__(self, receiver):
		raise NotImplemented, 'No injecting yet'

	def __gt__(self, receiver):
		"""
		Usage::
		
			builder > 'output.ext'

		Finalizes builder and saves builder output to 'output.ext'.
		"""
		#print 'saving to %s' % receiver
		with open(receiver, 'w') as f:
			f.write(self.output)
		return self

	def __or__(self, receiver):
		"""
		Builders conveyer. Usage::

			builder1 | builder2
		
		Pushes builder1 output to builder2 input.
		"""
		receiver.input = self.output
		return receiver

	def __and__(self, other):
		"""
		Builders concatenator. Usage::

			builder1 & builder2

		Creates new builder, pushing builder1 and builder2 output concatenated (in that order) to new builders input.
		"""
		concatBuilder = BaseBuilder()
		try:
			concatBuilder.input = self.output + other.output
		except TypeError, e:
			raise BuilderException, 'Unconcatenable output types' 
		return concatBuilder 

	def __xor__(self, other):
		"""
		Builders sequental 'forgetter'. Usage::

			builder1 ^ builder2

		Forgets output of builder1, returns builder.
		"""
		return other

	def build(self):
		"""
		Builders's build method --- defines builder's behaviour.
		Should return 'string' output which will be set to output property of builder.
		"""
		pass