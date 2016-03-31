#!/bin/bash -xevu
set -o pipefail
if [[ -e batch ]]; then
  cat batch | xargs -I% git merge %
fi
