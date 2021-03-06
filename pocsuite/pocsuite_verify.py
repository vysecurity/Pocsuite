#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014-2015 pocsuite developers (http://seebug.org)
See the file 'docs/COPYING' for copying permission
"""

import sys
from pocsuite_cli import pcsInit
from .lib.core.settings import PCS_OPTIONS
from .lib.core.common import banner
from .lib.core.common import dataToStdout


def main():
    try:
        pocFile, targetUrl = sys.argv[1: 3]
    except ValueError:
        excMsg = "usage: pcs-verify [pocfile] [url]\n"
        excMsg += "pocsuite: error: too few arguments"
        dataToStdout(excMsg)
        sys.exit(1)

    PCS_OPTIONS.update({'url': targetUrl, 'pocFile': pocFile, 'headers': None, 'extra_params': None})
    pcsInit(PCS_OPTIONS)
    banner()

if __name__ == "__main__":
    main()
