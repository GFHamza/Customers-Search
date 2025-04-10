import requests
import time
import json


def get_search_results(api_key, query):
    """Fetch all paginated results from Google Places Text Search."""
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {'query': query, 'key': api_key}
    all_results = []

    while True:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()

        if data['status'] != 'OK':
            print(f"API Error: {data['status']}")
            break

        all_results.extend(data.get('results', []))
        next_page_token = data.get('next_page_token')

        if not next_page_token:
            break  # Exit loop if no more pages

        params['pagetoken'] = next_page_token
        time.sleep(2)  # Mandatory delay for next page token

    return all_results


def get_place_details(api_key, place_id):
    """Fetch detailed information for a specific place using its place_id."""
    url = "https://maps.googleapis.com/maps/api/place/details/json"
    params = {
        'place_id': place_id,
        'fields': 'name,formatted_address,geometry,formatted_phone_number,website',
        'key': api_key
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    if data['status'] != 'OK':
        print(f"Details API Error: {data['status']}")
        return None

    return data.get('result', {})


def main():
    api_key = input("Enter your Google Maps API key: ")
    query = input("Enter search query (e.g., 'coffee shops, New York'): ")

    results = get_search_results(api_key, query)
    if not results:
        print("No results found.")
        return

    sites = []
    for result in results:
        place_id = result.get('place_id')
        if not place_id:
            continue  # Skip if no place_id is available

        details = get_place_details(api_key, place_id)
        if not details:
            continue  # Skip if details are not available

        coords = details.get('geometry', {}).get('location', {})
        site_info = {
            'name': details.get('name'),
            'latitude': coords.get('lat'),
            'longitude': coords.get('lng'),
            'address': details.get('formatted_address'),
            'phone': details.get('formatted_phone_number'),
            'website': details.get('website')
        }
        sites.append(site_info)

    # Save results to JSON file
    with open('google_maps_results_with_contacts.json', 'w') as f:
        json.dump(sites, f, indent=2)
    print(f"\nSaved {len(sites)} results to 'google_maps_results_with_contacts.json'")

    # Display results
    print("\nSearch Results with Contacts:")
    for idx, site in enumerate(sites, 1):
        print(f"\nSite {idx}:")
        print(f"Name: {site['name']}")
        print(f"Coordinates: {site['latitude']}, {site['longitude']}")
        print(f"Address: {site['address']}")
        print(f"Phone: {site.get('phone', 'Not available')}")
        print(f"Website: {site.get('website', 'Not available')}")


if __name__ == "__main__":
    main()