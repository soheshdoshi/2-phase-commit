import random


class participant:
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


class coordinate:
    def __init__(self, participants):
        self.participants = participants

    def send_prepare(self):
        votes = []
        for p in self.participants:
            vote = p.vote()
            votes.append(vote)
        return votes

    def send_commit(self):
        for p in self.participants:
            p.commit()

    def send_abort(self):
        for p in self.participants:
            p.abort()

    def two_phase_commit(self):
        votes = self.send_prepare()

        if all(vote == "commit" for vote in votes):
            print("all commit done")
            self.send_commit()

        else:
            print("all vote is not commit proply")
            self.send_abort()


def test_function():
    p = [participant(f"participant {i}") for i in range(5)]
    c = coordinate(p)

    c.two_phase_commit()


if __name__ == '__main__':
    test_function()
