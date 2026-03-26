from homeassistant.components.media_player import MediaPlayerEntity
from homeassistant.const import STATE_IDLE, STATE_PLAYING
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.components.media_player import MediaPlayerEntityFeature

from .const import DOMAIN


async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities([
        NavidromeMediaPlayer(coordinator)
    ])


class NavidromeMediaPlayer(CoordinatorEntity, MediaPlayerEntity):
    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_name = "Navidrome"
        self._attr_unique_id = "navidrome_media_player"

    @property
    def state(self):
        data = self.coordinator.data

        if not data:
            return STATE_IDLE

        tracks = data.get("now_playing")

        if not tracks:
            return STATE_IDLE

        return STATE_PLAYING

    @property
    def device_info(self):
        system = self.coordinator.data.get("system", {})

        return {
            "identifiers": {("navidrome", "server")},
            "name": "Navidrome",
            "manufacturer": "Navidrome",
            "model": "Music Server",
            "sw_version": system.get("version"),
            "configuration_url": self.coordinator.api.base_url,
        }

    def _get_current_track(self):
        data = self.coordinator.data

        if not data:
            return None

        tracks = data.get("now_playing")

        if not tracks or len(tracks) == 0:
            return None

        return tracks[0]

    def _get(self, key):
        track = self._get_current_track()

        if not track:
            return None

        return track.get(key)

    @property
    def media_title(self):
        artist = self._get("artist")
        title = self._get("title")

        if artist and title:
            return f"{artist} - {title}"

        return title

    @property
    def media_artist(self):
        return self._get("artist")

    @property
    def media_album_name(self):
        return self._get("album")

    @property
    def media_duration(self):
        return self._get("duration")

    @property
    def media_image_url(self):
        cover_id = self._get("coverArt")

        if not cover_id:
            return None

        salt, token = self.coordinator.api._generate_token()

        return (
            f"{self.coordinator.api.base_url}/rest/getCoverArt.view"
            f"?id={cover_id}"
            f"&u={self.coordinator.api.username}"
            f"&t={token}"
            f"&s={salt}"
            f"&v=1.16.1"
            f"&c=homeassistant"
        )

    @property
    def entity_picture(self):
        return self.media_image_url

    @property
    def extra_state_attributes(self):
        track = self._get_current_track()

        if not track:
            return {}

        attrs = {
            "track_number": track.get("track"),
            "year": track.get("year"),
            "genre": track.get("genre"),
            "path": track.get("path"),
        }

        return {k: v for k, v in attrs.items() if v is not None}