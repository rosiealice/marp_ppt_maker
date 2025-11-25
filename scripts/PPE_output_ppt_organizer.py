#!/usr/bin/env python3
import numbers
import subprocess

#-------------User Inputs----------------#

# What do you want your ppt file to be called and where do you want it to live?? 
filename='PPE_obs_slides_251125'
output_path='/datalake/NS9560K/www/diagnostics/noresm/rosief/marp_files/'

# Where are the figures you want to organize?
path='https://ns9560k.web.sigma2.no/datalake/diagnostics/noresm/masan/PPE/ppe_runs_landonly/ensemble_member.'

# Which directory are they in? 
subdir = 'OBS_comparison/ANN/'

# List of suffixes (in this case the members of the PPE) over which we want to loop
ppe_numbers=['000','003','005','009','019','021','024','030','032','039','041','042','048','058','059','064','065','069','072','073']

# Which variables do we want to look at? (these are fragments of the names of the files)
VARS = ['LAI_MODIS',
    'FATES_GPP_FLUXCOM',
    'EFLX_LH_TOT_FLUXCOM',
    'QRUNOFF_CLASS',
    'FATES_BURNFRAC_GFED',
    'FSR_GEWEX.SRB',
    'H2OSNO_CanSISE',
    'TSA_CRU4.07'
    ]


#---------End of user inputs --------------#

DIRS = [f"{path}{num}/{subdir}" for num in ppe_numbers]
COMMENTS = [f"Ens# {num}" for num in ppe_numbers]

OUTPUT_MD   = '../outputs/'+filename+'.md'
OUTPUT_PPTX = output_path+filename+'.pptx'

cmd = [
    'python3', 'generate_marp_from_directories.py',
    '--dirs', *DIRS,
    '--vars', *VARS,
    '--comments', *COMMENTS,
    '--output', OUTPUT_MD,
    '--pptx', OUTPUT_PPTX
]

print("Running...")
subprocess.run(cmd)

print("Done with making ppt!")


