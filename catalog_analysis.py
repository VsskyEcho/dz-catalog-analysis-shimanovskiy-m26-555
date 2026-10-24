import math

movies = [
{"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
 "rating": 8.6, "duration_min": 155,
 "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
{"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
 "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
{"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
 "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
{"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
 "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
{"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
 "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
{"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
 "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
{"title": "Garden of Static", "year": 2022, "genres": {"drama"},
 "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
{"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
 "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
{"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
 "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
{"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
 "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

# Этап 1
def average_rating(movies):
    if not movies:
        return 0
    total_rating = sum(movie['rating'] for movie in movies)
    return round(total_rating / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    if not movies:
        return (None, None, None)
    ages = [current_year - movie['year'] for movie in movies]
    oldest = max(ages)
    newest = min(ages)
    average = math.ceil(sum(ages) / len(ages))
    return (oldest, newest, average)


def duration_in_hours(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return f'{hours}ч {remaining_minutes}м'


# Этап 2
def rating_tier(rating):
    if rating >= 9:
        return 'шедевр'
    elif rating >= 7:
        return 'хорошо'
    else:
        return 'средне' if rating >= 5 else 'слабо'

def decade_label(year):
    match year:
        case _ if year > 2020:
            return 'новые'
        case _ if 2015 <= year <= 2020:
            return 'недавние'
        case _:
            return 'старые'


# Этап 3
def non_comedy_movies(movies):
    print("Фильмы, которые НЕ относятся к жанру 'comedy':")
    for movie in movies:
        if 'comedy' in movie['genres']:
            continue
        print(f"- {movie['title']}")


def find_first_masterpiece(movies):
    print("\nПоиск первого шедевра (> 9.0):")
    index = 0
    while index < len(movies):
        movie = movies[index]
        if movie["rating"] > 9.0:
            print(f"Найден шедевр: {movie['title']} (Рейтинг: {movie['rating']})")
            break
        index += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    count = 0 
    for movie in movies:
        if movie['duration_min'] > threshold:
            count += 1
    return count


# Этап 4. Строки
def normalize_title(title):
    words = title.split()
    normalized_words = []

    for word in words:
        normalized_words.append(word[0].upper() + word[1:])
    return ' '.join(normalized_words)


def make_slug(title):
    return title.lower().replace(' ', '-')


def format_report_line(movie):
    title = normalize_title(movie['title'])
    sorted_genres = sorted(movie['genres'])
    readable_duration = duration_in_hours(movie['duration_min'])
    return (f'"{title}" ({movie['year']}) — {movie['rating']}/10, '
            f'{readable_duration}, жанры: {", ".join(sorted_genres)}'
    )


# Этап 5. Списки
def titles_sorted_by_rating(movies):
    sorted_movies = sorted(movies, key=lambda a: a['rating'], reverse=True)
    titles = []

    for movie in sorted_movies:
        titles.append(movie['title'])
    return titles


def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(movies, key=lambda a: a['rating'], reverse =True)
    top_list = []

    for movie in sorted_movies:
        top_list.append((movie['title'], movie['rating']))
    return top_list[:n]


# Этап 6. Словари
def count_by_genre(movies):
    genre_counts = {}

    for movie in movies:
        for genre in movie['genres']:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1
    return genre_counts


def actor_filmography(movies):
    filmography = {}

    for movie in movies:
        for actor in movie['actors']:
            current_movies = filmography.get(actor, [])
            current_movies.append(movie['title'])
            filmography[actor] = current_movies
    return filmography


def above_average_ratings(movies):
    avg = average_rating(movies)

    return {m['title']: m['rating'] for m in movies if m['rating'] > avg}


# Этап 7. Множества
def all_genres(movies):
    genres_set = set()
    for movie in movies:
        genres_set.update(movie['genres'])
    return genres_set

def common_actors(movie1, movie2):
    actors1 = set(movie1['actors'])
    actors2 = set(movie2['actors'])
    return actors1 & actors2

def genres_only_in_one(movies_a, movies_b):
    genres_a = all_genres(movies_a)
    genres_b = all_genres(movies_b)
    return genres_a - genres_b


# Этап 8. Итераторы и генераторы
def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie['rating'] >= min_rating:
            yield movie

# Напишите генераторное выражение, которое считает суммарную длительность всех фильмов
# с рейтингом выше 7 в минутах, и передайте его в sum()
def total_duration(movies, rating=7):
    return sum(movie['duration_min'] for movie in movies if movie['rating'] > rating)


#Этап 9. Итоговый отчет
def build_report(movies):
    avg_rating = average_rating(movies)
    _, _, avg_age = catalog_age_stats(movies)

    print('ОТЧЕТ ПО КАТАЛОГУ')
    print(f'Средний рейтинг: {avg_rating}')
    print(f'Средний возраст фильмов: {avg_age} лет')

    print('\nТоп-3 фильма:')
    movies_by_title = {m['title']: m for m in movies}
    for title, _ in top_n_by_rating(movies, 3):
        print(f'  {format_report_line(movies_by_title[title])}')

    print('\nФильмы по жанрам:')
    genre_counts = count_by_genre(movies)
    sorted_counts = sorted(genre_counts.items(), key=lambda item: (-item[1], item[0]))
    for genre, count in sorted_counts:
        print(f'  {genre} — {count}')

    print(f'\nВсе жанры каталога: {', '.join(sorted(all_genres(movies)))}')

if __name__ == "__main__":
    # В этапе 3 просили вывести все фильмы, которые не относятся к жанру "comedy",
    non_comedy_movies(movies)
    
    # В этапе 8 просили продемонстрироватьт работу циклом for с вызовом format_report_line
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))
    
    # Этап 9: Итоговый отчет
    print()
    build_report(movies)