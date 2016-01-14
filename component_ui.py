'''

@author: jrosner
'''

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--vcf',
                    required=True,
                    help='input vcf file')
parser.add_argument('--output',
                    required = True,
                    help = 'output vcf file')
parser.add_argument('--db',
                    required = True,
                    help = 'mutation assessor db directory')
args, unknown = parser.parse_known_args()
