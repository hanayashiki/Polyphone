def to_numbered_tone(pinyin_token: str) -> str:
    vowel_to_number_plain_vowel = {
        'ā': (1, 'a'),
        'á': (2, 'a'),
        'ǎ': (3, 'a'),
        'à': (4, 'a'),
        'ō': (1, 'o'),
        'ó': (2, 'o'),
        'ǒ': (3, 'o'),
        'ò': (4, 'o'),
        'ē': (1, 'e'),
        'é': (2, 'e'),
        'ě': (3, 'e'),
        'è': (4, 'e'),
        'ī': (1, 'i'),
        'í': (2, 'i'),
        'ǐ': (3, 'i'),
        'ì': (4, 'i'),
        'ū': (1, 'u'),
        'ú': (2, 'u'),
        'ǔ': (3, 'u'),
        'ù': (4, 'u'),
        'ǖ': (1, 'v'),
        'ǘ': (2, 'v'),
        'ǚ': (3, 'v'),
        'ǜ': (4, 'v')
    }

    tone = 5
    for c in pinyin_token:
        if c in vowel_to_number_plain_vowel:
            tone = vowel_to_number_plain_vowel[c][0]
            plain_vowel = vowel_to_number_plain_vowel[c][1]
            pinyin_token = pinyin_token.replace(c, plain_vowel)
            break

    return pinyin_token + str(tone)


def translate_pucts(s: str) -> str:
    s = s.replace('，', ',')
    s = s.replace('。', '.')
    s = s.replace('；', ';')
    s = s.replace('……', '...')
    return s


if __name__ == '__main__':
    vowel_test = map(to_numbered_tone, 'nǐ zhè gè ài hǎo hěn hǎo'.split(' '))
    print(list(vowel_test))
