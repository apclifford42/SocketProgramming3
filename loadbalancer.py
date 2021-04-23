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
    parser.add_argument('-s', type=int, required=True, help='server ip')
    parser.add_argument('-p', type=str, required=True, help='Port')
    parser.add_argument('-l', type=str, required=True, help='logfile')
    args = parser.parse_args()
    
    serverIP = args.s
    port = args.p
    logfile = args.w
    return server_port, log_file, web_address