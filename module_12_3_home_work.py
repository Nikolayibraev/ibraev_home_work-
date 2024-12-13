import unittest

def skip_if_frozen(test_func):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        return test_func(self, *args, **kwargs)

    return wrapper


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


class RunnerTest(unittest.TestCase):
    is_frozen = False                  #пропускаем тесты

    @skip_if_frozen
    def test_run(self):
        runner = Runner("TestRunner")
        runner.run()
        self.assertEqual(runner.distance, 10)

    @skip_if_frozen
    def test_walk(self):
        runner = Runner("TestRunner")
        runner.walk()
        self.assertEqual(runner.distance, 5)

    @skip_if_frozen
    def test_challenge(self):
        runner1 = Runner("Runner1", speed=10)
        runner2 = Runner("Runner2", speed=5)

        runner1.run()
        runner2.run()

        self.assertGreater(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_if_frozen
    def test_first_tournament(self):
        runner1 = Runner("Runner1", speed=10)
        runner2 = Runner("Runner2", speed=5)

        tournament = Tournament(30, runner1, runner2)
        finishers = tournament.start()

        self.assertEqual(len(finishers), 2)

    @skip_if_frozen
    def test_second_tournament(self):
        runner1 = Runner("Runner1", speed=8)
        runner2 = Runner("Runner2", speed=7)

        tournament = Tournament(50, runner1, runner2)
        finishers = tournament.start()

        self.assertEqual(len(finishers), 2)

    @skip_if_frozen
    def test_third_tournament(self):
        runner1 = Runner("Runner1", speed=6)

        tournament = Tournament(20, runner1)
        finishers = tournament.start()

        self.assertEqual(len(finishers), 1)


if __name__ == "__main__":
    suite = unittest.TestSuite()

    suite.addTests(unittest.makeSuite(RunnerTest))
    suite.addTests(unittest.makeSuite(TournamentTest))

    runner = unittest.TextTestRunner(verbosity=2)

    result = runner.run(suite)


    if result.skipped:
        print(f"Ran {result.testsRun} tests in {result.timeTaken:.3f}s OK (skipped={len(result.skipped)})")
