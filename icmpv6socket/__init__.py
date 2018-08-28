
import socket
from typing import Optional, List


__version__ = '0.1.0'


class ICMPv6Socket(socket.socket):

    # From https://elixir.bootlin.com/linux/v4.18/source/include/linux/socket.h#L312
    SOL_ICMPV6 = 58  # type: int
    # From https://elixir.bootlin.com/linux/v4.18/source/include/uapi/linux/icmpv6.h#L139
    ICMPV6_FILTER = 1  # type: int

    # From ... yeah, not in the Linux kernel header files?!
    ICMPV6_ROUTER_SOL = 133  # type: int
    ICMPV6_ROUTER_ADV = 134  # type: int

    def __init__(self, message_types: Optional[List[int]] = None) \
            -> None:
        """Initializes an ICMPv6 socket. There isn't much argument here,
        it seems, unless you want to receive only certain ICMPv6 message
        types.

        :arg message_types: optional list of ICMPv6 message types (int).
          Defaults to None.
        """
        super(ICMPv6Socket, self).__init__(socket.AF_INET6,
                                           socket.SOCK_RAW,
                                           socket.IPPROTO_ICMPV6)
        self._filter_mask = bytearray(b'\x00' * 32)  # type: bytes
        self.accept_type(message_types)

    def accept_type(self, message_types: List[int]):
        # Please note that with the ICMPv6 filtering socket option
        # a "1" actually means to filter out(!), while "0" means to
        # let it pass to the socket. Crooked logic.
        self._filter_mask = bytearray(b'\xff' * 32)
        for msg_type in message_types:
            self._filter_mask[msg_type >> 3] &= ~(1 << (msg_type & 7))
        self.setsockopt(self.SOL_ICMPV6, self.ICMPV6_FILTER,
                        self._filter_mask)

