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
import subprocess

def get_args(argv=None):
    '''read the arguments from command line and return the values'''
    parser = argparse.ArgumentParser(description="LIGHTSERVER")
    parser.add_argument('-s', type=str, required=True, help='server ip')
    parser.add_argument('-p', type=str, required=True, help='Port')
    parser.add_argument('-l', type=str, required=True, help='logfile')
    args = parser.parse_args()
    
    serverIPtxt = args.s
    port = args.p
    logfile = args.l
    serverIP = 0
    #This takes the text file pulled in with -s and converts all lines (ip addresses, hopefully) in the file to an array holding all the ip addresses.
    with open(serverIPtxt) as f:
        serverIP = f.read().splitlines()

    #should return an array, port#, and logfile name
    return serverIP, port, logfile


def ping(host):
    result = subprocess.run(["ping", host, "-c 3"], capture_output=True, text=True)
    output = result.stdout
    output_string = output.split()
    #assigned to variables to save my ctrlv finger
    loss = output_string[-10].replace('%', '')
    print("Loss = ", loss, "%")
    
    delay = output_string[-2].split('/')[1]
    print("Delay = ", delay)

    #we bundle the performance metric with the loss and delay in one array
    metric = [host, int(loss), float(delay)] 
    return metric

#this function will take the mega list of server ips and return an array of arrays. Each array contain the server ip, the loss, and the delay.
def allping(ips):
    #counter variable
    counter = 0
    #instantiating array to return
    metric = [0] * len(ips)
    #iterating through each ip in the list and using ping(ip) on them
    for ip in ips:
        metric[counter] = ping(ip)
        counter = counter + 1

    #returns the big ol' array
    return metric