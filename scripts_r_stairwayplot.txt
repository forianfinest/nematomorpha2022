###SCRIPTS FOR GENERATING R PLOT

chordo.data <- read.table('chordodes.final.summary', header = TRUE);
pdf(file="figure.pdf")
plot(chordo.data$year,chordo.data$Ne_median,col='black',type='l',xlim=c(0,3285819), ylim=c(381.3709,8443256), xlab='Time (years ago)', ylab='Effective population size', main = 'C. formosanus's demographic history');
points(chordo.data$year,chordo.data$Ne_97.5, ylim=c(0,8443256), col='red',type='l',lty=1);
points(chordo.data$year,chordo.data$Ne_2.5, ylim=c(41.66966,1981582), col='red',type='l',lty=1);
dev.off()
