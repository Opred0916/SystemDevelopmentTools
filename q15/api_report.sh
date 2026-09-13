#!/bin/bash

JQ="/c/Users/opred/AppData/Local/Microsoft/WinGet/Packages/jqlang.jq_Microsoft.Winget.Source_8wekyb3d8bbwe/jq.exe"

curl -fsS http://127.0.0.1:8000/packages.json |
"$JQ" -r '
  map(select(.status == "active" and .downloads >= 100))
  | sort_by(-.downloads, .name)
  | ["# Package Summary", "", "| name | version | downloads |", "|---|---|---:|"]
    + map("| \(.name) | \(.version) | \(.downloads) |")
  | .[]
' > summary.md