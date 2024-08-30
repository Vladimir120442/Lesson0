import time


class User:  # Класс пользователей
    def __init__(self, nickname, password, age):
        self.nickname = nickname  # имя пользователя
        self.password = hash(password)  # пароль
        self.age = age  # возраст пользователя

    def __str__(self):  # возврат строки в удобочитаемом формате
        return self.nickname

    def __eq__(self, other):  # для корректного сравнения экземпляров класса User между собой
        if isinstance(other, User):
            return self.nickname == other.nickname

    def __hash__(self):  # возврат  пароля (для сравнения хэш-значений)
        return hash(self.password)

    def __contains__(self, password):  # для проверки пароля
        return password == self.password


class Video:  # Класс видео
    def __init__(self, title, duration, adult_mode=False):
        self.title = title  # название видеоролика
        self.duration = duration  # длительность видео (сек)
        self.time_now = 0  # таймер остановки (сек)
        self.adult_mode = adult_mode  # детям до 16

    def __repr__(self):  # для возвращения строкового значения названия видеоролика
        return self.title


class UrTube:  # Класс UrTube
    def __init__(self):
        self.users = []  # объекты класса User
        self.videos = []  # объекты класса Video
        self.current_user = None  # текущий пользователь

    def log_in(self, nickname, password):  # проверка логин-пароля пользователя и вход
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                return user

    def register(self, nickname, password, age):  # регистрация нового пользователя и вход
        new_user = User(nickname, password, age)
        if new_user not in self.users:
            self.users.append(new_user)
            self.current_user = new_user
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):  # обезличивание текущего пользователя (None)
        if self.current_user:
            self.current_user = None

    def add(self, *videos):  # добавление объектов класса Video в список videos
        for i in videos:
            if i.title not in self.videos:
                self.videos.append(i)

    def get_videos(self, to_find):  # найти видеоролик по запросу
        video_find = []
        for j in self.videos:
            if to_find.lower() in str(j).lower():
                video_find.append(j)
        return video_find

    def watch_video(self, titl_film):  # воспроизведение видеоролика при совпадении titl_film и title
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for k in self.videos:
                if k.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет! Пожалуйста, покиньте страницу!')
                elif titl_film in k.title:
                    for l in range(1, k.duration + 1):
                        print(l, end=' ')
                        time.sleep(0.1)
                    print('Конец видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
