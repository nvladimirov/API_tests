class TestExamples:
    def test_check_math(self):
        a = 8
        b = 9
        assert a + b == 17
    """
    мудреный запуск 
    python -m pytest week3/text_example.py -k "test_check_math"
    юзаем питон для запуска
    -m это указывается модуль который надо использовать
    -k - это ключ, в нем указывается название теста, который надо запустить
    """
    def test_check_math2(self):
        a = 8
        b = 0
        exeption_sum = 17
        assert a + b == exeption_sum, f"Сумма переменны не равна {exeption_sum}"
