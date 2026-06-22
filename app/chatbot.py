from rag_engine import ask_question

while True:
    query = input("Ask: ")

    if query == "exit":
        break

    response = ask_question(query)

    print("\nAnswer:")
    print(response)