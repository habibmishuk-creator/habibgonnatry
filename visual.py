import matplotlib.pyplot as plt


def show_reviews_by_park_pie(data):
    labels = list(data.keys())
    values = list(data.values())

    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=labels, autopct="%1.1f%%")
    plt.title("Number of Reviews per Disneyland Park")
    plt.show()


def show_top_locations_bar(data, park):
    if len(data) == 0:
        print("No data found for this park.")
        return

    labels = list(data.keys())
    values = list(data.values())

    plt.figure(figsize=(10, 6))
    plt.bar(labels, values)
    plt.title(f"Top 10 Locations by Average Rating for {park}")
    plt.xlabel("Reviewer Location")
    plt.ylabel("Average Rating")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def show_monthly_average_bar(data, park):
    labels = list(data.keys())
    values = list(data.values())

    plt.figure(figsize=(10, 6))
    plt.bar(labels, values)
    plt.title(f"Average Rating by Month for {park}")
    plt.xlabel("Month")
    plt.ylabel("Average Rating")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()