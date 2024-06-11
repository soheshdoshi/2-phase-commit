import random


class Participant:
    def __init__(self, name):
        self.name = name
        self.votes = None

    def vote(self):
        self.votes = random.choice(["commit", "abort"])
        print(f"{self.name} votes {self.votes}")
        return self.votes

    def commit(self):
        print(f"{self.name} commit done")

    def abort(self):
        print(f"{self.name} abort done")


class Coordinate:
    def __init__(self, participants):
        self.participants = participants

    def send_prepare(self):
        votes = []
        for participant in self.participants:
            vote = participant.vote()
            votes.append(vote)
        return votes

    def send_commit(self):
        for participant in self.participants:
            participant.commit()

    def send_abort(self):
        for participant in self.participants:
            participant.abort()

    def two_phase_commit(self):
        votes = self.send_prepare()

        if all(vote == "commit" for vote in votes):
            print("all commit done")
            self.send_commit()

        else:
            print("all vote is not commit properly")
            self.send_abort()


def test_function():
    participant_list = [Participant(f"participant {i}") for i in range(5)]
    coordinate_obj = Coordinate(participant_list)

    coordinate_obj.two_phase_commit()


if __name__ == '__main__':
    test_function()
