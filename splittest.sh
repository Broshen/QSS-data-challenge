cat yelpHeld.json | ./jq -c -M '.[]' | split -l 50000 - ./test/; 
sed -e 's/$/,/' -i ./test/*
sed -e '1s/^/[/' -i ./test/*
sed -e '$ s/.$//' -i ./test/*
sed -e "\$a]" -i ./test/*