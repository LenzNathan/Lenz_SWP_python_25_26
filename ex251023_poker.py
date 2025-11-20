import random


# Aufgabe: zufällige Pokerhände analysieren und bewerten
# Kombinationen mit Wikipedia abgleichen

# Gibt den Wert und die Farbe der Karte zurück
def show_card(i):
    farbe = ('Herz', 'Karo', 'Kreuz', 'Pik')
    wert = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
    f = i % 4
    w = i // 4
    return farbe[f] + "  " + wert[w] if w != 8 else farbe[f] + " " + wert[w]


# Gibt eine gesamte Hand mit Wert und Farbe der Karten zurück
def show_hand(hand):
    s = ""
    for i in hand:
        s += show_card(i) + ", "
    return s[:-2]


# Druckt das gesamte Kartendeck in leserlicher Form mit den entsprechenden Indizes
def print_deck():
    for i in range(0, 52, 4):
        for j in range(4):
            print(end="    | ") if j != 0 else print(end="| ")

            if i + j >= 10:
                print(i + j, "| " + show_card(i + j), end=" |")
            else:
                print("", i + j, "| " + show_card(i + j), end=" |")  # ',' makes a space too
        print()


# Zieht eine zufällige Pokerhand (5 Karten) aus dem Deck
def draw_hand():
    deck = list(range(52))
    random.shuffle(deck)
    hand = deck[:5]
    return hand


