movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
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

import math

# Этап 1
def average_rating(movies):
    if not movies:
        return 0
    total_rating = sum(movie['rating'] for movie in movies)
    return round(total_rating / len(movies), 1)

#print(average_rating(movies))

def catalog_age_stats(movies, current_year=2026):
    if not movies:
        return (None, None, None)
    ages = [current_year - movie['year'] for movie in movies]
    oldest = max(ages)
    newest = min(ages)
    average_age = math.ceil(sum(ages) / len(ages))
    return (oldest, newest, average_age)

#print(catalog_age_stats(movies))

def duration_in_hours(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return f'{hours}ч {remaining_minutes}м'

#print(duration_in_hours(155))

# Этап 2
def rating_tier(rating):
    if rating >= 9:
        return 'шедевр'
    elif rating >= 7:
        return 'хорошо'
    else:
        return 'средне' if rating >= 5 else 'слабо'

#rating_tier(6.4)

def decade_label(year):
    match year:
        case _ if year > 2020:
            return 'новые'
        case _ if 2015 <= year <= 2020:
            return 'недавние'
        case _:
            return 'старые'

#print(decade_label(2018))

# Этап 3

def non_comedy_movies(movies):
    #non_comedy_list = []
    print("Фильмы, которые НЕ относятся к жанру 'comedy':")
    for movie in movies:
        if 'comedy' in movie['genres']:
            continue
        print(f"- {movie['title']}")

#print(non_comedy_movies(movies))

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

#find_first_masterpiece(movies)

def count_long_movies(movies, threshold=120):
    count = 0 
    for movie in movies:
        if movie['duration_min'] > threshold:
            count += 1
    return count

#long_movies_count = count_long_movies(movies, threshold=120)
#print(f"\nКоличество фильмов длиннее 120 минут: {long_movies_count}")

# Этап 4. Строки
def normalize_title(title):
    words = title.split()
    normalized_words = []

    for word in words:
        if word:
            normalized_word = word[0].upper() + word[1:]
            normalized_words.append(normalized_word)
    return ' '.join(normalized_words)

def make_slug(title):
    return title.lower().replace(' ', '-')

def format_report_line(movie):
    title = normalize_title(movie["title"])
    sorted_genres = sorted(movie["genres"])
    readable_duration = duration_in_hours(movie["duration_min"])
    return (f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, 'f'{readable_duration}, жанры: {", ".join(sorted_genres)}')

#print(normalize_title("silent hours"))
#print(make_slug("Silent Hours"))
print(format_report_line(movies[7]))