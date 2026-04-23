#!/bin/bash

set -euo pipefail

setup(){
  chmod +x unixfetch
  mv unixfetch /usr/bin/unixfetch
  echo "Your setup is done (+)"
}

setup

