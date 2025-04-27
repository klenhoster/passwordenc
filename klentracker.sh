#!/bin/bash

# Replace with your actual Numverify API Key
API_KEY="4da6e7cae151cdd0aa27ba570d1c6ce7"

# Displaying the Klentracker Header
echo "===================================="
echo "       Welcome to Klentracker       "
echo "===================================="

# Ask user for phone number
read -p "Enter phone number (with country code, e.g. +14155552671): " phone

# Send request to Numverify API and get the response
response=$(curl -s "http://apilayer.net/api/validate?access_key=$API_KEY&number=$phone&country_code=&format=1")

# Extract relevant information from the response
valid=$(echo "$response" | jq '.valid')
country=$(echo "$response" | jq -r '.country_name')
carrier=$(echo "$response" | jq -r '.carrier')
line_type=$(echo "$response" | jq -r '.line_type')

# Display results
if [ "$valid" = "true" ]; then
    echo "✅ Phone Number is Valid!"
    echo "🌎 Country: $country"
    echo "📡 Carrier: $carrier"
    echo "📞 Line Type: $line_type"
else
    echo "❌ Invalid Phone Number"
fi
