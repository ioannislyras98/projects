import requests
import time

def make_http_call(url):
    try:
        response = requests.post(url)
        if response.status_code == 200:
            print(f"Success: {response.status_code}")
        else:
            print(f"Failed: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    url = "https://prod-08.westeurope.logic.azure.com:443/workflows/8b2525a5edbd46b1842bd7c8c3f55559/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=18EZc-BcI6uoWiNDN3MvFZQKizNETD470aoOYhU6Tuw"  # Replace with your target URL
    interval = 3 * 60  # 3 minutes in seconds
    repetitions = 80

    for i in range(repetitions):
        print(f"Making HTTP call {i + 1} of {repetitions}")
        make_http_call(url)
        if i < repetitions - 1:  # Avoid sleeping after the last call
            time.sleep(interval)

if __name__ == "__main__":
    main()