"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* This program is free software: you can redistribute it and/or modify
* it under the terms of the GNU Lesser General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
"""

import zlib

from podrum.network.PacketPool import PacketPool
from podrum.network.protocol.DataPacket import DataPacket
from podrum.network.protocol.ProtocolInfo import ProtocolInfo

class BatchPacket(DataPacket):
    NID = ProtocolInfo.BATCH_PACKET
    
    payload = ""
    compressionLevel = 7
    
    def canBeBatched():
        return False
    
    def canBeSentBeforeLogin():
        return True
    
    def decodeHeader(self):
        pid = self.getByte()
        assert pid == self.NID
        
    def decodePayload(self):
        data = self.getRemaining()
        try:
            self.payload = zlib.decompress(data, 1024 * 1024 * 2)
        except:
            self.payload = ""
            