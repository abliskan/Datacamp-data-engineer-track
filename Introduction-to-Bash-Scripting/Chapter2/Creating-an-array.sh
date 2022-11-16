# Create a normal array with the mentioned elements
capital_cities=("Sydney", "Albany", "Paris")
# --------------------------
# Create a normal array with the mentioned elements using the declare method
declare -a capital_cities
# Add (append) the elements
capital_cities+=("Sydney")
capital_cities+=("Albany")
capital_cities+=("Paris")
# --------------------------
# The array has been created for you
capital_cities=("Sydney" "Albany" "Paris")
# Print out the entire array
echo ${capital_cities[@]}
# Print out the array length
echo ${#capital_cities[@]}