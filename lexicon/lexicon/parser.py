from lexicon.sentence import Sentence

verbs = {"go", "stop", "kill", "eat"}
directions = {"north", "south", "east", "west", "down", "up", "left", "right",
              "back"}
stopWords = {"the", "in", "of", "from", "at", "it"}
nouns = {"door", "bear", "princess", "cabinet"}


def scan(string):
    tokens = string.split(" ")
    result = []
    for token in tokens:
        if (is_numbers(token)):
            result.append(("number", int(token)))
        elif (is_verbs(token)):
            result.append(("verb", token))
        elif (is_directions(token)):
            result.append(("direction", token))
        elif (is_stopWords(token)):
            result.append(("stop", token))
        elif (is_nouns(token)):
            result.append(("noun", token))
        else:
            result.append(("error", token))
    return result


def is_numbers(token):
    return True if token.isdigit() else False


def is_verbs(token):
    return True if token.lower() in verbs else False


def is_directions(token):
    return True if token.lower() in directions else False


def is_stopWords(token):
    return True if token.lower() in stopWords else False


def is_nouns(token):
    return True if token.lower() in nouns else False


def peek(word_list):
    if word_list:
        return word_list[0][0]
    else:
        return None


def match(word_list, type):
    if not word_list:
        return None
    word = word_list.pop(0)
    if word[0] == type:
        return word
    else:
        raise ParseError


def skip(word_list, word_type):
    if word_list:
        while peek(word_list) == word_type:
            match(word_list, word_type)


def parse_subject(word_list):
    skip(word_list, "stop")
    word_type = peek(word_list)
    if word_type == "noun":
        return match(word_list, "noun")
    elif word_type == "verb":
        return ("noun", "Player")
    else:
        raise ParseError


def parse_verb(word_list):
    skip(word_list, "stop")
    word_type = peek(word_list)
    if word_type == "verb":
        return match(word_list, "verb")
    else:
        raise ParseError


def parse_object(word_list):
    skip(word_list, "stop")
    word_type = peek(word_list)
    if word_type == "noun":
        return match(word_list, "noun")
    if word_type == "direction":
        return match(word_list, "direction")
    else:
        raise ParseError


def parse_sentence(word_list):
    subject = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)
    return Sentence(subject, verb, obj)


class ParseError(Exception):
    pass
