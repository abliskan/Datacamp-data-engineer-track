# Create empty associative array
declare -A model_metrics
# Add the key-value pairs
model_metrics[model_accuracy]=98
model_metrics[model_name]="knn"
model_metrics[model_f1]=0.82
# --------------------------
# Declare associative array with key-value pairs on one line
declare -A model_metrics=([model_accuracy]=98 [model_name]="knn" [model_f1]=0.82)
# Print out the entire array
echo ${model_metrics[@]}
# --------------------------
# An associative array has been created for you
declare -A model_metrics=([model_accuracy]=98 [model_name]="knn" [model_f1]=0.82)
# Print out just the keys
echo ${!model_metrics[@]}