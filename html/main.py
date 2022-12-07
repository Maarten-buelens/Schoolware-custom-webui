import argparse
from python.get_punten import *
from python.get_data import *
from python.get_agenda import *

parser = argparse.ArgumentParser(description='Optional app description')

parser.add_argument('--taken', action='store_true',
                    help='do taken')

parser.add_argument('--punten', action='store_true',
                    help='do punten')

parser.add_argument('--agenda', action='store_true',
                    help='do agenda')

args = parser.parse_args()

if(args.taken and not args.punten and not args.agenda):
    taken()

elif(not args.taken and args.punten and not args.agenda):
    punten()

elif(not args.taken and not args.punten and args.agenda):
    agenda()