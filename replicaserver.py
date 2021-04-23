import argparse
import socket
import struct
import threading
import sys
import logging
import time
import random
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
ENCODING = 'utf-8'

def get_args(argv=None):
    '''read the arguments from command line and return the values'''
    parser = argparse.ArgumentParser(description="LIGHTSERVER")
    parser.add_argument('-p', type=int, required=True, help='Port')
    parser.add_argument('-s', type=str, required=True, help='logFile')
    parser.add_argument('-w', type=str, required=True, help='webserver')
    args = parser.parse_args()
    
    log_file = args.s
    server_port = args.p
    web_address = args.w
    return server_port, log_file, web_address