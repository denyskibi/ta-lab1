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
    logger.add(sys.stderr, level="INFO")  # create new logger & set log level

    try:
        # Step #1: Встановлюємо довжину чисел, які будуть генеруватись
        len_of_numbers_to_be_generated = 30

        # Step #2: Генеруємо два випадкові числа заданої довжини
        x_randomized = random_utils.generate_random_number(length=len_of_numbers_to_be_generated)
        y_randomized = random_utils.generate_random_number(length=len_of_numbers_to_be_generated)

        logger.info(f'Generated input numbers: x={x_randomized}, y={y_randomized}')

        # Step #3: Виконуємо множення двох чисел за допомогою алгоритму Карацуби:

        # Завдання #1
        # result = karatsuba.multiply_two_numbers(x=x_randomized, y=y_randomized)
        # logger.success(f'The result of multiplication by the Karatsuba method: {result}')

        # OR (запускати або блок з Завдання 1 або блок з Завдання 2)

        # Завдання #2
        result = karatsuba.multiply_two_numbers(x=x_randomized, y=y_randomized)
        calls_count = karatsuba.get_method_calls_count()
        logger.success(f'The result of multiplication by the Karatsuba method: {result}')
        logger.info(f'Karatsuba method was used {calls_count} times.')
    except KeyboardInterrupt:
        logger.error('Failed: script interrupted by user (CTRL + C)')
        stop()
    except Exception as e:
        logger.error(f'Failed due to error: {e}')
        stop()
    else:
        logger.success('Script finished without any critical errors.')


if __name__ == '__main__':
    main()
