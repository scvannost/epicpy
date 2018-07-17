# epicpy
A python wrapper for the EPIC cell type-identifying R library

Original EPIC sofware: https://github.com/GfellerLab/EPIC

Paper: https://doi.org/10.7554/eLife.26476.001

Only the python file is necessary, as it will generate the R file if it does not exist. 

I am not in any way affiliated with the Gfeller lab or Ludwig Institute for Cancer Research Ltd, nor claim any ownership of EPIC nor license on this wrapper beyond what is required. Commercial users are requested to obtain a license from the developers of EPIC.

## Instructions
```python
from epic import epic
fname = 'test.txt'
results = epic(fname[,sep])
```

'test.txt' must be a delimited file readable by pandas.read_csv, with gene symbols in the first column and sample names in the first row. Do not include multiple gene names or it will throw and error. The optional parameter `sep` is passed to pandas.read_csv to read the file.

Returns a pandas.DataFrame() with the samples as the index and the cell types as the columns.

Possible errors thrown are: `FileNotFound` if 'test.txt' does not exist; `ValueError` if there are repeated gene names; or a generic `Exception` if there was an error in the R processing.

epicpy requires console access, as it calls `Rscript` from the shell. Additionally, it needs write access to the folder it's in.

Note that epicpy writes over the file if `sep` is not `\t` to make it a tab-delimited file for processing, then writes over it again with the given `sep` to return the original file. Therefore, a tab-delimited file will run faster than any other separator due to avoiding two I/O steps. I could make this use another temp file, but that doesn't change the speed. I should pass `sep` to epic.R and handle the separator there as to avoid this issue.

Note that epicpy creates/writes and deletes the file `temp.txt` in the folder it acts in. It should use a better temp filename.

Feature creation by request.
