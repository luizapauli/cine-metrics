from services.tmdb_client import TMDBClient
from services.database import DatabaseClient

def menu():

    print("\n--- C | I | N | E  ||  M | E | T | R | I | C | S ---")
    print("----------------------------------------------------\n")
    print("1 - Insert new series\n")
    print("2 - View all series saved\n")
    print("3 - Delete a series\n")
    print("4 - View statistics\n")
    print("0 - Exit\n")

    choice = input("Choose an option: ")
    try:
        return int(choice)
    except ValueError:
        return -1


def main():
    # 1. Instance client and database (loads the API by itself)
    try:
        client = TMDBClient()
        db_client = DatabaseClient()
    except ValueError as e:
        print(e)
        return
    
    db_client.init_db()

    op = None
    while op != 0:
        op = menu()
        match op:
            case 0:
                print("Exiting...")
                break
            case 1:
                # 1. User input
                name_series = input("Type a series name: ")

                print(f"\n🔎 Searching for '{name_series}' in TMDB...")
                
                # 2. Calls the method
                result = client.search_tv_show(name_series)

                # 3. Shows result
                if result:
                    db_client.add_series(result)
                    print(f"\n✅ SUCCESS! Series found:")
                    print(f"Original Name: {result['original_name']}")
                    print(f"ID: {result['id']}")
                    print(f"Average rating: {result['vote_average']}")
                    print("-" * 30)
                    print(f"Synopsis: {result['overview']}")
                else:
                    print("\n❌ Series not found (or connection error).")

            case 2:
                print("--- M | Y  ||  C | O | L | L | E | C | T | I | O | N ---\n")
                print("--------------------------------------------------------\n")

                series = db_client.get_all_series()
                for s in series:
                    print(f"📺 {s[1]} - Average rating: {s[2]}")
            
            case 3:
                print("--- D | E | L | E | T | E  ||  S | E | R | I | E | S ---\n")
                print("--------------------------------------------------------\n")

                series = db_client.get_all_series()
                for s in series:
                    print(f"{s[0]} 📺 {s[1]} - Average rating: {s[2]}")

                try:
                    series_id = int(input("\nType the ID of the series to delete: "))
                    db_client.delete_series(series_id)
                except ValueError:
                    print("Invalid ID.")

            case 4:
                print("--- S | T | A | T | I | S | T | I | C | S ---\n")
                print("------------------------------------------------\n")

                avg_rating = db_client
                if avg_rating := db_client.get_average_rating():
                    print(f"⭐ Average rating of all series: {avg_rating:.2f}")
                else:
                    print("No series found in the database.")
                
            case _:
                print("Invalid option. Please try again.\n")
                continue

"""
    print("--- CineMetrics: Connection Test ---")
    
    # 2. User input
    name_series = input("Type a series name to test it: ")

    print(f"\n🔎 Searching for '{name_series}' in TMDB...")
    
    # 3. Calls the method
    result = client.search_tv_show(name_series)

    # 4. Shows result
    if result:
        db_client.add_series(result)
        print(f"\n✅ SUCCESS! Series found:")
        print(f"Original Name: {result['original_name']}")
        print(f"ID: {result['id']}")
        print(f"Average rating: {result['vote_average']}")
        print("-" * 30)
        print(f"Synopsis: {result['overview']}")
    else:
        print("\n❌ Series not found (or connection error).")

"""

if __name__ == "__main__":
    main()