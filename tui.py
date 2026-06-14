def display_title():
    print("=" * 60)
    print("DISNEYLAND REVIEW ANALYSER")
    print("=" * 60)


def display_dataset_loaded(number_of_rows):
    print("\nDataset loaded successfully.")
    print(f"Number of rows loaded: {number_of_rows}")


def display_main_menu():
    print("\nPlease enter one of the following options:")
    print("[A] View Data")
    print("[B] Visualise Data")
    print("[X] Exit")

    choice = input("Enter your choice: ").upper()
    print(f"You selected: {choice}")
    return choice


def display_view_menu():
    print("\nPlease enter one of the following options:")
    print("[A] View Reviews by Park")
    print("[B] Number of Reviews by Park and Reviewer Location")
    print("[C] Average Rating by Park and Year")
    print("[D] Average Score per Park by Reviewer Location")

    return input("Enter your choice: ").upper()


def display_visual_menu():
    print("\nPlease enter one of the following options:")
    print("[A] Most Reviewed Parks")
    print("[B] Park Ranking by Nationality")
    print("[C] Most Popular Month by Park")

    return input("Enter your choice: ").upper()


def display_reviews(reviews):
    if len(reviews) == 0:
        print("No reviews found.")
        return

    for review in reviews:
        print("-" * 60)
        print(f"Review ID: {review['Review_ID']}")
        print(f"Rating: {review['Rating']}")
        print(f"Year Month: {review['Year_Month']}")
        print(f"Reviewer Location: {review['Reviewer_Location']}")
        print(f"Branch: {review['Branch']}")


def display_average_scores(averages):
    for park, locations in averages.items():
        print("\n" + "=" * 60)
        print(park)
        print("=" * 60)

        for location, average in locations.items():
            print(f"{location}: {average:.2f}")
