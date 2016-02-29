__author__ = 'jb393'

import os
import sys
import re
import errno
import glob
import time
import pickle
import logging
from joblib import Parallel, delayed
import multiprocessing
import functions





def callpeaks(i):
    if i in controlDict:
        controlSample=controlDict[i]
        treatedSample=i
        if broad:
            os.system('macs2 callpeak --broad -s='+fragSize+' -broadCutOff '+broadCutOff+' -q' + qCutOff + ' --bw '+fragSize+' -f '+readFormat+' -c '+indir+'/'+controlSample+'Aligned.sortedByCoord.bam -t '+in_dir+'/'+treatedSample+"Aligned.sortedByCoord.dedup.removed.out.bam -g "+genomeSize+" -n "+treatedSample+"_"+controlSample+"_bampe_q_value_filtered_dedup_00001_pval -outdir "+out_dir)
        else:
            os.system('macs2 callpeak -s='+fragSize+' -q' + qCutOff + ' --bw '+fragSize+' -f '+readFormat+' -c '+indir+'/'+controlSample+'Aligned.sortedByCoord.bam -t '+in_dir+'/'+treatedSample+"Aligned.sortedByCoord.dedup.removed.out.bam -g "+genomeSize+" -n "+treatedSample+"_"+controlSample+"_bampe_q_value_filtered_dedup_00001_pval -outdir "+out_dir)



if __name__ == '__main__':

    parser = argparse.ArgumentParser(description = 'Peaking calling with MACS2')
    parser.add_argument('--analysis_info_file', help='Text file with details of the analysis. Default=analysis_info.txt', default='analysis_info.txt')
    parser.add_argument('--in_dir', help='Path to folder containing fastq files. Default=trimmedReads/', default='trimmedReads/')
    parser.add_argument('--out_dir', help='Path to out put folder. Default=alignedReads/', default='alignedReads/')
    args=parser.parse_args()

    params_file=args.analysis_info_file
    path=functions.read_parameters_file(params_file)['Working directory']
    #refGenome=functions.read_parameters_file(params_file)['Reference Genome']
    os.chdir(path)

    # Read sample names text file
    sampleNames = functions.read_sample_names()

    # Set input and output directories if not '/'
    in_dir=args.in_dir
    out_dir=args.out_dir
    readLength=args.read_length
    fragSize = args.fragSize
    readFormat = args.readFormat
    qCutOff = args.qCutoff
    broad = args.broad
    broadCutOff = args.broadCutOff

    functions.make_sure_path_exists(out_dir)
    controlDict={}
    sampleInfo=open(sample_peak_info)
    for sample_matches in sampleInfo:
        sample_matches=sample_matches.strip()
        sampleTab=sample_matches.split("\t")
        controlDict[sampleTab[0]]=sampleTab[1]

    Parallel(n_jobs=4)(delayed(callpeaks)(i) for i in sampleNames)
