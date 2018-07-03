p <- .packages(all.available = TRUE)
if (!("EPIC" %in% p)) {
  if (!("devtools" %in% p)) {
    install.packages("devtools")
  }
  devtools::install_github("GfellerLab/EPIC")
}
rm(p)

library("EPIC")

# python handler checks for proper input of arguments
myArgs <- commandArgs(trailingOnly = TRUE)

mydata <- read.table(myArgs[1], row.names=1, header=TRUE)

tryCatch(
  {
    out <- EPIC(mydata)
    write.table(out$cellFractions, myArgs[2], sep="	")
  },
  error = function(e) {
    return(paste("Error:",e))
  }
)