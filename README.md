# epicpy
A python wrapper for the EPIC cell type-identifying R library

Since http://epic.gfellerlab.org/ wasn't working for me and I didn't want to deal with R, I wrote a python wrapper for the R library that returns the cell type fractions using the default reference set of EPIC.

Only the python file is necessary, as it will generate the R file if it does not exist. 

I am not in any way affiliated with the Gfeller lab or Ludwig Institute for Cancer Research Ltd, nor claim any ownership of EPIC nor license on this wrapper beyond what is required.

## Instructions
```python
from epic import epic
fname = 'test.txt'
results = epic(fname)
```

'test.txt' must be a tab-separated file, with gene symbols in the first column and sample names in the first row.
There cannot be any duplicate gene symbols.

Returns a pandas.DataFrame() with the samples as the index and the cell types as the columns.

Possible errors thrown are `FileNotFound`, if 'test.txt' does not exist, or a generic `Exception`, if there was an error in the R processing.

epicpy requires console access, as it calls `Rscript` from the shell. Additionally, it needs write access to the folder it's in.
Note that it creates/writes and deletes the file `/temp.txt` in the folder it acts in. It will be updated to use a better filename if I get around to it.

Feature creation by request.
