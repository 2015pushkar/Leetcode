import hashlib
import json

traits = ["Craftsman", "Pragmatic", "Curious", "Methodical", "Driven", "Collaborator"]
key = "Close-3bd54647".encode("utf-8")

out = [
    hashlib.blake2b(t.encode("utf-8"), key=key, digest_size=64).hexdigest()
    for t in traits
]

print(json.dumps(out))
