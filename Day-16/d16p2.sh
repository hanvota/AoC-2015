#!/bin/bash

grep -v "children: [^3]" Day-16-data.txt | grep -v "cats: [01234567]" | grep -v "samoyeds: [^2]" | grep -v "pomeranians: \([3456789]\|10\)" | grep -v "akitas: [^0]" | grep -v "vizslas: [^0]" | grep -v "goldfish: \([56789]\|10\)" | grep -v "trees: [0123]" | grep -v "cars: [^2]" | grep -v "perfumes: [^1]"
