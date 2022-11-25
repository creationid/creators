#!/usr/bin/env python3
import uuid

NS = uuid.uuid5(uuid.NAMESPACE_DNS, "https://github.com/creationid")

def uuid_to_creationid(u):
    """Perform a non-reversible conversion from UUID to CreationID

    This may be used to generate a fully self-administered 64-bit
    CreatorID:CreationID pair for use in the CreationID system,
    without the requirement to register the ID.

    This approach is suggested for people making one-off designs. If you
    plan to release multiple designs, you should still allocate a unique
    CreatorID and then allocate CreationIDs as needed in any way you see fit.

    Over 1.5 million IDs may be allocated in this fashion before the chance of
    any collision exceeds one in a million.

    It is NOT permitted to generate multiple UUIDs until desirable sub-strings
    appear in the resulting CreationID. If you want to have cute messages made
    out of hex digits in your product's identifier, then allocate a CreatorID.
    """

    u = uuid.uuid5(NS, u.hex)
    h = f"{u.time:015X}"
    return f"0xF{h[0:3]}_{h[3:7]}:0x{h[7:11]}_{h[11:]}"

def self_administered_creationid():
    return uuid_to_creationid(uuid.uuid4())

if __name__ == '__main__':
    print(self_administered_creationid())
