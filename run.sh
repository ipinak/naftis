#!/bin/sh

# Start the application using the supervisor, so it never stops
supervisord -n -c /naftis/supervisord.conf
