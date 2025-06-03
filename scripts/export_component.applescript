set basePath to do shell script "pwd"
set componentNumbers to basePath & "/data/component_input.numbers"
set componentCSV to basePath & "/data/component_input.csv"
tell application "Numbers"
  open POSIX file componentNumbers
  delay 10
  tell document 1
    export to POSIX file componentCSV as CSV
  end tell
  close document 1 saving no
end tell