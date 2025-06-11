class Election:
    def __init__(self):
        self.votes = []  # List to store (voter, candidate) tuples
        self.voters = []

    def add_vote(self, voter, candidate):
        """Adds a vote to the election."""
        if voter not in self.voters:
            self.votes.append((voter, candidate))
            self.voters.append(voter)
        else:
            print("you have already voted")

    def count_votes(self):
        """Counts votes per candidate using a dictionary."""
        vote_count = {}
        for _, candidate in self.votes:
            if candidate in vote_count:
                vote_count[candidate] += 1
            else:
                vote_count[candidate] = 1
        return vote_count


# Example usage:
election = Election()
election.add_vote("Voter1", "CandidateA")
election.add_vote("Voter2", "CandidateB")
election.add_vote("Voter3", "CandidateA")
election.add_vote("Voter4", "CandidateC")
election.add_vote("Voter4", "CandidateA")

vote_counts = election.count_votes()
print("Vote counts per candidate:")
for candidate, count in vote_counts.items():
    print(f"{candidate}: {count}")
