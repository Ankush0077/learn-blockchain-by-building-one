from hashlib import sha256

message = "Hello Bob, Let's meet at the Kruger National Park on 2020-12-12 at 1pm."
hash_message = sha256(("p@55w0rd" + message).encode()).hexdigest()

from hashlib import sha256
alices_message = "Hello Bob, Let's meet at the Kruger National Park on 2020-12-12 at 1pm."
alices_hash = "39aae6ffdb3c0ac1c1cc0f50bf08871a729052cf1133c4c9b44a5bab8fb66211"
hash_message = sha256(("p@55w0rd" + alices_message).encode()).hexdigest()

if hash_message == alices_hash:
    print("Message has not been tampered with")