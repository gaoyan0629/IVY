import optparse
usage = ("polotools [options]")
parser = optparse.OptionParser(version="polotools abc", usage=usage)
parser.add_option('--amrsim', dest='amrsim', action='store_true',
    help=('Set amr simulation mode, skips if not present'))    

groupAMR = optparse.OptionGroup(parser,'AMR simulation:',
                "ATENTION: use these options only with --amrsim")
groupAMR.add_option('--Utility', dest='Utility', action='store',
    help=('Set utility rate for AMR simulation, accept dictionary'))

parser.add_option_group(groupAMR)

(options, args) = parser.parse_args()
