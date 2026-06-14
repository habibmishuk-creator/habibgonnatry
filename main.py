import process
import tui
import visual


DATA_FILE = "Disneyland_reviews.csv"


def main():
    tui.display_title()

    reviews = process.read_csv_file(DATA_FILE)
    tui.display_dataset_loaded(len(reviews))

    while True:
        choice = tui.display_main_menu()

        if choice == "A":
            handle_view_data(reviews)

        elif choice == "B":
            handle_visual_data(reviews)

        elif choice == "X":
            print("Thank you for using the program.")
            break

        else:
            print("Invalid menu choice.")


def handle_view_data(reviews):
    choice = tui.display_view_menu()

    if choice == "A":
        park = input("Enter park name: ")
        park_reviews = process.get_reviews_by_park(reviews, park)
        tui.display_reviews(park_reviews)

    elif choice == "B":
        park = input("Enter park name: ")
        location = input("Enter reviewer location: ")
        count = process.count_reviews_by_park_and_location(
            reviews, park, location
        )
        print(f"{park} has {count} reviews from {location}.")

    elif choice == "C":
        park = input("Enter park name: ")
        year = input("Enter year: ")
        average = process.average_rating_by_park_and_year(
            reviews, park, year
        )

        if average == 0:
            print("No matching reviews found.")
        else:
            print(f"Average rating for {park} in {year}: {average:.2f}")

    elif choice == "D":
        averages = process.average_score_per_park_by_location(reviews)
        tui.display_average_scores(averages)

    else:
        print("Invalid menu choice.")


def handle_visual_data(reviews):
    choice = tui.display_visual_menu()

    if choice == "A":
        data = process.review_counts_by_park(reviews)
        visual.show_reviews_by_park_pie(data)

    elif choice == "B":
        park = input("Enter park name: ")
        data = process.top_locations_by_average_rating(reviews, park)
        visual.show_top_locations_bar(data, park)

    elif choice == "C":
        park = input("Enter park name: ")
        data = process.average_rating_by_month(reviews, park)
        visual.show_monthly_average_bar(data, park)

    else:
        print("Invalid menu choice.")


if __name__ == "__main__":
    main()