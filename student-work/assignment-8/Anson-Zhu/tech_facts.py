#!/usr/bin/env python3

import random
import time

def get_random_tech_fact():
    facts = [
        "The first computer bug was an actual moth found in Harvard's Mark II computer in 1947.",
        "The QWERTY keyboard layout was designed to slow down typists to prevent typewriter jams.",
        "There are more possible iterations of a game of chess than there are atoms in the known universe.",
        "The first 1GB hard drive was announced in 1980, weighed 550 pounds, and cost $40,000.",
        "The world's first website is still online: http://info.cern.ch",
        "Python was named after Monty Python, not the snake.",
        "The original name for Windows was Interface Manager.",
        "The first computer mouse was made of wood.",
        "Google's original name was BackRub.",
        "The first email was sent in 1971 by Ray Tomlinson.",
        "There are over 700 programming languages in existence.",
        "The first video game was created in 1962 and was called Spacewar!",
        "CAPTCHA stands for 'Completely Automated Public Turing test to tell Computers and Humans Apart'.",
        "The average person spends about 6 years and 8 months of their lifetime on social media."
    ]
    return random.choice(facts)

def main():
    print("Welcome to Random Tech Facts Generator!")
    print("=" * 50)
    
    for i in range(3):
        fact = get_random_tech_fact()
        print(f"Fact #{i+1}: {fact}")
        if i < 2:
            print("-" * 50)
            time.sleep(2)
    
    print("=" * 50)
    print("Thanks for learning some tech history!")

if __name__ == "__main__":
    main()
