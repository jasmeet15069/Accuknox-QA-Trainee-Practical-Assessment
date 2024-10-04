import requests
import logging

logging.basicConfig(filename='application_health.log', level=logging.INFO)

def check_application_health(api_url, url):
    try:
        response = requests.get(api_url, params={'url': url}, timeout=10)
        if response.status_code == 200:
            result = response.json()
            logging.info(f'Application is up and running: {url}')
            return result
        else:
            logging.warning(f'Application is down or not responding: {url} - Status Code: {response.status_code}')
            return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f'Error checking application health: {e}')
        return {"status": "error", "message": str(e)}

def main():
    api_url = 'http://localhost:3000/check_health'
    url = 'http://example.com'
    result = check_application_health(api_url, url)
    print(result)

if __name__ == '__main__':
    main()
