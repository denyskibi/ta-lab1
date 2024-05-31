# Third-party Libraries
import sys

# Third-party Libraries
from loguru import logger

# Custom Modules
from core.karatsuba import Karatsuba
from utils import random_utils


def stop():
    sys.exit(1)


def main():
    # Створюємо необхідні обєкти для роботи програми
    karatsuba = Karatsuba()

    # Задаємо налаштування для логування повідомлень
    #   DEBUG - в консолі будуть відображатись повідомлення з кожної ітерації множення методом Карацуби
    #   INFO - в консолі будуть відображатись тільки вхідні дані і результат або попередження/помилки
    logger.remove()  # reset current logger
    logger.add(sys.stderr, level="DEBUG")  # create new logger & set log level

    try:
        # Step #1: Встановлюємо довжину чисел, які будуть генеруватись
        len_of_numbers_to_be_generated = 30

        # Step #2: Генеруємо два випадкові числа заданої довжини
        x_randomized = random_utils.generate_random_number(length=len_of_numbers_to_be_generated)
        y_randomized = random_utils.generate_random_number(length=len_of_numbers_to_be_generated)

        logger.info(f'Generated input numbers: x={x_randomized}, y={y_randomized}')

        # Step #3: Виконуємо множення двох чисел за допомогою алгоритму Карацуби.
        result = karatsuba.multiply_two_numbers(x=x_randomized, y=y_randomized)
    except KeyboardInterrupt:
        logger.error('Failed: script interrupted by user (CTRL + C)')
        stop()
    except Exception as e:
        logger.error(f'Failed due to error: {e}')
    else:
        logger.success(f'The result of multiplication by the Kartsuba method: {result}')


if __name__ == '__main__':
    main()
