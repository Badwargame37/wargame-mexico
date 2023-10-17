[Unit]
Description=Your Service Description
After=network.target

[Service]
User=root
ExecStart=/path/to/your/script.sh

[Install]
WantedBy=multi-user.target
