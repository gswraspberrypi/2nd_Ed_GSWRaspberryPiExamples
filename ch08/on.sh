#!/bin/bash
echo Exporting pin $1. 
echo $1 > /sys/class/gpio/export
echo Setting direction to out.
echo out > /sys/class/gpio/gpio$1/direction
echo Setting pin high.
echo 1 > /sys/class/gpio/gpio$1/value