# # Helper Functions ----------------------------------------------------------
# def card_value(card):
#     rank, suit = card[0], card[1]
#     value = determine_rank_value(rank) + determine_suit_value(suit)
#
#     return value
#
#
# def determine_rank_value(rank):
#     if rank == 'A':
#         return '01'
#     elif rank == 'J':
#         return '10'
#     elif rank == 'Q':
#         return '11'
#     elif rank == 'K':
#         return '12'
#     else:
#         return '0' + rank
#
#
# def determine_suit_value(suit):
#     if suit == 'S':
#         return '1'
#     elif suit == 'D':
#         return '2'
#     elif suit == 'H':
#         return '3'
#     else:
#         return '4'
# # End of Helper Functions ---------------------------------------------------
#
#
# if __name__ == '__main__':
#     previous_card = 'AH'
#     shuffled_deck = 'AC AS AH AH AD'.strip().split()
#     sorted_deck = sorted(shuffled_deck, key=card_value)
#
#     # Join the elem/s of the list into a one string and then use
#     # the rindex method for a python string. This returns the
#     # starting index for the last occurrence of the previous_card
#     # (divide it by 2 since the previous_card has two character
#     # values).
#     last_occurrence_index = ''.join(sorted_deck).rindex(previous_card) // 2
#
#     # If the last occurrence of the picked_card is the last card
#     # in the sorted_deck, then choose the first card of the same
#     # deck.
#     picked_card = sorted_deck[(last_occurrence_index+1) % len(sorted_deck)]
#
#     print(shuffled_deck)
#     print(sorted_deck)
#     print(last_occurrence_index)
#     print(picked_card)


# Helper Functions ----------------------------------------------------------
def card_value(card):
    rank, suit = card[0], card[1]
    value = determine_rank_value(rank) + determine_suit_value(suit)

    return value


def determine_rank_value(rank):
    if rank == 'A':
        return '01'
    elif rank == 'J':
        return '10'
    elif rank == 'Q':
        return '11'
    elif rank == 'K':
        return '12'
    else:
        return '0' + rank


def determine_suit_value(suit):
    if suit == 'S':
        return '1'
    elif suit == 'D':
        return '2'
    elif suit == 'H':
        return '3'
    else:
        return '4'
# End of Helper Functions ---------------------------------------------------


if __name__ == '__main__':
    no_of_test_cases = int(input())

    for _ in range(no_of_test_cases):
        previous_card = input()
        shuffled_deck = input().split()
        sorted_deck = sorted(shuffled_deck, key=card_value)

        # Join the elem/s of the list into a one string and then use
        # the rindex method for a python string. This returns the
        # starting index for the last occurrence of the previous_card
        # (divide it by 2 since the previous_card has two character
        # values).
        last_occurrence_index = ''.join(sorted_deck).rindex(previous_card) // 2

        # If the last occurrence of the picked_card is the last card
        # in the sorted_deck, then choose the first card of the same
        # deck.
        picked_card = sorted_deck[(last_occurrence_index+1) % len(sorted_deck)]

        print(picked_card)
