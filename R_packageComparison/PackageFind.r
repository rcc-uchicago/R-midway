rpack = as.data.frame(installed.packages()[,c(3:4)])
rpack = rpack[is.na(rpack$Priority),0:1,drop=FALSE]
write.csv(rpack,file="output.csv")