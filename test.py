#!/usr/bin/env python

import sys
import os

if os.environ.get('AFFECTED_ONLY') == 'true':
	sys.exit(1)
