import copy
import sys

def show(a):
    str_a = map(str, a)
    print(' '.join(str_a))


def card_compare(card1, card2, ):
    card1_number = int(card1[1:2])
    card2_number = int(card2[1:2])
    return card1_number - card2_number

def bubble_sort(a, n):
    flag = True
    while flag:
        flag = False
        for i in reversed(range(1, n)):
            if card_compare(a[i], a[i - 1]) < 0:
                a[i], a[i - 1] = a[i - 1], a[i]
                flag = True


def selection_sort(a, n):
    for i in range(0, n - 1):
        min_j = i
        for j in range(i + 1, n):
            if card_compare(a[j], a[min_j]) < 0:
                min_j = j
        a[i], a[min_j] = a[min_j], a[i]


n = int(input())
if not (0 <= n <= 100):
    print('Please integer n is 0 or more and 100 less.', sys.stderr)
    exit(1)

card_list = input().split(" ")
for card in card_list:
    if not (2 <= len(card) <= 3):
        print('Please input card info is 0 characters or more and 3 characters less.', sys.stderr)
        exit(1)

    suit = card[0]
    number = int(card[1:2])
    if not (suit == 'S' or suit == 'H' or suit == 'C' or suit == 'D'):
        print('Please input suit part character is \'S\',\'H\',\'C\',\'D\'. Input value is ' + suit, sys.stderr)
        exit(1)
    if not (1 <= number <= 13):
        print('Please input number part character is 1 or more and 13 less.', sys.stderr)
        exit(1)

card_list_for_selection = copy.copy(card_list)

bubble_sort(card_list, n)
selection_sort(card_list_for_selection, n)
show(card_list)
print("Stable")
show(card_list_for_selection)
print("Stable" if card_list == card_list_for_selection else "Not stable")