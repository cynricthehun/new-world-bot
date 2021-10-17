import fishing_actions as fish
import setup


def main():
    configs = setup.Setup()
    fish.fishing_loop(configs)


if __name__ == "__main__":
    main()
