#! /usr/bin/bash
cd CryptoLeague 
docker-compose up -d --force-recreate --build
echo README.md

echo
echo

cd ../CryptoLeagueV2
docker-compose up -d --force-recreate --build
echo README.md