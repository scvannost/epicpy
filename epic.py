import os, pandas, subprocess

def epic(file:str, sep='\t'):
	if not os.path.isfile(file):
		raise FileNotFoundError('File '+file+' cannot be found.')
	if not os.path.isfile('epic.R'):
		with open('epic.R','w') as f:
			f.write(r_code)

	temp = pandas.read_csv(file,sep=sep,index_col=0)
	if not len(set(temp.index.values)) == len(temp.index.values):
		raise ValueError('You must not have duplicate row (i.e. gene) names.')
	elif sep != '\t':
		with open(file,'w') as f:
			f.write(temp.to_csv(sep='\t'))

	cmd = 'Rscript epic.R ' + file + ' temp.txt'
	err = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout
	if err:
		raise Exception(err.decode().replace('\n','')[12:-3])

	out = pandas.read_csv('temp.txt',sep='\t',header=0,index_col=0)
	os.remove('temp.txt')

	if sep != '\t':
		with open(file,'w') as f:
			f.write(temp.to_csv(sep=sep))

	return out

r_code = '''p <- .packages(all.available = TRUE)
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
    write.table(out$cellFractions, myArgs[2], sep="\t")
  },
  error = function(e) {
    return(paste("Error:",e))
  }
)'''
