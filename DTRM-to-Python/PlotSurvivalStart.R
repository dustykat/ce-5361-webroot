# R script to process particle position file and plot
# starting positions of particles that survive to the outlet
rm(list=ls()) # deallocate workspace
zz <- read.table(file="PARTICLE-POSITIONS.TXT",header=TRUE)
attach(zz)
pdf(file="WATERSHED-PLOT.pdf")
upperBound <- max(XPS,YPS)
plot(XPS,YPS,type="p",pch=3,col="red",cex=0.5,xlim=c(0,upperBound),ylim=c(0,upperBound),xlab="METERS (EASTING)",ylab="METERS (NORTHING)")
# build a subset of vectors that have attribute ALIVE=1.0
HowMany = length(XPS)
xalive <- numeric(0)
yalive <- numeric(0)
talive <- numeric(0)
index <- 1
for (i in 1:HowMany){
 if (ALIVE[i]==1.0){
  xalive[index]<-XPS[i];
  yalive[index]<-YPS[i];
  talive[index]<-TP[i];
  index <- index+1
 }
}
lines(xalive,yalive,type="p",col="blue",pch=19,cex=0.3)
lines(XP[1],YP[1],type="p",col="black",pch=19,cex=3.0)
#
dev.off()
pdf(file="WATERSHED-HISTOGRAMS.pdf")
par(mfrow=c(2,2))
hist(TP/60,breaks=300,freq=TRUE,ylim=c(0,1000),xlab="ARRIVAL TIME (MINUTES)",ylab="COUNTS",main="Arrival Time All Particles");
hist(talive/60,breaks=300,freq=TRUE,ylim=c(0,1000),xlab="ARRIVAL TIME (MINUTES)",ylab="COUNTS",main="Arrival Time Alive Particles");
hist(TP/60,breaks=300,freq=FALSE,ylim=c(0,0.02),xlab="ARRIVAL TIME (MINUTES)",ylab="REL. FREQUENCY",main="Arrival Time All Particles");
hist(talive/60,breaks=300,freq=FALSE,ylim=c(0,0.02),xlab="ARRIVAL TIME (MINUTES)",ylab="REL FREQUENCY",main="Arrival Time Alive Particles");
dev.off()
runoff_coefficient <- sum(ALIVE)/HowMany
outfile <- file("WATERSHED-SUMMARY.txt","w")
write(paste("Total Particles = ",length(TP)),outfile,sep=",")
write(paste("Alive Particles = ",length(talive)),outfile,sep=",")
write(paste("Runoff Coefficient = ",runoff_coefficient),outfile,sep=",")
write(paste("Mean Arrival Time Total =",mean(TP)/60),outfile,sep=",")
write(paste("Mean Arrival Time Lossy =",mean(talive)/60),outfile,sep=",")
#(t.test(TP,talive))
#(wilcox.test(TP,talive))
close(outfile)
#detach(zz)
##########
time2peakAll <- sort(TP)
HowManyTimes <- length(time2peakAll)
HowBigTime <- max(time2peakAll)
HowManyBins <- 300
HowBigBin <- HowBigTime/HowManyBins
BinCounts <- rep(0,HowManyBins)
BinMedian <- rep(0,HowManyBins)
BinCumulative <- rep(0,HowManyBins)
for (j in 1:HowManyBins){
  lowerValue <- (j-1)*HowBigBin
  upperValue <- lowerValue + HowBigBin
  BinMedian[j] <- upperValue
  for (i in 1:HowManyTimes){
    if ((time2peakAll[i] >= lowerValue )&(time2peakAll[i] <= upperValue) ){
          BinCounts[j]<-BinCounts[j]+1
          }
  }
}
BinCumulative[1]<-BinCounts[1]
for (j in 2:HowManyBins){
  BinCumulative[j] <- BinCounts[j]+BinCumulative[j-1]
}

time2peakS <- sort(talive)
HowManyTimes <- length(time2peakS)
HowBigTimeS <- max(time2peakS)
HowManyBins <- 300
HowBigBinS <- HowBigTimeS/HowManyBins
BinCountsS <- rep(0,HowManyBins)
BinMedianS <- rep(0,HowManyBins)
BinCumulativeS <- rep(0,HowManyBins)
for (j in 1:HowManyBins){
  lowerValue <- (j-1)*HowBigBinS
  upperValue <- lowerValue + HowBigBinS
  BinMedianS[j] <- upperValue
  for (i in 1:HowManyTimes){
    if ((time2peakS[i] >= lowerValue )&(time2peakS[i] <= upperValue) ){
      BinCountsS[j]<-BinCountsS[j]+1
    }
  }
}
BinCumulativeS[1]<-BinCountsS[1]
for (j in 2:HowManyBins){
  BinCumulativeS[j] <- BinCountsS[j]+BinCumulativeS[j-1]
}
maxBinCum <- max(BinCumulative)
maxBinCumS <- max(BinCumulativeS)
maxBinCount <- max(BinCounts)
maxBinCountS <- max(BinCountsS)
plot(BinMedian/60,BinCumulative/maxBinCum,type="s",xlab="ARRIVAL TIME (MINUTES)",ylab="REL./CUM. FREQUENCY")
lines(BinMedianS/60,BinCumulativeS/maxBinCum,type="s",col="blue")
lines(BinMedian/60,BinCounts/maxBinCount,type="s",col="black")
lines(BinMedianS/60,BinCountsS/maxBinCount,type="s",col="blue")
