import nacl.encoding
import nacl.signing

# Generate a new key-pair for Bob
bobs_private_key = nacl.signing.SigningKey.generate()
bobs_public_key = bobs_private_key.verify_key

# Since it's bytes, we'll need to serialize the key to a readable format before publishing it:
bobs_public_key_hex = bobs_public_key.encode(encoder=nacl.encoding.HexEncoder)

# Now, let's sign a message with it
signed = bobs_private_key.sign(b"Send $37 to Alice")

print(bobs_public_key_hex)
print(signed)