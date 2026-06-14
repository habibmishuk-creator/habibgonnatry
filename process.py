import csv
from calendar import month_name


def read_csv_file(filename):
    reviews = []

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            reviews.append(row)

    return reviews


def get_reviews_by_park(data, park):
    results = []

    for review in data:
        if review["Branch"].lower() == park.lower():
            results.append(review)

    return results


def count_reviews_by_park_and_location(data, park, location):
    count = 0

    for review in data:
        same_park = review["Branch"].lower() == park.lower()
        same_location = (
            review["Reviewer_Location"].lower() == location.lower()
        )

        if same_park and same_location:
            count += 1

    return count


def average_rating_by_park_and_year(data, park, year):
    ratings = []

    for review in data:
        same_park = review["Branch"].lower() == park.lower()
        same_year = review["Year_Month"].startswith(year)

        if same_park and same_year:
            ratings.append(int(review["Rating"]))

    if len(ratings) == 0:
        return 0

    return sum(ratings) / len(ratings)


def review_counts_by_park(data):
    counts = {}

    for review in data:
        park = review["Branch"]

        if park not in counts:
            counts[park] = 0

        counts[park] += 1

    return counts


def top_locations_by_average_rating(data, park):
    location_ratings = {}

    for review in data:
        if review["Branch"].lower() == park.lower():
            location = review["Reviewer_Location"]
            rating = int(review["Rating"])

            if location not in location_ratings:
                location_ratings[location] = []

            location_ratings[location].append(rating)

    averages = {}

    for location, ratings in location_ratings.items():
        averages[location] = sum(ratings) / len(ratings)

    sorted_averages = sorted(
        averages.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return dict(sorted_averages[:10])


def average_rating_by_month(data, park):
    month_ratings = {}

    for number in range(1, 13):
        month_ratings[number] = []

    for review in data:
        if review["Branch"].lower() == park.lower():
            year_month = review["Year_Month"]

            if "-" in year_month:
                month_number = int(year_month.split("-")[1])
                month_ratings[month_number].append(int(review["Rating"]))

    averages = {}

    for number, ratings in month_ratings.items():
        month = month_name[number]

        if len(ratings) == 0:
            averages[month] = 0
        else:
            averages[month] = sum(ratings) / len(ratings)

    return averages


def average_score_per_park_by_location(data):
    results = {}

    for review in data:
        park = review["Branch"]
        location = review["Reviewer_Location"]
        rating = int(review["Rating"])

        if park not in results:
            results[park] = {}

        if location not in results[park]:
            results[park][location] = []

        results[park][location].append(rating)

    averages = {}

    for park, locations in results.items():
        averages[park] = {}

        for location, ratings in locations.items():
            averages[park][location] = sum(ratings) / len(ratings)

    return averages