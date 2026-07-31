from agents.search_agent import SearchAgent


def main():
    print("=" * 40)
    print("🚀 Welcome to JobPilot AI")
    print("=" * 40)

    agent = SearchAgent()
    agent.start()

    print("\n✅ JobPilot AI finished.")


if __name__ == "__main__":
    main()