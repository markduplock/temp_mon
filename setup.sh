#!/bin/bash

echo "[+] Creating log directory..."
mkdir -p /mnt/data/logs
touch /mnt/data/logs/temp_log.txt
chmod 644 /mnt/data/logs/temp_log.txt

echo "[+] Copying service to systemd..."
sudo cp temp_mon.service /etc/systemd/system/

echo "[+] Reloading systemd..."
sudo systemctl daemon-reload

echo "[+] Enabling temp_mon service..."
sudo systemctl enable temp_mon

echo "[+] Starting temp_mon service..."
sudo systemctl start temp_mon

echo "[✓] Done. Check status with: sudo systemctl status temp_mon"
