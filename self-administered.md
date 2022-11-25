The Python script `self_administered.py` may be used to generate a fully
self-administered 64-bit CreatorID:CreationID pair for use in the CreationID
system, without the requirement to register the ID.

Simply run the script in a terminal and collect your unique ID.

This approach is suggested for individuals making one-off designs. If you plan
to release multiple designs, you should still allocate a unique CreatorID and
then allocate CreationIDs as needed in any way you see fit.

It is NOT permitted to generate multiple UUIDs until desirable sub-strings
appear in the resulting CreationID. If you want to have cute messages made out
of hex digits in your product's identifier, then allocate a CreatorID.

Statistically, around 1.5 million IDs may be allocated in this fashion before
the chance of any collision exceeds one-in-a-million. If this is not acceptable
for your use-case, then allocate a CreatorID.
