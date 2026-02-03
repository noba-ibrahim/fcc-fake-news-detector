#!/bin/bash

# Script de test manuel de l'API
# Usage: bash test_manual.sh

echo "=========================================="
echo "Testing FCC Fake News Detector API"
echo "=========================================="

API_URL="http://localhost:5000"

# Test 1: Health check
echo -e "\n1. Testing health endpoint..."
curl -s ${API_URL}/health | python -m json.tool

# Test 2: Fake news detection
echo -e "\n2. Testing prediction - Fake News..."
curl -s -X POST ${API_URL}/predict \
  -H "Content-Type: application/json" \
  -d '{"text":"SHOCKING: Aliens landed in New York City yesterday!!!"}' \
  | python -m json.tool

# Test 3: Reliable news detection
echo -e "\n3. Testing prediction - Reliable News..."
curl -s -X POST ${API_URL}/predict \
  -H "Content-Type: application/json" \
  -d '{"text":"President announces new economic policy at White House press conference"}' \
  | python -m json.tool

echo -e "\n=========================================="
echo "Tests completed!"
echo "=========================================="
