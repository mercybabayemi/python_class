import unittest

from tv import Tv

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.tv = Tv()

    def test_that_turn_on_set_is_on_to_true(self):
        self.tv.turn_on()
        self.assertTrue(self.tv.get_is_on)

    def test_that_turn_off_set_is_on_to_false(self):
        self.tv.turn_on()
        self.assertTrue(self.tv.get_is_on)
        self.tv.turn_off()
        self.assertFalse(self.tv.get_is_on)

    def test_that_volume_level_increments_volume(self):
        self.assertFalse(self.tv.get_is_on)
        self.tv.turn_on()
        self.assertTrue(self.tv.get_is_on)
        self.tv.increment_volume()
        self.assertEqual(self.tv.get_volume, 1)

    def test_that_volume_level_decrements_volume(self):
        self.assertFalse(self.tv.get_is_on)
        self.tv.turn_on()
        self.assertTrue(self.tv.get_is_on)
        self.tv.increment_volume()
        self.tv.increment_volume()
        self.tv.decrement_volume()
        self.assertEqual(self.tv.get_volume, 1)

    def test_that_volume_level_doesnt_decrement_pass_zero(self):
        self.assertFalse(self.tv.get_is_on)
        self.tv.turn_on()
        self.assertTrue(self.tv.get_is_on)
        self.tv.increment_volume()
        self.tv.increment_volume()
        self.tv.decrement_volume()
        self.tv.decrement_volume()
        self.tv.decrement_volume()
        self.assertEqual(self.tv.get_volume, 0)

    def test_that_channel_goes_up(self):
        self.assertFalse(self.tv.get_is_on)
        self.tv.turn_on()
        self.assertTrue(self.tv.get_is_on)
        self.tv.channel_up()
        self.assertEqual(self.tv.get_channel, 1)

    def test_that_channel_goes_down(self):
        self.assertFalse(self.tv.get_is_on)
        self.tv.turn_on()
        self.assertTrue(self.tv.get_is_on)
        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_down()
        self.assertEqual(self.tv.get_channel, 1)

    def test_that_channel_does_not_decrement_pass_zero(self):
        self.assertFalse(self.tv.get_is_on)
        self.tv.turn_on()
        self.assertTrue(self.tv.get_is_on)
        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_down()
        self.tv.channel_down()
        self.tv.channel_down()
        self.assertEqual(self.tv.get_channel, 0)

    def test_that_channel_sets_to_a_certain_value(self):
        self.assertFalse(self.tv.get_is_on)
        self.tv.turn_on()
        self.assertTrue(self.tv.get_is_on)
        self.tv.set_channel(5)
        self.assertEqual(self.tv.get_channel, 5)

    def test_that_mute_sets_volume_to_zero(self):
        self.assertFalse(self.tv.get_is_on)
        self.tv.turn_on()
        self.assertTrue(self.tv.get_is_on)
        self.tv.increment_volume()
        self.tv.increment_volume()
        self.tv.mute()
        self.assertEqual(self.tv.get_volume, 0)

    def test_that_unmute_sets_volume_back_to_its_previous_volume(self):
        self.assertFalse(self.tv.get_is_on)
        self.tv.turn_on()
        self.assertTrue(self.tv.get_is_on)
        self.tv.increment_volume()
        self.tv.increment_volume()
        self.tv.mute()
        self.assertEqual(self.tv.get_volume, 0)
        self.tv.unmute()
        self.assertEqual(self.tv.get_volume, 2)

if __name__ == '__main__':
    unittest.main()
