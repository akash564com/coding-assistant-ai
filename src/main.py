from inference import CodingAI
from error_handler import run_code
from memory import Memory

def main():
    ai = CodingAI()
    memory = Memory()

    while True:
        user_input = input("\n💡 Ask your coding question (or 'exit'): ")
        if user_input.lower() == "exit":
            break

        # Recall memory
        past = memory.recall(user_input)
        if past["documents"]:
            print("\n[📖 Memory Recall]:", past["documents"])

        # Get AI response
        response = ai.ask(user_input)
        print("\n🤖 AI Response:\n", response)

        # Auto-run code block if Python detected
        if "def " in response or "print(" in response:
            print("\n[⚡ Running the generated code...]")
            result = run_code(response)
            print("Execution Result:", result)

        # Save to memory
        memory.add(user_input, response)

if __name__ == "__main__":
    main()