# gibt zurück, was man auf der Hand hat
def analyze_hand(hand):
    # region Eingabevalidierung
    if len(hand) != 5:
        raise ValueError("Hand must contain exactly 5 cards")
    if len(set(hand)) != 5:
        raise ValueError("Hand contains duplicate cards")
    # endregion

    # region Variablendeklaration
    hand_state = "High Card"
    op = -1  # one pair
    toak = -1  # three of a kind
    str = -1  # straight: -1 = false, 0 = true, 1 = bruch A->2
    flu = False  # flush
    # endregion

    hand.sort()  # somit liegen die Karten mit gleichem Wert nebeneinander

    # region Two Pair
    for i in range(len(hand)):
        # removes one card because 4 cards form the two pairs and the fifth could separate the pairs anywhere
        a = hand[:i] + hand[i + 1:]
        if a[0] // 4 == a[1] // 4 and a[2] // 4 == a[3] // 4:
            hand_state = "Two Pair"
            break
    # endregion
    # region Four of a Kind
    for i in range(2):  # either first 4 or last 4
        if hand[i] // 4 == hand[i + 1] // 4 == hand[i + 2] // 4 == hand[i + 3] // 4:
            hand_state = "Four of a Kind"
            break
    # endregion
    # region Three of a Kind
    if hand_state != "Four of a Kind":
        for i in range(len(hand) - 2):
            if hand[i] // 4 == hand[i + 1] // 4 == hand[i + 2] // 4:
                hand_state = "Three of a Kind"
                toak = hand[i] // 4  # Merke den Wert des Drilling
                break
    # endregion
    # region One Pair
    if hand_state != "Four of a Kind" and hand_state != "Two Pair":
        for i in range(len(hand) - 1):
            # wenn es schon ein Drilling ist, darf das Paar nicht auf die gleichen Karten zeigen
            if hand[i] // 4 == hand[i + 1] // 4 != toak:
                hand_state = "One Pair"
                op = hand[i] // 4  # Merke den Wert des Paares
                break
    # endregion
    # region Straight
    # alle Zahlen in einer Reihe, aber nach A kommt 2 (also ein Kreis)
    if (hand[0] // 4) == (hand[1] // 4) - 1 == (hand[2] // 4) - 2 == (hand[3] // 4) - 3 == (hand[4] // 4) - 4:
        hand_state = "Straight"
        str = 0  # normaler Straight
    if hand[4] // 4 == 12 and hand[
        3] // 4 != 11 and hand_state != "One Pair" and hand_state != "Three of a Kind" and hand_state != "Four of a Kind" and hand_state != "Two Pair":
        if hand[0] // 4 == 0 and hand[1] // 4 == 1 and hand[2] // 4 == 2 and hand[3] // 4 == 3:
            hand_state = "Straight"
            str = 1  # Straight mit wrapping A = 1
    # Hier dachte ich zuerst, dass die Ass den Zahlenstral zu einem Kreis macht, aber eigentlich darf nur die A als 1 gewertet werden
    # wenn die höchste Karte ein Ass ist und die niedrigste eine 1, dann müssen wir A -> 2 berücksichtigen
    # if hand[4] // 4 == 12 and hand[0] // 4 == 0:
    #     # Die Idee: zählen wie viele Karten in der Reihe von unten nach oben
    #     # und von oben nach unten sind, wenn sie sich aufsummieren, sind alle Karten Teil der Reihe
    #     countup = True
    #     i = 1  # begin checking second number, first one is already correct
    #     while countup:
    #         if hand[i] // 4 == hand[i - 1] // 4 + 1:
    #             i += 1
    #         else:
    #             countup = False
    #     j = 1  # same here
    #     while not countup:  # not countup means countdown
    #         if hand[len(hand) - j] // 4 == hand[len(hand) - j - 1] // 4 + 1:
    #             j += 1
    #         else:
    #             countup = True
    #     if (i + j) == len(hand):
    #         hand_state = "Straight"
    #         str = 1  # Straight mit bruch A->2
    # endregion
    # region Flush
    if hand[0] % 4 == hand[1] % 4 == hand[2] % 4 == hand[3] % 4 == hand[4] % 4:
        hand_state = "Flush"
        flu = True
    # endregion
    # region Full House
    if op != -1 and toak != -1 and op != toak:  # es darf natürlich nicht derselbe Wert sein (alle drillinge wären full houses)
        hand_state = "Full House"
    # endregion
    # region Straight Flush
    if str >= 0 and flu:
        hand_state = "Straight Flush"
    # endregion
    # region Royal Flush
    if (hand[4] // 4) == 12 and str == 0 and flu:
        hand_state = "Royal Flush"
    # endregion

    # print("op:", op, " toak:", toak, " str:", str, " flu:", flu)
    return hand_state


# Zieht eine gewisse Menge an Karten und gibt eine List zurück in der steht welche Kombination wie oft gezogen wurde
def analyze_hands(amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    results = {}
    # region Progress vars
    progress = 0
    print("0.00 %", end="\r", flush=True)
    step = amount / 10000 if amount >= 1_000_000 else amount / 1000 if amount >= 100_000 else amount / 100
    # endregion
    for _ in range(amount):
        # region Fortschrittsanzeige
        if _ % step == 0 and _ != 0:
            print(f"{progress:.2f}", "%", end="\r", flush=True)
            progress = _ / (amount) * 100
        # endregion
        hand = draw_hand()
        result = analyze_hand(hand)
        if result in results:
            results[result] += 1
        else:
            results[result] = 1
    print("100.00 %\n")
    return results


# printet die Analyse für results in die Konsole, mit compare werden die Daten mit Wikipedia verglichen
def visualize_analysis(results, compare=False):
    wikipedia_data = {
        "Royal Flush": 0.000154,
        "Straight Flush": 0.00139,
        "Four of a Kind": 0.02401,
        "Full House": 0.1441,
        "Flush": 0.1965,
        "Straight": 0.3925,
        "Three of a Kind": 2.1128,
        "Two Pair": 4.7539,
        "One Pair": 42.2569,
        "High Card": 50.1177}
    if compare:
        print("Visualizing analysis with comparison to Wikipedia data:")
        print(" Calculated % |  Wikipedia % | rel_diff% |   Count  | Hand Type")
    else:
        print("Visualizing analysis:")
    total_hands = sum(results.values())
    for hand_type, count in sorted(results.items(), key=lambda kv: kv[1], reverse=True):
        percentage = (count / total_hands) * 100
        if compare:
            wiki_percentage = wikipedia_data.get(hand_type, 0)
            print(
                f"{percentage:12.8f}% | {wiki_percentage:12.8f} | {(percentage - wiki_percentage) / wiki_percentage * 100:8.3f}% | {count:8.0f} | {hand_type}")
        else:
            if percentage >= 10:
                print(f"{percentage:.8f}% | {count:8.0f} | {hand_type}")
            else:
                print(f" {percentage:.8f}% | {count:8.0f} | {hand_type}")


# Einfache Benutzeroberfläche zum Interagieren mit dem Programm
def ui():
    print("Welcome to poker!")
    print("Available commands: help, deck, draw, show, amount <number>, setup or amount, analyze -c, review -c, exit.",
          end="\n\n")
    hand = [0, 1, 2, 3, 4]
    amount = 100_000
    last_results = {}
    while True:
        command = input().strip().lower()
        if command.startswith("amount "):
            try:
                amount = int(command.split(" ")[1])
                if amount > 0:
                    print("amount set to", amount)
                else:
                    print("amount must be positive")
            except (IndexError, ValueError):
                print("Invalid amount command. Usage: amount <number>")
        else:
            match command:
                case "help":
                    print("Available commands: help, deck, draw, show, exit, amount <number>, setup, analyze.")
                    print("help: shows this help message.")
                    print("deck: shows the entire deck with indices.")
                    print("draw: draws a random poker hand of 5 cards.")
                    print("show: shows the current hand and its analysis.")
                    print("amount <number>: sets the number of hands to analyze when using 'analyze'.")
                    print("setup: shows the current setup (amount of hands to analyze).")
                    print("analyze: calculates 'amount' random poker hands, analyzes them and shows statistics.")
                    print("analyze -c: same as analyze, but compares results to Wikipedia data.")
                    print("review: reviews the last analysis results.")
                    print("review -c: reviews the last analysis results with comparison to Wikipedia data.")
                    print("exit: exits the program.")
                case "deck":
                    print_deck()
                # region Extra commands I used for testing
                # THIS CODE IS NOT BEAUTIFUL, DON'T JUDGE ME
                # case "draw -straight":
                #     hand = draw_hand()
                #     while analyze_hand(hand) != "Straight":
                #         hand = draw_hand()
                #     hand.sort()
                #     print("Drew straight hand:", show_hand(hand))
                #     print("Hand analysis:", analyze_hand(hand))
                # case "draw -royalflush":
                #     hand = draw_hand()
                #     while analyze_hand(hand) != "Royal Flush":
                #         hand = draw_hand()
                #     hand.sort()
                #     print("Drew royal flush hand:", show_hand(hand))
                #     print("Hand analysis:", analyze_hand(hand))
                # case "draw -straightflush":
                #     hand = draw_hand()
                #     while analyze_hand(hand) != "Straight Flush":
                #         hand = draw_hand()
                #     hand.sort()
                #     print("Drew straight flush hand:", show_hand(hand))
                #     print("Hand analysis:", analyze_hand(hand))
                # endregion
                case "draw":
                    hand = draw_hand()
                    hand.sort()
                    print("Drew hand:", show_hand(hand))
                    print("Hand analysis:", analyze_hand(hand))
                case "show":
                    hand.sort()
                    print("Current hand:", show_hand(hand))
                    print("Hand analysis:", analyze_hand(hand))
                case "amount":
                    print("amount:", amount)
                case "setup":
                    print("amount:", amount)
                case "analyze":
                    print(f"Analyzing {amount} hands...")
                    results = analyze_hands(amount)
                    last_results = results
                    visualize_analysis(results)
                case "analyze -c":
                    print(f"Analyzing {amount} hands with comparison to Wikipedia data...")
                    results = analyze_hands(amount)
                    last_results = results
                    visualize_analysis(results, compare=True)
                case "review":
                    if last_results:
                        print("Reviewing last analysis results:")
                        visualize_analysis(last_results)
                    else:
                        print("No previous analysis results to review.")
                case "review -c":
                    if last_results:
                        print("Reviewing last analysis results with comparison to Wikipedia data:")
                        visualize_analysis(last_results, compare=True)
                    else:
                        print("No previous analysis results to review.")
                case "exit":
                    print("Exiting poker...")
                    break
                case _:
                    print("Unknown command. Type 'help' for a list of commands.")
        print()


def main():
    ui()


# ein paar tests um die Funktionalität zu testen (auch hier hatte ich zuvor Fehler)
def run_tests():
    # Test cases for analyze_hand function
    test_hands_straight = [
        [0, 4, 8, 12, 17],
        [49, 45, 42, 39, 35]
    ]
    test_hands_four_of_a_kind = [
        [0, 1, 2, 3, 4]
    ]
    test_hands_one_pair = [
        [37, 43, 48, 49, 1],
        [47, 50, 2, 4, 5],
        [0, 3, 13, 34, 47],
        [46, 21, 12, 6, 4],
        [44, 29, 49, 20, 31]
    ]
    test_hands_high_card = [
        [40, 44, 49, 0, 10],
        [51, 0, 5, 10, 16],
    ]
    test_hands_flush = [
        [0, 4, 8, 12, 20],
    ]
    test_hands_two_pair = [
        [0, 1, 4, 5, 10]
    ]
    test_hands_three_of_a_kind = [
        [0, 1, 2, 5, 10]
    ]
    test_hands_full_house = [
        [0, 1, 2, 4, 5]
    ]
    test_hands_straight_flush = [
        [0, 4, 8, 12, 16]
    ]

    i = 0
    for hand in test_hands_straight:
        result = analyze_hand(hand)
        assert result == "Straight", f"Test failed for {show_hand(hand)}: expected Straight, got {result}"
        i += 1
    for hand in test_hands_four_of_a_kind:
        result = analyze_hand(hand)
        assert result == "Four of a Kind", f"Test failed for {show_hand(hand)}: expected Four of a Kind, got {result}"
        i += 1
    for hand in test_hands_one_pair:
        result = analyze_hand(hand)
        assert result == "One Pair", f"Test failed for {show_hand(hand)}: expected One Pair, got {result}"
        i += 1
    for hand in test_hands_high_card:
        result = analyze_hand(hand)
        assert result == "High Card", f"Test failed for {show_hand(hand)}: expected High Card, got {result}"
        i += 1
    for hand in test_hands_flush:
        result = analyze_hand(hand)
        assert result == "Flush", f"Test failed for {show_hand(hand)}: expected Flush, got {result}"
        i += 1
    for hand in test_hands_two_pair:
        result = analyze_hand(hand)
        assert result == "Two Pair", f"Test failed for {show_hand(hand)}: expected Two Pair, got {result}"
        i += 1
    for hand in test_hands_three_of_a_kind:
        result = analyze_hand(hand)
        assert result == "Three of a Kind", f"Test failed for {show_hand(hand)}: expected Three of a Kind, got {result}"
        i += 1
    for hand in test_hands_full_house:
        result = analyze_hand(hand)
        assert result == "Full House", f"Test failed for {show_hand(hand)}: expected Full House, got {result}"
        i += 1
    for hand in test_hands_straight_flush:
        result = analyze_hand(hand)
        assert result == "Straight Flush", f"Test failed for {show_hand(hand)}: expected Straight Flush, got {result}"
        i += 1
    print(i, "tests passed.")


if __name__ == "__main__":
    run_tests()
    print_deck()
    main()
