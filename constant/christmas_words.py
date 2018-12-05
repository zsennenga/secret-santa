from random import randint

CHRISTMAS_WORDS = [
    "advent",
    "bells",
    "blitzen",
    "candles",
    "candy",
    "candy-canes",
    "cards",
    "cedar",
    "celebrate",
    "ceremonies",
    "chimney",
    "cookies",
    "tree",
    "cold",
    "comet",
    "crowds",
    "cupid",
    "dancer",
    "dasher",
    "december",
    "decorations",
    "dolls",
    "donner",
    "dressing",
    "eggnog",
    "elves",
    "family",
    "festival",
    "fir",
    "frosty",
    "fruitcake",
    "gift-boxes",
    "gifts",
    "goodwill",
    "greetings",
    "ham",
    "happy",
    "holiday",
    "holly",
    "holy",
    "icicles",
    "jolly",
    "lights",
    "lists",
    "merry",
    "miracle",
    "mistletoe",
    "new-year",
    "noel",
    "north-pole",
    "pageant",
    "parades",
    "party",
    "pie",
    "pine",
    "plum-pudding",
    "poinsettia",
    "prancer",
    "presents",
    "punch",
    "reindeer",
    "ribbon",
    "rudolph",
    "sacred",
    "sales",
    "sauce",
    "Scrooge",
    "season",
    "sled",
    "sleigh-bells",
    "snowflakes",
    "spirit",
    "St-nick",
    "stand",
    "star",
    "stickers",
    "stocking-stuffers",
    "sweet-potato",
    "tidings",
    "tinsel",
    "togetherness",
    "toys",
    "tradition",
    "traffic",
    "trips",
    "turkey",
    "vacation",
    "Vixen",
    "Winter",
    "worship",
    "wrapping-paper",
    "wreath",
    "yule",
    "yuletide",
    "zach",
    "nora"
]


def get_index():
    return randint(0, len(CHRISTMAS_WORDS) - 1)


def gen_phrase():
    indexes = []

    while len(indexes) < 5:
        index = get_index()
        if index in indexes:
            continue
        indexes.append(index)

    return "-".join(
        [
            CHRISTMAS_WORDS[index].lower()
            for index in indexes
        ]
    )
