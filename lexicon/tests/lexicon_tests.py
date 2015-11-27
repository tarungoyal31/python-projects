from nose.tools import assert_equals
from nose.tools import assert_raises
from lexicon import parser


def test_directions():
    assert_equals(parser.scan("north"), [('direction', 'north')])
    result = parser.scan("north south east")
    assert_equals(result, [('direction', 'north'),
                           ('direction', 'south'),
                           ('direction', 'east')])


def test_verbs():
    assert_equals(parser.scan("go"), [('verb', 'go')])
    result = parser.scan("go kill Eat")
    assert_equals(result, [('verb', 'go'),
                           ('verb', 'kill'),
                           ('verb', 'Eat')])


def test_stops():
    assert_equals(parser.scan("the"), [('stop', 'the')])
    result = parser.scan("the in of")
    assert_equals(result, [('stop', 'the'),
                           ('stop', 'in'),
                           ('stop', 'of')])


def test_nouns():
    assert_equals(parser.scan("bear"), [('noun', 'bear')])
    result = parser.scan("bear princess")
    assert_equals(result, [('noun', 'bear'),
                           ('noun', 'princess')])


def test_numbers():
    assert_equals(parser.scan("1234"), [('number', 1234)])
    result = parser.scan("3 91234")
    assert_equals(result, [('number', 3),
                           ('number', 91234)])


def test_errors():
    assert_equals(parser.scan("ASDFADFASDF"), [('error', 'ASDFADFASDF')])
    result = parser.scan("bear IAS princess")
    assert_equals(result, [('noun', 'bear'),
                           ('error', 'IAS'),
                           ('noun', 'princess')])


def test_parse_sentence():
    line = "Go north"
    word_list = parser.scan(line)
    sentence = parser.parse_sentence(word_list)
    assert_equals(sentence.subject, 'Player')
    assert_equals(sentence.verb.lower(), 'go')
    assert_equals(sentence.obj, 'north')


def test_parse_exception():
    line = "go go go"
    word_list = parser.scan(line)
    assert_raises(parser.ParseError, parser.parse_sentence, word_list)
