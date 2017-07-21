#!/usr/bin/env python3

import crozono
import src.settings as settings
import sys

def main():
    essids = ['completar']
    for essid in essids:
        print(essid)
        settings.TARGET_ESSID = essid
        try:
            crozono.main()
        except:
            print('fin')  

main()
