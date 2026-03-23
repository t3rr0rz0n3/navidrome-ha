[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![Downloads][download-latest-shield]](https://github.com/t3rr0rz0n3/navidrome-ha/releases)
[![License][license-shield]](LICENSE)
[![hacs][hacsbadge]][hacs]

<img width="606" height="611" alt="imatge" src="https://github.com/user-attachments/assets/1300247a-34fd-4765-868c-e311b64fd37b" />

# Navidrome Home Assistant Integration

A custom Home Assistant integration to connect your Navidrome server using the Subsonic API.

This integration provides real-time information about your music server, including currently playing tracks, library statistics, and server status.

## 🌍 Languages

- English (this file)
- [Español](docs/README.es.md)
- [Català](docs/README.ca.md)

Want to translate this integration into your language? Check the [translation guide](docs/translate.md)

---

## 📦 Installation (via HACS)

1. Open HACS in Home Assistant
2. Go to **Integrations**
3. Click the three dots → **Custom repositories**
4. Add: https://github.com/t3rr0rz0n3/navidrome-ha
5. Select category: **Integration**
6. Install the integration
7. Restart Home Assistant

---

## ⚙️ Configuration

1. Go to **Settings → Devices & Services**
2. Click **Add Integration**
3. Search for **Navidrome**
4. Enter:
   - Server URL
   - Username
   - Password

---

## ✨ Features

- Media player with Now Playing information
- Trigger library scan from Home Assistant
- Library statistics:
  - Total songs
  - Total artists
  - Total genres
- Current playback sensors:
  - Current song
  - Current artist
  - Current album
- Last library scan (with relative time)
- Multi-language support (EN, ES, CA)
- Config flow support (UI setup)

---

## 📸 Screenshots

<img width="1056" height="822" alt="imatge" src="https://github.com/user-attachments/assets/edaa6c53-a85f-4706-8b7e-0cc470f051ff" />
<img width="1100" height="783" alt="imatge" src="https://github.com/user-attachments/assets/36106afb-5a76-4931-8ff7-c6db8aba6f0f" />
<img width="787" height="547" alt="imatge" src="https://github.com/user-attachments/assets/012ece4c-a5b8-47c2-8a47-257fd553dd43" />

---

## 📄 License

GPL-3.0

[releases-shield]: https://img.shields.io/github/release/t3rr0rz0n3/navidrome-ha.svg?style=for-the-badge
[releases]: https://github.com/t3rr0rz0n3/navidrome-ha/releases
[commits-shield]: https://img.shields.io/github/commit-activity/m/t3rr0rz0n3/navidrome-ha.svg?style=for-the-badge
[commits]: https://github.com/t3rr0rz0n3/navidrome-ha/commits/main
[download-latest-shield]: https://img.shields.io/github/downloads/t3rr0rz0n3/navidrome-ha/latest/total?style=for-the-badge
[license-shield]: https://img.shields.io/github/license/t3rr0rz0n3/navidrome-ha.svg?style=for-the-badge
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[hacs]: https://github.com/hacs/integration
