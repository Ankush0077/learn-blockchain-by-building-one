import nacl.encoding
import nacl.signing


# From the above example...
bobs_public_key = b'1a503b386ee6198d3b3d3e9d3a44e66b465fcb4c8140e3684d27f8247b45be6e'

# We generate the verify_key
verify_key = nacl.signing.VerifyKey(bobs_public_key,
encoder=nacl.encoding.HexEncoder)
1
signed_message = b'\x9d\xb5/\x95\x0c5L\xa6\x0c\xd0\x80\x9fm\xec\x1d\xc3\x0c\xa0v\xf2\x03\x94\xd0\xbe\x94\x15\x8a\x9aH}wV\xdag\x89\xe1\xc2d\x91\xc3\x14\x82\x8b\xad\xba\x7f{\xf6\xa7\xe2n\x93\xdeQm\x9bP\xed\xd7\xb1M#6\x04Send $37 to Alice'

# Now we attempt to verify the message
# Any invalidation will result in an Exception being thrown
verify_key.verify(signed_message)
print("Verification Successful!!!")