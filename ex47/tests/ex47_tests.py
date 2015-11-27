from nose.tools import *
from ex47.game import Room

def test_room():
  gold = Room("gold room",
      """This room has gold in it you can grab. There's a
      door to the north.""")
  assert_equal(gold.name, "gold room")
  assert_equal(gold.paths, {})

def test_room_paths():
  center = Room("Center", "Test room is in the Center")
  north = Room("North", "Test room is in the North")
  south = Room("South", "Test room is in the South")

  center.add_paths({"North" : north, "South" : south})
  assert_equal(center.go("North"), north)
  assert_equal(center.go("South"), south)

def test_map():
  start = Room("Start", "You can go west and down a hole.")
  west = Room("Trees", "There are trees here, you can go east.")
  down = Room("Dungeon", "It's dark down here, you can go up.")

  start.add_paths({'west': west, 'down': down})
  west.add_paths({'east': start})
  down.add_paths({'up': start})

  assert_equal(start.go('west'), west)
  assert_equal(start.go('west').go('east'), start)
  assert_equal(start.go('down').go('up'), start)
