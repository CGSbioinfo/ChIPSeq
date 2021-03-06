# ChIPSeq
ChIPSeq pipeline

Software required:
Trimgalore, FASTQC, BWA, bamtools, PICARD tools, MACS2.

The python main script calls other scripts, make sure they are available from 
the $PATH: functions.py, analysis_info.py, organizeWorkingDirectory.py, qcReads.py, 
trimmingReads.py, fastqc_tables_all.py, mappingReads.py, peak_calling.py.


# Download and Install
----------------------
 $ git clone https://github.com/CGSbioinfo/ChIPSeq.git

 $ cd ChIPSeq/scripts
 $ for i in $(ls *py); do cp $i /usr/local/bin; done # NEED SUDO!!
 $ for i in $(ls *py); do chmod 777 /usr/local/bin/$i ; done # NEED SUDO!
 $ cp junctionPlotAll.R ~/bin 

##------------------------------------------------------------------------------##

# Running the pipeline

Setting up the analysis
-----------------------
1.	Go to the main folder of the project and run:
    		$ analysis_info.py
This will create a file named analysis_info.txt, which needs to be filled in a text editor.
2.	Create a sample_names.txt file with the list of the sample names
3.	Next run:
    		$ organizeWorkingDirectory.py --analysis_info_file analysis_info.txt

4. List of arguments to fill in the parameter file:

* Working directory: base directory 
* Reference genome: path to the reference genome directory
* sample_peak_calling: file defining the control and treatment match up, first column should be treatment and the second one * * control, tab delimited
* Number of samples: how many sample to analyse
* genome size: argument for macs 2, for known organisms can use abrevation (hs=human, mm=mouse)
* name of the experiment: name for the experiment
* fragment size: expected fragment size
* tag length: read length
* read_format: read format, if single end read, use 'auto', for pair end use 'BAMPE' (need to be bam format)
* peak_out_file_name: suffix for peak call file to be added to the sample name
* fdr cut off: Cut off for FDR after peak calling
* broad: TRUE/FALSE, do broad peak calling
* broadCutOff: fdr cut off for broad peaks.



QC and trimming
---------------
Run the following commands:
  $ qcReads.py --in_dir rawReads/ --out_dir rawReads/
  $ fastqc_tables_all.py --in_dir rawReads/ --out_dir rawReads/  
  $ trimmingReads.py --in_dir rawReads/ --out_dir trimmedReads/
  $ fastqc_tables_all.py --in_dir trimmedReads/ --out_dir trimmedReads/  

Mapping and mapping QC
----------------------
Run the following commands:
  $ mappingReads.py --in_dir trimmedReads/ --out_dir alignedReads/
  Note: mapping QC integrated in the mapping step.

Peak calling
--------------
Run the following commands:
  $ peak_calling.py --in_dir alignedReads/ --out_dir alignedReads/ 
