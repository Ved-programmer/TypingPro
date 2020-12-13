texts = """Lawrence Edward Page is an American computer scientist and Internet entrepreneur. He is best known as one of the co-founders of Google.
Ved Rathi is the inventor of this game who was born on 19th May 2007, he had a passion for programming and tech. This game was first put on Github.
I wrote my first line of code a couple of weeks after graduating from college. Six months later, I landed a software engineering job at Google.
Tim a first year computer science student that has a passion for programming and everything tech! Teaching and writing guides is his favorite past-time.
This game is made By Ved Rathi, This was inspired from a website known as nitrotype. Ved made this game in 2020. It has been updated but the first version was by Ved.
Python is an interpreted, high level and general purpose programming language. Python's design philosophy emphasizes code readability.
William Henry Gates III is an American business magnate, software developer, and philanthropist. He is best known as the co-founder of Microsoft Corporation.
Hi, I am Ved Rathi. The creator of this game. I created this game for people to have fun with typing. Make sure to tell your friends about this game.
Sherlock Holmes is a fictional private detective created by British author Sir Arthur Conan Doyle. Referring to himself as a "consulting detective" in the stories, Holmes is known for his proficiency.
Sergey Mikhaylovich Brin is an American computer scientist and Internet entrepreneur. Together with Larry Page, he co-founded Google.
Mark Elliot Zuckerberg is an American media magnate, internet entrepreneur, and philanthropist. He is known for co-founding Facebook
Pichai Sundararajan, known as Sundar Pichai, is an Indian-American business executive. He is the chief executive officer of Alphabet Inc. and its subsidiary Google.
Elon Reeve Musk FRS is a business magnate, industrial designer and engineer. He is the founder, CEO, CTO and chief designer of SpaceX; early investor, CEO and product architect of Tesla, Inc.
Jeffrey Preston Bezos is an American internet entrepreneur, industrialist, media proprietor, and investor. He is best known as the founder, CEO, and president of the multi-national technology company Amazon.
Steven Paul Jobs was an American business magnate, industrial designer, investor, and media proprietor. He was the chairman, chief executive officer (CEO), and co-founder of Apple Inc.
Google, LLC is an American multinational technology company that specializes in Internet-related services and products, which include online advertising technologies, a search engine, cloud computing, software, and hardware.
""".splitlines()
import random

def getText():
    return random.choice(texts).removesuffix("\n")
