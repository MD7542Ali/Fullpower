#!/bin/bash

BOT_COMMAND="python3 p.py" LOG_FILE="bot_restart.log"

while true; do echo "[INFO] Starting bot..." | tee -a "$LOG_FILE" nohup $BOT_COMMAND >> "$LOG_FILE" 2>&1 & BOT_PID=$! wait $BOT_PID echo "[WARNING] Bot stopped! Restarting in 5 seconds..." | tee -a "$LOG_FILE" sleep 5 done

)