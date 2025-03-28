#!/bin/bash

# Auto-install Python if missing
if ! command -v python3 &> /dev/null
then
    echo "⚠️ Python not found! Installing..."
    apt update -y && apt install -y python3
fi

# Start the auto-restart script
nohup python3 rona.py > bot.log 2>&1 &
echo "🚀 Bot started!"