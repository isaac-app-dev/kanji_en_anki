set basePath to do shell script "pwd"
set compoundNumbers to basePath & "/data/compound_input.numbers"
set compoundCSV to basePath & "/data/compound_input.csv"
tell application "Numbers"
  open POSIX file compoundNumbers
  delay 10
  tell document 1
    export to POSIX file compoundCSV as CSV
  end tell
  close document 1 saving no
end tell