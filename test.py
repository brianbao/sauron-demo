import sys
import os

if os.environ.get('AFFECTED_ONLY') == 'false':
	sys.exit(1)
