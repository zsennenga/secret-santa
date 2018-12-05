import sys

from model.service.matching_service import MatchingService


def main(exchange_id):
    MatchingService().match_users(exchange_id)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: whatever.py exchange_id_as_a_number_not_a_fun_phrase")
        exit(1)

    main(sys.argv[1])
