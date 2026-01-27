#!/bin/bash

set -euo pipefail

SHELL_TYPE=$(basename $SHELL)
setup(){
  chmod +x unixfetch.sh
  mv unixfetch.sh ~/.local/bin/unixfetch
  echo "(+) Setup is Completed! Now you can use unixfetch!"
}

shell_type(){
  if $SHELL_TYPE == "fish"; then
    echo "set -gx $PATH $HOME/.local/bin $PATH" >> ~/.config/fish/config.fish
    source ~/.config/fish/config.fish
    setup
  else
    setup
  fi
}

if [ ! -f ~/.local/bin ]; then
  mkdir -p ~/.local/bin/
  shell_type
else
  shell_type

