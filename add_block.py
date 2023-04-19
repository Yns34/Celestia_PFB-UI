import requests
import json
import sys

# Usage: python3 add_block.py --namespace <NAMESPACE> --data <DATA>

args = sys.argv[1:]
namespace = None
data = None

for i in range(len(args)):
    if args[i] == '--namespace' and i < len(args) - 1:
        namespace = args[i+1]
    elif args[i] == '--data' and i < len(args) - 1:
        data = args[i+1]

if not namespace or not data:
    print("Usage: python3 add_block.py --namespace <NAMESPACE> --data <DATA>")
    sys.exit(1)

# create the payload
payload = {
    "namespace": namespace,
    "data": data
}

# make the POST request
url = "http://localhost:8000/add_block"
response = requests.post(url, data=json.dumps(payload))

# print the response
print(response.text)

