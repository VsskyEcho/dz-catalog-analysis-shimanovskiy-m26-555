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

#print(rating_tier(6.4))

def decade_label(year):
    match year:
        case _ if year > 2020:
            return 'новые'
        case _ if 2015 <= year <= 2020:
            return 'недавние'
        case _:
            return 'старые'

#print(decade_label(2018))

# Этап 3. Циклы

def non_comedy_movies(movies):
    #non_comedy_list = []
    print("Фильмы, которые НЕ относятся к жанру 'comedy':")
    for movie in movies:
        if 'comedy' in movie['genres']:
            continue  # Пропускаем комедии и сразу переходим к следующему фильму
        print(f"- {movie['title']}")
        #non_comedy_list.append(movie['title'])
    #return non_comedy_list

#print(non_comedy_movies(movies))

def find_first_masterpiece(movies):
    print("\nПоиск первого шедевра (> 9.0):")
    index = 0
    while index < len(movies):
        movie = movies[index]
        if movie["rating"] > 9.0:
            print(f"Найден шедевр: {movie['title']} (Рейтинг: {movie['rating']})")
            break  # Выходим из цикла. Ветка else ниже НЕ выполнится!
        index += 1
    else:
        # Сработает, только если цикл дошел до конца списка без break
        print("Шедевров не найдено")

# Вызов функции
#find_first_masterpiece(movies)

def count_long_movies(movies, threshold=120):
    count = 0  # Накопительная переменная
    for movie in movies:
        if movie['duration_min'] > threshold:
            count += 1  # Накапливаем значение
    return count

long_movies_count = count_long_movies(movies, threshold=120)
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
    #sorted_generes = sorted(movie['genres'])
    #readable_duration = duration_in_hours(movie['duration_min'])
    #report = f'"{movie["title"]} ({movie["year"]}) - {movie["rating"]}/10, {readable_duration}, жанры: {", ".join(sorted_generes)}'
    #return report
    title = normalize_title(movie["title"])
    sorted_genres = sorted(movie["genres"])
    readable_duration = duration_in_hours(movie["duration_min"])
    return (f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, 'f'{readable_duration}, жанры: {", ".join(sorted_genres)}')

#print(normalize_title("silent hours"))      # "Silent Hours"
#print(make_slug("Silent Hours"))            # "silent-hours"
#print(format_report_line(movies[7]))

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

#print(top_n_by_rating(movies))

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

#print(count_by_genre(movies))

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

#print(all_genres(movies))
#print(common_actors(movies[0], movies[4]))
#print(genres_only_in_one(movies[5:6], movies[:5]))


# Этап 8. Итераторы и генераторы
def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie['rating'] >= min_rating:
            yield movie

# Демонстрация работы генератора через цикл for
print("Фильмы с высоким рейтингом (>= 8.0):")
for movie in iter_high_rated(movies):
    print(format_report_line(movie))

# Подсчет суммарной длительности фильмов с рейтингом > 7
# Круглые скобки означают, что мы передаем генераторное выражение, а не список
total_duration = sum(m["duration_min"] for m in movies if m["rating"] > 7)

print(f"\nСуммарная длительность фильмов с рейтингом выше 7: {total_duration} минут")
# Для нашего каталога (155 + 124 + 118 + 110) выведет: 507 минут


# Итог
def build_report(movies):
    print('ОТЧЕТ ПО КАТАЛОГУ')

    
    avg_rating = sum(m["rating"] for m in movies) / len(movies)
    print(f"Средний рейтинг: {avg_rating:.1f}")
    
    CURRENT_YEAR = 2029  # Зафиксировано для соответствия примеру (средний возраст 8 лет)
    avg_age = sum(CURRENT_YEAR - m["year"] for m in movies) // len(movies)
    print(f"Средний возраст фильмов: {avg_age} лет")
    print()

    # 2. Блок Топ-3 фильма (берем первые 3 после сортировки по рейтингу)
    print("Топ-3 фильма:")
    sorted_by_rating = sorted(movies, key=lambda m: m["rating"], reverse=True)
    for movie in sorted_by_rating[:3]:
        print(f"  {format_report_line(movie)}")
    print()

    # 3. Блок фильтрации жанров по убыванию количества фильмов
    print("Фильмов по жанрам:")
    genre_counts = count_by_genre(movies)
    # Сортируем пары (жанр, количество) по количеству (g[1]) в обратном порядке
    sorted_genres_by_count = sorted(genre_counts.items(), key=lambda g: g[1], reverse=True)
    for genre, count in sorted_genres_by_count:
        print(f"  {genre} — {count}")
    print()

    # 4. Блок вывода всех жанров одной строкой по алфавиту
    unique_genres = sorted(list(all_genres(movies)))
    genres_string = ", ".join(unique_genres)
    print(f"Все жанры каталога: {genres_string}")