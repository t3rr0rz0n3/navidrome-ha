from datetime import timedelta
import logging

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import DEFAULT_SCAN_INTERVAL


_LOGGER = logging.getLogger(__name__)


class NavidromeCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, api):
        super().__init__(
            hass,
            _LOGGER,
            name="navidrome",
            update_interval=timedelta(seconds=DEFAULT_SCAN_INTERVAL),
        )
        self.api = api

    async def _async_update_data(self):
        try:
            now_playing = await self.hass.async_add_executor_job(
                self.api.get_now_playing
            )

            scan_status = await self.hass.async_add_executor_job(
                self.api.get_scan_status
            )

            system = await self.hass.async_add_executor_job(
                self.api.get_system_info
            )

            genres = await self.hass.async_add_executor_job(
                self.api.get_genres
            )

            artists = await self.hass.async_add_executor_job(
                self.api.get_artists
            )

            playlists = await self.hass.async_add_executor_job(
                self.api.get_playlists
            )

            return {
                "now_playing": now_playing,
                "scan_status": scan_status,
                "system": system,
                "genres": genres,
                "artists": artists,
                "playlists": playlists,
            }

        except Exception as err:
            raise UpdateFailed(f"Error fetching Navidrome data: {err}")