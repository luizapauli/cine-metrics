from services.tmdb_client import TMDBClient

def main():
    # 1. Instance client (loads the API by itself)
    try:
        client = TMDBClient()
    except ValueError as e:
        print(e)
        return

    print("--- CineMetrics: Connection Test ---")
    
    # 2. User input
    name_series = input("Type a series name to test it: ")

    print(f"\n🔎 Searching for '{name_series}' in TMDB...")
    
    # 3. Calls the method
    result = client.search_tv_show(name_series)

    # 4. Shows result
    if result:
        print(f"\n✅ SUCCESS! Series found:")
        print(f"Original Name: {result['original_name']}")
        print(f"ID: {result['id']}")
        print(f"Average rating: {result['vote_average']}")
        print("-" * 30)
        print(f"Synopsis: {result['overview']}")
    else:
        print("\n❌ Series not found (or connection error).")

if __name__ == "__main__":
    main()