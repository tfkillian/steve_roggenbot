# ---------------
# Script: create_csv.R
# Description:
#   Reads all *.jpg files from a given directory, 
#   strips out the path, prepends "images/" to the file name, 
#   and creates a CSV with columns: image_path, tweet, posting_status.
# ---------------

# 1. Specify your directory path containing the *.jpg files
dir_path <- "path/to/your/images"
#dir_path <- "~/Pictures/lemurian_propaganda/"

# 2. List all .jpg files (note: pattern = "\\.jpg$" ensures we only match .jpg)
all_jpg_files <- list.files(dir_path, pattern = "\\.jpg$", full.names = TRUE)

# 3. Remove the directory path from the file names
file_names <- basename(all_jpg_files)

# 4. Prepend "images/" to each file name
image_path_list <- paste0("images/", file_names)

# 5. Create a dataframe with three columns:
#    image_path, tweet, and posting_status (both tweet and posting_status are blank)
df <- data.frame(
  image_path = image_path_list,
  tweet = "",
  posting_status = "",
  stringsAsFactors = FALSE
)
# View(df)

# 6. Save the resulting dataframe as new_tweet_list.csv
write.csv(df, "new_tweet_list.csv", row.names = FALSE)