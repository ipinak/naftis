#!/bin/sh

# Create log directory
mkdir /var/tmp/supervisor

# Clone the repository from github
git clone "https://github.com/ipinak/naftis.git" naftis

# Start the application using the supervisor, so it never stops
supervisor -c /naftis/src/supervisord.conf
