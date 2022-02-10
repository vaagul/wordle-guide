from filter_engine.orchestrator import Orchestrator

if __name__ == '__main__':
    orchestrator = Orchestrator()
    while True:
        value = input("Enter choice: \n1. Load all possible answers\n"
                      "2. Add filter\n3. Display master list length\n"
                      "4. Display master list\n5. Recommend word\n")
        if value == "0":
            break
        orchestrator.handle_selection(value)