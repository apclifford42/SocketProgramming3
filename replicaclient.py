import socket
import struct
import argparse
import logging
import sys
import random

def get_args(argv=None):
    '''read the arguments from command line and return the values'''
    parser = argparse.ArgumentParser(description="LIGHTCLIENT")
    parser.add_argument('-s', type=str, required=True, help='Load Balancer IP')
    parser.add_argument('-p', type=int, required=True, help='Port')
    parser.add_argument('-l', type=str, required=True, help='logFile')
    parser.add_argument('-f', type=str, required=True, help='File to write to')
    args = parser.parse_args()
    loadBalancer = args.s
    server_port = args.p
    log_file = args.l    
    dest_file = args.f
    return loadBalancer, server_port, log_file, dest_file



# this class makes me want to die