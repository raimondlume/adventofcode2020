#!/usr/bin/env sh

if [ -z "$1" ]
  then
    echo "❌ No day number given as an argument, exiting..."
    exit 1
fi

if [ -z "$AOC_TOKEN" ]
  then
    echo "❌ No AOC authentication cookie found as \$AOC_TOKEN, exiting..."
    exit 1
fi

echo "Fetching input for AOC day $1...\n"

# create day folder if it does not exist
mkdir -p ./"$1"

# download input with cookie from $AOC_TOKEN global variable
curl --cookie "$AOC_TOKEN" "https://adventofcode.com/2020/day/$1/input" -o "./$1/input.txt"

echo "\n✔️Input saved as ./$1/input.txt!"
exit 0