import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in sorted(self.participants, key=lambda x: x.speed, reverse=True):
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
                    break
        return finishers

# -----------------------------------------------------------------------------------------

def skip_if_frozen(test_func):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            print(f"Тесты в этом кейсе заморожены: {test_func.__name__}")
            return
        return test_func(self, *args, **kwargs)
    return wrapper


class TournamentTest(unittest.TestCase):
    all_results = {}
    is_frozen = True  # Заморожено

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усэйн', speed=10)
        self.runner2 = Runner('Андрей', speed=9)
        self.runner3 = Runner('Ник', speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    @skip_if_frozen
    def test_tournament_1(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        TournamentTest.all_results[1] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(list(results.values())[-1] == 'Ник')

    @skip_if_frozen
    def test_tournament_2(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        TournamentTest.all_results[2] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(list(results.values())[-1] == 'Ник')

    @skip_if_frozen
    def test_tournament_3(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        TournamentTest.all_results[3] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(list(results.values())[-1] == 'Ник')


class RunnerTest(unittest.TestCase):
    is_frozen = False  # Не заморожено

    @skip_if_frozen
    def test_run(self):
        runner = Runner('Тестовый бегун', speed=5)
        runner.run()
        self.assertEqual(runner.distance, 10)

    @skip_if_frozen
    def test_walk(self):
        runner = Runner('Тестовый бегун', speed=5)
        runner.walk()
        self.assertEqual(runner.distance, 5)

if __name__ == '__main__':
    unittest.main()
