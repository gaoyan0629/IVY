from __future__ import absolute_import
import optparse
import sys
from optparse import Option
from functools import partial

print 'ARGV      :', sys.argv[1:]

parser = optparse.OptionParser()
"""
help_ = partial(
    Option,
    '-h', '--help',
    dest='help',
    action='help',
    help='Show help.')
"""

# parser.add_option('-h', '--help', 
# parser.add_option('-h', 
#                   dest='help', 
#                   action='help',
#                   help='show help'
#                   )

parser.add_option('-o', '--output', 
                  dest="output_filename", 
                  default="default.out",
                  help = 'show me the file'
                  )
adm = partial(
        Option,
        '-a',
        dest='adm_file',
        default = 'adm.xlsx',
        help = 'adm file name'
        )
parser.add_option(adm())
    

parser.add_option('-v', '--verbose',
                  dest="verbose",
                  default=False,
                  action="store_true",
                  help = 'verbose version'
                  )

parser.add_option('--version',
                  dest="version",
                  default=1.0,
                  type="float",
                  )

# opt_args = ['-v','-o','myfile.o']
# opt_args = ['-v','-o','myfile.o']
opt_args = ['-h']
options, remainder = parser.parse_args(opt_args)

print 'VERSION   :', options.version
print 'VERBOSE   :', options.verbose
print 'OUTPUT    :', options.output_filename
print 'REMAINING :', remainder
