# 🌡️ temp_mon

**temp_mon** is a lightweight systemd-enabled Python daemon that monitors the temperature of your Raspberry Pi and logs high readings to an external drive.

Built to be:
- Reliable on reboot ✅  
- Self-restarting on crash ✅  
- Easily deployable via `setup.sh` ✅  
- Friendly for future dashboarding, CLI tools, or alert systems 🚀

---

## 🚀 Features

- Log temperature every 30 seconds
- Logs as INFO if less than `70°C` else logs as WARN
- Writes to `/mnt/data/logs/temp_mon.log` on your external SSD
- Designed to run as a systemd service
- Auto-starts on boot, and auto-recovers on failure

---

## 🧱 Folder Structure

```bash
temp_mon/
├── temp_mon.py         # The Python daemon
├── temp_mon.service    # systemd unit file
├── setup.sh            # One-shot installer script
└── README.md           # You're here
```

---

## ⚙️ Requirements

- Raspberry Pi OS Lite (or any Debian-based distro)
- `vcgencmd` tool (usually pre-installed on Pi)
- Python 3
- External SSD or disk mounted at `/mnt/data` with a `logs/` folder

---

## 🛠️ Setup

> Clone the repo to your Pi:

```bash
git clone https://github.com/markduplock/temp_mon.git
cd temp_mon
chmod +x temp_mon.py setup.sh
sudo ./setup.sh
```

This will:
- Create `/mnt/data/logs/temp_mon.log` (if it doesn't exist)
- Copy the systemd service to `/etc/systemd/system/`
- Reload systemd
- Enable and start the `temp_mon` service

---

## ✅ Verifying It Works

```bash
sudo systemctl status temp_mon
tail -f /mnt/data/logs/temp_mon.log
```

You should start seeing entries like:

```
2025-07-17T20:39:48.601167 - temp_mon - INFO - Temp: 60.8°C
```

---

## 🔄 Making Changes

If you change `temp_mon.py`:

```bash
sudo systemctl restart temp_mon
```

---

## 🚧 Roadmap / Ideas

- [ ] Add log rotation
- [ ] Export to CSV or JSON for graphing
- [ ] Alerting system (email, Telegram, etc)
- [ ] Integrate with Flask dashboard
- [ ] Add average/max temp CLI summary tool

---

## 🛡️ License

MIT. Do whatever the hell you want, just don’t sue me.

---

## 🛰️ Naming Convention

In the spirit of *The Expanse*, this repo was born on the Raspberry Pi named `razorback`, monitored by a dev machine named `rocinante`.
