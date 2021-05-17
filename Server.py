# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:14:46 2021

@author: devanshi
"""

import Pyro4
from Operation import Op

class Server:
    obj=Op()
    with Pyro4.Daemon() as daemon:
        uri = daemon.register(obj)
        with Pyro4.locateNS() as ns:
            ns.register("URI", uri)
            daemon.requestLoop()
    