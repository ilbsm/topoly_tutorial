#!/bin/bash
wget https://knotprot.cent.uw.edu.pl/chains/1j85/A/chain.xyz.txt -P /tmp
knotnet /tmp/chain.xyz.txt -c 2 -t 2
