#!/bin/bash
# Where tiles are:
input_dir="$HOME/repository_local/FFT-from-image-compute-radial-intensity/INPUT/carK_tiles_original/Montage_833"
output_dir="./results"
# command input parameters.
lam=0.05
for file in ${input_dir}/*tile*; do
    echo file: "$file"
    # remove suffix
    base_name=${file%.*}
    # remove dir
    base_name=$(basename $base_name)
    out_name="${output_dir}/${base_name}_lam${lam}"
    python $HOME/repository_local/total_variation/demo_saxstem/demo_saxstem.py \
        -i "$file" \
        -l $lam \
        -o "${out_name}.png"
done;
