#! /usr/bin/expect
spawn ssh root@192.168.0.2

expect "#"
send "reuwsgi\r"

expect "#"
send "exit\r"
