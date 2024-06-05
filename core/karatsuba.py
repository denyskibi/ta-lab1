# Standard Libraries
from typing import Tuple

# Third-party Libraries
from loguru import logger


class Karatsuba:
    def multiply_two_numbers(self, x: int, y: int) -> float:
        logger.debug(f"Starting multiplying numbers {x} and {y} by Karatsuba method.")

        # Step #1: Перевіряємо базовий випадок рекурсії (якщо x або y < 10 - перемножуємо їх і повертаємо результат)
        if x < 10 or y < 10:
            logger.debug(f"Base recursive case occurred for input numbers x={x}, y={y}")
            return x * y

        # Step #2: Знаходимо середину довжини числа (для подальшого розділення числа на частини)
        middle_of_num_len = self._get_the_middle_of_number_len(x, y)

        # Step #3: Розділяємо числа на "верхню" та "нижню" частини
        upper_part_x, lower_part_x = self._separate_num_into_upper_and_lower_parts(middle_of_num_len, number=x)
        upper_part_y, lower_part_y = self._separate_num_into_upper_and_lower_parts(middle_of_num_len, number=y)

        # Step #4: Обчислюємо дані, які необхідно підставити в формулу
        x_parts_sum = upper_part_x + lower_part_x
        y_parts_sum = upper_part_y + lower_part_y
        z0 = self.multiply_two_numbers(lower_part_x, lower_part_y)  # Рекурсивно множимо нижні частини
        z1 = self.multiply_two_numbers(x_parts_sum, y_parts_sum)  # Рекурсивно множимо суми верхніх і нижніх частин
        z2 = self.multiply_two_numbers(upper_part_x, upper_part_y)  # Рекурсивно множимо верхні частини

        # Step #5: # Обчислюємо результат за формулою Карацуби
        result = self._calculate_result(z0, z1, z2, middle_of_num_len)
        return result

    @staticmethod
    def _get_the_middle_of_number_len(x: int, y: int) -> int:
        # Step #1: Визначаємо довжину найбільшого числа
        x_len = len(str(x))
        y_len = len(str(y))
        max_number_len = max(x_len, y_len)

        # Step #2: Знаходимо середину довжини числа
        middle_of_numbers = max_number_len // 2
        return middle_of_numbers

    @staticmethod
    def _separate_num_into_upper_and_lower_parts(middle_of_num_len: int, number: int) -> Tuple[int, int]:
        upper_part, lower_part = divmod(number, 10 ** middle_of_num_len)
        return upper_part, lower_part

    @staticmethod
    def _calculate_result(z0, z1, z2, middle_of_num_len: int) -> float:
        result = (z2 * 10 ** (2 * middle_of_num_len)) + ((z1 - z2 - z0) * 10 ** middle_of_num_len) + z0
        return result
