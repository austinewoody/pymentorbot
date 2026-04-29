import sys
from pymentorbot import explain, list_topics, search, quiz

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  pymentorbot explain <topic>")
        print("  pymentorbot list")
        print("  pymentorbot search <word>")
        print("  pymentorbot quiz")
        return

    command = sys.argv[1].lower()

    if command == "explain":
        if len(sys.argv) < 3:
            print("Please provide a topic. Example: pymentorbot explain lambda")
            return
        topic = " ".join(sys.argv[2:])
        print(explain(topic))

    elif command == "list":
        for topic in list_topics():
            print(topic)

    elif command == "search":
        if len(sys.argv) < 3:
            print("Please provide a search word. Example: pymentorbot search error")
            return
        query = " ".join(sys.argv[2:])
        results = search(query)
        if not results:
            print(f"No topics found for '{query}'.")
            return
        for topic in results:
            print(topic)

    elif command == "quiz":
        q = quiz()
        print("Question:")
        print(q["question"])
        print()
        print("Answer:")
        print(q["answer"])

    else:
        print(f"Unknown command: {command}")
        print("Try: explain, list, search, quiz")

if __name__ == "__main__":
    main()
