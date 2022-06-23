import requests as req
from bs4 import BeautifulSoup

POSSIBLE_SCORES = {"2 - 1", "2 - 0", "1 - 2", "0 - 2"}

def parsePlayerPage(url):
    page = req.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    # decks = soup.find_all("a", attrs={"class": "basic-black-text"})
    decks = soup.select("a.basic-black-text")

    decknames = []
    deckcodes = []

    for deck in decks:
        # print(deck)
        decknames.append(deck.get_text())
        deckcodes.append(deck.attrs["href"][6:])

    tables = soup.select("table.table.is-striped.is-fullwidth.is-narrow")
    # print(tables[1])
    playerStats = []
    opponentStats = []
    scores = []
    opponentNicknames = []

    for score in tables[1].select("td.a"):
        print(score)
        scoreText = score.get_text()
        if scoreText in POSSIBLE_SCORES:
            scores.append(scoreText)
    print(scores)
    return page.text


parsePlayerPage("https://www.d0nkey.top/battlefy/tournament/628ffe0f3fafb65c4aec72ad/player/CheeseHead%232178")
# with open("page.html", 'w') as html:
#     print(parsePlayerPage("https://www.d0nkey.top/battlefy/tournament/628ffe0f3fafb65c4aec72ad/player/CheeseHead%232178"), file=html)