# madlibs random story generator
from random import randint
import copy
# enter ur mad libs story
story = (
    "Last night at {} Stadium, played against {} . " +
    "It was the {} game of the Euro League Championship. " +
    "All the players were {}. " +
    "The {} coach screamed at the players that it was do or {}. " +
    "If they {} the game, then their {} would not be in the Final {}. " +
    "Our best player, {} was sick with the {} flu and had to stay at {} to get {}. " +
    "So the coach chose {} to be the {} of the team. " +
    "He plays {} and usually misses all his {} point shots. " +
    "The rest of the team were very {}." +
    "They said that the {} team needed and that he runs {} down the {} and never misses a {}. " +
    "The game began {}. " +
    "The crowd was shouting {} so that the team would {}. " +
    "At half time the score was {} to {}. " +
    "We went into the {} and everyone was {}. " +
    "We wanted to win the{}. " +
    "The coach said: Don't be {}. " +
    "We will win the {} if we have to drink {} to do it! " +
    "At the end of the game we were the {} and we had a chance to be in the Final of the {} Euro League game. "
)
# creating a word dictionary
word_dic = {
    'nouns': ['sponge', 'hoodie', 'platapus', 'swordfish', 'aden', 'loser', 'monster', 'toilet paper', 'ghost', 'jellyfish', 'unicorn', 'bathtub', 'garbage', 'bedbugs', 'popcorn', 'rhino', 'vacum cleaner', 'mop'],
    'verb': ['shrink', 'buzz', 'yodel', 'snore', 'burp', 'shave', 'tickle', 'boring', 'boiling', 'freezing', 'smelly', 'scream', 'shout', 'stink', 'shrink'],
    'adjective': ['cheap', 'scary', 'spicy', 'slimy', 'weird', 'stupid', 'disguesting', 'antique', 'smelly', 'cool', 'sloppy'],
    'adverbs': ['fast', 'solw', 'early', 'quickly', 'suddenly', 'late'],
    'number': ['7', '2', '9', '6', '5'],
    'name': ['bob', 'mike', 'alex'],
    'country_name': ['aleska', 'vegas', 'afganistan', 'srilanka'],
    'sport': ['basketball']
}


def get_word(type, local_dict):
    words = local_dict[type]
    cnt = len(words)-1
    index = randint(0, cnt)
    return local_dict[type].pop(index)


def create_story():
    local_dict = copy.deepcopy(word_dic)
    return story.format(
        get_word('nouns', local_dict),
        get_word('nouns', local_dict),
        get_word('number', local_dict),
        get_word('adjective', local_dict),
        get_word('adjective', local_dict),
        get_word('verb', local_dict),
        get_word('verb', local_dict),
        get_word('nouns', local_dict),
        get_word('number', local_dict),
        get_word('name', local_dict),
        get_word('country_name', local_dict),
        get_word('country_name', local_dict),
        get_word('adjective', local_dict),
        get_word('name', local_dict),
        get_word('nouns', local_dict),
        get_word('adverbs', local_dict),
        get_word('number', local_dict),
        get_word('adjective', local_dict),
        get_word('adjective', local_dict),
        get_word('name', local_dict),
        get_word('adverbs', local_dict),
        get_word('country_name', local_dict),
        get_word('nouns', local_dict),
        get_word('adverbs', local_dict),
        get_word('nouns', local_dict),
        get_word('verb', local_dict),
        get_word('number', local_dict),
        get_word('number', local_dict),
        get_word('country_name', local_dict),
        get_word('verb', local_dict),
        get_word('nouns', local_dict),
        get_word('adjective', local_dict),
        get_word('nouns', local_dict),
        get_word('nouns', local_dict),
        get_word('nouns', local_dict),
        get_word('sport', local_dict)
    )


print("## Story 1 : ")
print(create_story())
print()
print("## Story 2 : ")
print(create_story())
print()
print("## Story 3 : ")
print(create_story())
