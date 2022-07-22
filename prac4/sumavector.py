#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2022 LJ.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy
import math
from gnuradio import gr

class sumavector(gr.sync_block):
    """
    docstring for block sum_vector
    """
    def __init__(self, PARAM1):
        self.PARAM1 = PARAM1
        gr.sync_block.__init__(self,
            name="sumavector",
            in_sig=[(numpy.float32,int(self.PARAM1))],
            out_sig=[numpy.float32, ])


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        for i in range(len(in0)):
                out[i] = math.fsum(in0[i,:])
        return len(output_items[0])
