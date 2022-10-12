find . -name "*.blp" -print0 | while read -d $'\0' file
do
  renamed_file=${file/.blp/.ui}
  blueprint-compiler compile "$file" --output "$renamed_file"
done
