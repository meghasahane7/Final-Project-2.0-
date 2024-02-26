import streamlit as st

class Candidate:
    def __init__(self, name, party):
        self.name = name
        self.party = party
        self.votes = 0

    def add_vote(self):
        self.votes += 1

class Election:
    def __init__(self):
        self.candidates = []

    def add_candidate(self, candidate):
        self.candidates.append(candidate)

    def vote(self, candidate_index):
        if 0 <= candidate_index < len(self.candidates):
            self.candidates[candidate_index].add_vote()
            st.success("Vote cast successfully!")
        else:
            st.error("Invalid candidate index.")

    def get_results(self):
        results = []
        for candidate in self.candidates:
            results.append((candidate.name, candidate.party, candidate.votes))
        return results

def main():
    st.title("Online Election System")

    election = Election()

    st.header("Register Candidates")
    name = st.text_input("Candidate Name")
    party = st.text_input("Party Name")
    if st.button("Register Candidate"):
        candidate = Candidate(name, party)
        election.add_candidate(candidate)
        st.success("Candidate registered successfully!")

    st.header("Cast Vote")
    vote_options = [candidate.name for candidate in election.candidates]
    vote_index = st.selectbox("Select Candidate to Vote", vote_options)
    if st.button("Cast Vote"):
        election.vote(vote_options.index(vote_index))

    st.header("Election Results")
    results = election.get_results()
    for result in results:
        st.write(f"Name: {result[0]}, Party: {result[1]}, Votes: {result[2]}")

if __name__ == "__main__":
    main()
