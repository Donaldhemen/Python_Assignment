from movie_functions import movie_functions


movies = []


def display_menu():

    print("\n MOVIE RATING SYSTEM ")
    print("1. Add a Movie")
    print("2. Rate a Movie")
    print("3. View Average Ratings")
    print("4. Exit")


def get_menu_choice():

    while True:

        choice = int(input("Enter your choice: "))

        if 1 <= choice <= 4:
            return choice

        print("Please enter a number between 1 and 4.")


def find_movie(movie_name):

    for movie in movies:

        if movie.get_movie_name().lower() == movie_name.lower():
            return movie

    return None


def add_movie():

    movie_name = input("Enter movie name: ").strip()

    if movie_name == "":
        print("Movie name cannot be empty.")
        return

    if find_movie(movie_name) is not None:
        print("Movie already exists.")
        return

    movie = MovieFunctions(movie_name)

    movies.append(movie)

    print(f"Movie '{movie_name}' added successfully!")
    print(f"Date added: {movie.get_date_added()}")


def rate_movie():

    movie_name = input("Enter movie name: ").strip()

    movie = find_movie(movie_name)

    if movie is None:
        print("Movie not found.")
        return

    while True:

        try:
            rating = int(input("Enter rating (1-5): "))

            if 1 <= rating <= 5:
                break

            print("Rating must be between 1 and 5.")

        except ValueError:
            print("Invalid rating. Please enter a number.")

    movie.add_rating(rating)

    print(f"Rating {rating} added to '{movie.get_movie_name()}'.")


def view_average_ratings():

    if len(movies) == 0:
        print("No movies have been added yet.")
        return

    print("\n AVERAGE RATINGS ")

    for movie in movies:

        average = movie.get_average_rating()

        print(f"{movie.get_movie_name()}: {average:.2f}")


def main():

    running = True

    while running:

        display_menu()

        choice = get_menu_choice()

        if choice == 1:
            add_movie()

        elif choice == 2:
            rate_movie()

        elif choice == 3:
            view_average_ratings()

        elif choice == 4:
            running = False
            print("Goodbye!")


if __name__ == "__main__":
    main()
