from random import randint

adjectives = [
    "admiring",
    "adoring",
    "agitated",
    "amazing",
    "angry",
    "awesome",
    "backstabbing",
    "berserk",
    "big",
    "boring",
    "clever",
    "cocky",
    "compassionate",
    "condescending",
    "cranky",
    "desperate",
    "determined",
    "distracted",
    "dreamy",
    "drunk",
    "ecstatic",
    "elated",
    "elegant",
    "evil",
    "fervent",
    "focused",
    "furious",
    "gigantic",
    "gloomy",
    "goofy",
    "grave",
    "happy",
    "high",
    "hopeful",
    "hungry",
    "insane",
    "jolly",
    "jovial",
    "kickass",
    "lonely",
    "loving",
    "mad",
    "modest",
    "naughty",
    "nostalgic",
    "pensive",
    "prickly",
    "reverent",
    "romantic",
    "sad",
    "serene",
    "sharp",
    "sick",
    "silly",
    "sleepy",
    "small",
    "stoic",
    "stupefied",
    "suspicious",
    "tender",
    "thirsty",
    "tiny",
    "trusting"
]

names = [
    "lisa",
    "james",
    "janek",
    "aaron",
    "preston",
    "nicole",
    "david",
    "jen",
    "jennifer",
    "allegra",
    "sandy",
    "jorge"
]


def get_random_name():
    adj = adjectives[randint(0, len(adjectives)-1)]
    name = names[randint(0, len(names)-1)]
    return "{}_{}".format(adj, name)

if __name__ == '__main__':
    print get_random_name()
