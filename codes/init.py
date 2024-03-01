import pygame as pg
import warnings
import json
import os
import tqdm.rich as tr
import time
#This files is used to intialize only
#No actual function
pg.init()
config_exist=0
config_path="./settings/config.json"
W_width=0
W_height=0
caption="Pending"
if os.path.exists(config_path):
    if os.access(config_path,os.R_OK):
        config_exist=1
if config_exist==0:
    warnings.warn("config.json can not be read,loading defaults...")
    for i in tr.trange(100):
        time.sleep(0.01)#absolutely weird, this progress bar indicates nothing
        W_width=720
        W_height=480
    time.sleep(1)
#config detection
else:
    print("Loading config from config.json...")
    config={}
    with open(config_path,'r') as config_reader:#read configs
        config=json.load(config_reader)
    for i in tr.trange(100):
        time.sleep(0.01)#absolutely weird, this progress bar indicates nothing
    time.sleep(1)
    print("config.json loaded as",config)
    W_width=config["resolution_horizontal"]
    W_height=config["resolution_vertical"]#load configs
    caption=config["caption"]
screen=pg.display.set_mode([W_width,W_height])
pg.display.set_caption(caption)#initializing window
