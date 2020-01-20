######################
## Import Libraries ##
######################

import pytest
from contextlib import contextmanager

######################
## Import Functions ##
######################

from repeated_word import repeated_word, all_repeated_words

##################
## Test Imports ##
##################

def test_function_import():
  assert repeated_word
  assert all_repeated_words

#####################
## Pytest Fixtures ##
#####################

@contextmanager
def does_not_raise():
  yield

#########################
## Test Repeated Words ##
#########################

@pytest.mark.parametrize(
  "string, result, exception",
    [
      ("Once upon a time, there was a brave princess who...", 'a', does_not_raise()),
      ("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...", 'it', does_not_raise()),
      ("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...", 'summer', does_not_raise()),
      ("This string will return None", None, does_not_raise()),
      ('This will also be a case where the string won\'t have return value: t', None, does_not_raise()),
      (30, None, pytest.raises(ValueError)),
      (True, None, pytest.raises(ValueError)),
      ([], None, pytest.raises(ValueError)),
    ],
)
def test_first_repeat(string, result, exception):
  with exception:
    assert repeated_word(string) == result

