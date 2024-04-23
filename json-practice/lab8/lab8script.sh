#!/bin/bash

url="https://aviationweather.gov/api/data/metar?ids=KMCI&format=json&taf=false&hours=12&bbox=40%2C-90%2C45%2C-85"

IFS=$'\n'
receipt_times=$(curl -s "$url" | jq -r ' .[] | .receiptTime')

count=0
for time in $receipt_times; do
    echo "\"$time\""
    ((count++))
    if [ $count -ge 6 ]; then
        break
    fi
done

