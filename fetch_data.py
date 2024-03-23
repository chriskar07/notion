import requests

def fetch_coingecko_data():
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 100,
        'page': 1,
        'sparkline': False
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        print("API Response Status Code:", response.status_code)  # Debug statement
        print("API Response Content:", response.text)  # Debug statement
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print('Error fetching data from CoinGecko API:', e)
        return None

if __name__ == '__main__':
    coingecko_data = fetch_coingecko_data()
    if coingecko_data:
        print('Data fetched successfully:', coingecko_data)
    else:
        print('Failed to fetch data from CoinGecko API')
print("Script execution started...")
