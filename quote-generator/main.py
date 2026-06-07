import random

def get_random_quote():
    # List of 10 inspirational tuples (Quote, Author)
    quotes = [
        ("The only way to do great work is to love what you do.", "Steve Jobs"),
        ("Success is not final, failure is not fatal: it is the courage to continue that counts.", "Winston Churchill"),
        ("The future belongs to those who believe in the beauty of their dreams.", "Eleanor Roosevelt"),
        ("Do not watch the clock; do what it does. Keep going.", "Sam Levenson"),
        ("Keep your face always toward the sunshine - and shadows will fall behind you.", "Walt Whitman"),
        ("It always seems impossible until it's done.", "Nelson Mandela"),
        ("Happiness is not something ready-made. It comes from your own actions.", "Dalai Lama"),
        ("Don't count the days, make the days count.", "Muhammad Ali"),
        ("You miss 100% of the shots you don't take.", "Wayne Gretzky"),
        ("Act as if what you do makes a difference. It does.", "William James")
    ]
    
    # Pick a random tuple from the list
    quote, author = random.choice(quotes)
    
    # Format and print the output nicely
    print("\n" + "=" * 60)
    print(f'"{quote}" \n\t— {author}')
    print("=" * 60 + "\n")

if __name__ == "__main__":
    get_random_quote()