# Prototype Plotting Function
plotNow <- function(station,time,flowObs,flowMod){
  XLABEL <- "TIME (MIN)"
  YLABEL <- "DISCHARGE (MM/MIN)"
  plot(time,flowObs*25.4,type="s",col="blue",lwd=3,xlab=XLABEL,ylab=YLABEL,main=station)
  lines(time,flowMod*25.4,type="s",col="red",lwd=3)
  return()
}
##############################################################################
pdf(file="junk.pdf")
##############################################################################
z1 <- read.table(file="iuh4_sta08057435_1976_0530.out.txt",header=TRUE)
# assume it fucks up the reading of RATE_MODEL - use the differencing to fix
attach(z1)
HowMany <- length(ACC_MOD_RUNOFF)
modelFlow <- rep(0,HowMany)
for (i in 2:HowMany){
  modelFlow[i] <- ACC_MOD_RUNOFF[i]-ACC_MOD_RUNOFF[i-1]
}
plotNow("sta08057435_1976_0530",TIME,RATE_RUNOFF,modelFlow)
detach(z1)
##############################################################################
z2 <- read.table(file="iuh4_sta08057435_1977_0327.out.txt",header=TRUE)
# assume it fucks up the reading of RATE_MODEL - use the differencing to fix
attach(z2)
HowMany <- length(ACC_MOD_RUNOFF)
modelFlow <- rep(0,HowMany)
for (i in 2:HowMany){
  modelFlow[i] <- ACC_MOD_RUNOFF[i]-ACC_MOD_RUNOFF[i-1]
}
plotNow("sta08057435_1977_0327",TIME,RATE_RUNOFF,modelFlow)
detach(z2)
##############################################################################
z3 <- read.table(file="iuh4_sta08057435_1979_0501.out.txt",header=TRUE)
# assume it fucks up the reading of RATE_MODEL - use the differencing to fix
attach(z3)
HowMany <- length(ACC_MOD_RUNOFF)
modelFlow <- rep(0,HowMany)
for (i in 2:HowMany){
  modelFlow[i] <- ACC_MOD_RUNOFF[i]-ACC_MOD_RUNOFF[i-1]
}
plotNow("sta08057435_1979_0501",TIME,RATE_RUNOFF,modelFlow)
detach(z3)
##############################################################################
z4 <- read.table(file="iuh4_sta08057435_1979_0503.out.txt",header=TRUE)
# assume it fucks up the reading of RATE_MODEL - use the differencing to fix
attach(z4)
HowMany <- length(ACC_MOD_RUNOFF)
modelFlow <- rep(0,HowMany)
for (i in 2:HowMany){
  modelFlow[i] <- ACC_MOD_RUNOFF[i]-ACC_MOD_RUNOFF[i-1]
}
plotNow("sta08057435_1979_0503",TIME,RATE_RUNOFF,modelFlow)
detach(z4)
dev.off()
