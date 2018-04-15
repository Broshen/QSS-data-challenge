cat yelp.json | ./jq -c -M '.[]' | split -l 50000 - ./parts/; 
sed -e 's/$/,/' -i ./parts/*
sed -e '1s/^/[/' -i ./parts/*
sed -e '$ s/.$//' -i ./parts/*
sed -e "\$a]" -i ./parts/*