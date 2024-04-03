from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_no_genre_available(self):
        collector = BooksCollector()

        collector.add_new_book('Бойцовский клуб')

        assert collector.get_book_genre('Бойцовский клуб') == ''

    def test_set_book_genre_change_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Фантастика')
        collector.set_book_genre('Сияние', 'Ужасы')

        assert collector.get_book_genre('Сияние') == 'Ужасы'

    def test_get_book_genre_new_genre(self):

        collector = BooksCollector()

        collector.add_new_book('Армагеддон')
        collector.set_book_genre('Армагеддон', 'Фантастика')

        assert collector.get_book_genre('Армагеддон') == 'Фантастика'

    def test_get_books_with_specific_genre_positive(self):
        collector = BooksCollector()

        collector.add_new_book('Армагеддон')
        collector.set_book_genre('Армагеддон', 'Фантастика')
        collector.add_new_book('Три кота')
        collector.set_book_genre('Три кота', 'Мультфильмы')
        collector.add_new_book('Фиксики')
        collector.set_book_genre('Фиксики', 'Мультфильмы')

        assert len(collector.get_books_with_specific_genre('Мультфильмы')) == 2

    def test_get_books_genre_is_not_empty(self):
        collector = BooksCollector()

        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')

        assert len(collector.get_books_genre()) != 0

    def test_get_books_for_children_not_for_children(self):
        collector = BooksCollector()

        collector.add_new_book('Аватар')
        collector.set_book_genre('Аватар', 'Фантастика')
        collector.add_new_book('Поворот не туда')
        collector.set_book_genre('Поворот не туда','Ужасы')
        collector.add_new_book('Настоящий детектив')
        collector.set_book_genre('Настоящий детектив','Детективы')
        collector.add_new_book('Американский пирог')
        collector.set_book_genre('Американский пирог', 'Комедии')
        collector.add_new_book('Чип и Дейл')
        collector.set_book_genre('Чип и Дейл','Мультфильмы')

        assert 'Поворот не туда' and 'Настоящий детектив' not in collector.get_books_for_children()

    def test_add_book_in_favorites_add_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Аватар')
        collector.add_new_book('Поворот не туда')
        collector.add_new_book('Настоящий детектив')
        collector.add_new_book('Американский пирог')
        collector.add_new_book('Чип и Дейл')
        collector.add_book_in_favorites('Аватар')

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_delete_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Аватар')
        collector.add_book_in_favorites('Аватар')
        collector.delete_book_from_favorites('Аватар')

        assert len(collector.get_list_of_favorites_books()) == 0

    @pytest.mark.parametrize('genre', ['Исторические', 'Триллер', 'Аниме'])
    def test_get_book_with_specific_genre_no_such_genre(self, genre):
        collector = BooksCollector()

        collector.add_new_book('Аватар')
        collector.set_book_genre('Аватар', 'Фантастика')
        collector.add_new_book('Поворот не туда')
        collector.set_book_genre('Поворот не туда','Ужасы')
        collector.add_new_book('Настоящий детектив')
        collector.set_book_genre('Настоящий детектив','Детективы')
        collector.add_new_book('Американский пирог')
        collector.set_book_genre('Американский пирог', 'Комедии')
        collector.add_new_book('Чип и Дейл')
        collector.set_book_genre('Чип и Дейл','Мультфильмы')

        assert collector.get_books_with_specific_genre(genre) == []