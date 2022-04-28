echo "build tests"
go test -c ./gotests -o tests

echo "get binary size"
out=$(ls -l tests | awk '{print $5}' | tr -d '\n')

echo "Adding metrics $out B"
python3 .buildkite/custom_tags.py metrics job "binary.size:$out"