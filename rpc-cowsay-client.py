import requests
import json
import subprocess


def main():
    url = "http://0.0.0.0:3031/api/cowsay"
    headers = {'content-type': 'application/json'}

    q = subprocess.run(["fortune"], stdout=subprocess.PIPE)
    d = q.stdout.decode("utf-8")
    payload = {"m": d, "b":True}

    response = requests.post(
            url, data=json.dumps(payload), headers=headers).json()

    for x in response["message"]:
        print(x)

if __name__ == "__main__":
    main()
