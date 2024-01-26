install.packages("ggplot2")
library(ggplot2)

csv_files <- c("mean and SEM-YY1 293T.csv","mean and SEM-H3K4me3 293T.csv")  
line_colors <- c("#bb2927","#246397")



all_data <- data.frame()


for (i in seq_along(csv_files)) {
  csv_file <- csv_files[i]
  file_path <- paste0("D:/LAB-209/YY1/PAPER/bioinformatics/data-set/recombination rate vs peak distance +-5000/mean and SEM/", csv_file)  # 替换为实际的文件夹路径
  current_data <- read.csv(file_path)
  current_data$line_color <- line_colors[i]  
  all_data <- rbind(all_data, current_data)
}

plot <- ggplot(all_data, aes(x = x, y = y, group = NULL, color = line_color)) +
  geom_line() +
  geom_ribbon(aes(ymin = y - sd, ymax = y + sd), alpha = 0.3) +
  labs(title = "plot",
       x = "x",
       y = "y") +
  scale_color_manual(values = line_colors)


print(plot)

