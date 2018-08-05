import requests
import json
import subprocess


def main():
    url = "http://localhost:8080/jsonrpc"
    headers = {'content-type': 'application/json'}

    q = subprocess.run(["fortune", "futurama"], stdout=subprocess.PIPE)
    d = q.stdout.decode("utf-8")
    # Example echo method
    payload = {
        "method": "cowsay",
        "params": {"message": d, "cow": "flaming-sheep", "greedy": True},
        "jsonrpc": "2.0",
        "id": 0,
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()

    for x in response["result"]:
        print(x)

if __name__ == "__main__":
    main()
