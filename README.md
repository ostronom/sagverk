AssetsBuilder
=============

python assets builder

Pipelined assets building system.

Builders operations:
- `builder1 & builder2` produces new builder with input == concatenated builder1 and builder2 outputs
- `builder1 ^ builder2` executes builder1, forgets it's output and return builder2
- `builder1 | builder2` sets builder2 input == builder1 output
- `builder1 > 'somefilename.ext'` writes builder1 output to 'somefilename.ext' and returns builder1