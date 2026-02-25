from app.utils.pagination import pagination


class TestPagination:
    def test_get_pagination(self):
        expected = (3, 6)
        res = pagination(2, 3, 10)
        assert res == expected

    def test_get_pagination_of_last_page_with_a_length_not_divisible_by_offset(self):
        expected = (9, 10)
        res = pagination(4, 3, 10)
        assert res == expected

    def test_get_pagination_of_page_under_1(self):
        expected = (0, 3)
        res = pagination(-2, 3, 10)
        assert res == expected

    def test_get_pagination_of_page_above_length(self):
        expected = (5, 10)
        res = pagination(12, 5, 10)
        assert res == expected

    def test_get_pagination_of_offset_bigger_than_length(self):
        expected = (0, 10)
        res = pagination(2, 100, 10)
        assert res == expected
