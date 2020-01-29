import pytest

##################
## Import Graph ##
##################

from graphs import Graph

####################
## Pytest Fixture ##
####################

@pytest.fixture()
def sample_graph():
  g = Graph()
  v1 = g.add('Pandora')
  v2 = g.add('Arendelle')
  v3 = g.add('Metroville')
  v4 = g.add('Monstroplolis')
  v5 = g.add('Narnia')
  v6 = g.add('Naboo')

  g.add_double_edge(v1, v2, 150)
  g.add_double_edge(v1, v3, 82)
  g.add_double_edge(v2, v3, 99)
  g.add_double_edge(v2, v4, 42)
  g.add_double_edge(v3, v4, 105)
  g.add_double_edge(v3, v5, 37)
  g.add_double_edge(v3, v6, 26)
  g.add_double_edge(v4, v6, 73)
  g.add_double_edge(v5, v6, 250)

  return (g, [v1,v2,v3,v4,v5,v6])

###################
## Test Get Edge ##
###################


@pytest.mark.parametrize(
  "lst, expected",
    [
      (['Pandora'], (True, '$0')), # Not going anywhere
      (['Arendelle', 'Monstroplolis', 'Naboo'], (True, '$115')), #Across the graph
      (['Pandora', 'Arendelle', 'Monstroplolis'], (True, '$192')), # Prep test for next one
      (['Pandora', 'Arendelle', 'Monstroplolis', 'Metroville', 'Narnia', 'Naboo'], (True, '$584')), # Visit them all
      (['Monstroplolis', 'Metroville','Monstroplolis'], (True, '$210')), # Round Trip
      (['Pandora', 'Naboo'], (False, '$0')), # Skip a stop
      (['Pandora', 'Pandora'], (False, '$0')), # Going to self
      (['Mordor'], (False, '$0')), # Not in Graph
    ]
)
def test_single_value(sample_graph, lst, expected):

  g = sample_graph[0]

  actual = g.get_edge(lst)
  assert actual == expected
