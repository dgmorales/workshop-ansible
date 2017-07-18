#!/bin/sh

# Populate /etc/hosts
cat >> /etc/hosts <<EOF
192.168.100.11 m1.local m1
192.168.100.12 m2.local m2
192.168.100.13 m3.local m3
EOF
