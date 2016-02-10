-e import sys
import os

if not os.environ.get('AFFECTED_ONLY'):
	sys.exit(1)
