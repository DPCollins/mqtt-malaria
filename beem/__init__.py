# Copyright (c) 2013, ReMake Electric ehf
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
"""
Bits and pieces of malaria code that aren't needed anywhere else
"""
import time

def TimeTrackingPayloadGenerator(cid, sequence_size):
    """
    Message generator creating payloads with timestamps
    to help determine total flight time.
    """
    num = 0
    while num < sequence_size:
        topic = "mqtt-malaria/%s/data/%d" % (cid, num)
        payload = '{:f}'.format(time.time())
        yield (num, topic, payload)
        num = num + 1

def PayloadGeneratorGaussianSize(cid, sequence_size, target_size):
    """
    Message generator creating gaussian distributed message sizes
    centered around target_size with a deviance of target_size / 20
    """
    num = 0
    while num < sequence_size:
        topic = "mqtt-malaria/%s/data/%d" % (cid, num)
        real_size = int(random.gauss(msg_size, msg_size / 20))
        payload = ''.join(random.choice(string.hexdigits) for x in range(real_size))
        yield (num, topic, payload)
        num = num + 1

