import logging
import unittest
from class_runner import Runner


logging.basicConfig(      #возможные логи
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner("John", -3)
            runner.walk()
            logging.info('test_walk выполнен успешно')
        except ValueError as e:
            logging.warning('Неверная скорость для Runner: %s', e)

    def test_run(self):
        try:
            runner = Runner('687')
            runner.run()
            logging.info('test_run выполнен успешно')
        except TypeError as e:
            logging.warning('Неверный тип данных для Runner: %s', e)


if __name__ == '__main__':
    unittest.main()
