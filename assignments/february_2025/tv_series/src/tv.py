class Tv:
    def __init__(self):
        self._is_on = False
        self._volume_level = 0
        self._channel_level = 0
        self._previous_volume_level = 0

    def turn_on(self) -> bool:
        self._is_on = True
        return self._is_on

    def turn_off(self) -> bool:
        self._is_on = False
        return self._is_on

    def increment_volume(self):
        self._volume_level += 1

    def decrement_volume(self):
        if self._volume_level > 0:
            self._volume_level -= 1

    def channel_up(self):
        self._channel_level += 1

    def channel_down(self):
        if self._channel_level > 0:
            self._channel_level -= 1

    def set_channel(self, value):
        self._channel_level = value

    def mute(self):
        self._previous_volume_level = self._volume_level
        self._volume_level = 0

    def unmute(self):
        self._volume_level = self._previous_volume_level
        self._previous_volume_level = 0
    