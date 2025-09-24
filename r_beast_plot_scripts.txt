###SCRIPTS FOR R PLOTTING

acuto.data <- read.table('acuto_finals.tsv', header = TRUE);
gordius.data <- read.table('gordius_final.tsv', header = TRUE);
japan.data <- read.table('japan_final.tsv', header = TRUE);
taiwan.data <- read.table('taiwan_final.tsv', header = TRUE);
pdf(file="figure3.pdf")
par(mfrow=c(2,2))
plot(taiwan.data$Time,taiwan.data$Median,col='red',type='l',xlab='Time (years ago)', ylab='Effective population size', main = 'Estimated demographic history');
plot(japan.data$Time,japan.data$Median,col='blue',type='l',xlab='Time (years ago)', ylab='Effective population size', main = 'Estimated demographic history');
plot(acuto.data$Time,acuto.data$Median,col='green',type='l',xlab='Time (years ago)', ylab='Effective population size', main = 'Estimated demographic history');
plot(gordius.data$Time,gordius.data$Median,col='black',type='l',xlab='Time (years ago)', ylab='Effective population size', main = 'Estimated demographic history');
dev.off()
