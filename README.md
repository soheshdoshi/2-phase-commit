# 2-phase-commit

Explanation:
Participant Class: Simulates a participant in the 2PC protocol. It has methods to vote on the transaction and to commit or abort the transaction.
Coordinator Class: Manages the 2PC protocol. It sends the prepare message, collects votes, and then sends either a commit or abort message based on the votes.
simulate_2pc Function: Creates participants and a coordinator, then initiates the 2PC protocol.
Running the Code:
To run the code, simply execute the script. It will simulate the 2PC protocol with random votes from the participants.

This is a basic simulation and doesn't include network communication, persistence, or fault tolerance mechanisms. In a real-world implementation, you would need to handle these aspects to ensure the robustness and reliability of the 2PC protocol.
