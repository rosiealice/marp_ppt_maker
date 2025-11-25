#!/usr/bin/env python3
import numbers
import subprocess


# User settings
filename='PPE_obs_slides_251125'
run='obs'  # 'hist' or ' obs' or 'seasonal'
type='main obs' # for the seasonal runs

path='https://ns9560k.web.sigma2.no/datalake/diagnostics/noresm/masan/PPE/ppe_runs_landonly/ensemble_member.'
subdir = 'OBS_comparison/ANN/'

ppe_numbers=['000','003','005','009','019','021','024','030','032','039','041','042','048','058','059','064','065','069','072','073']

DIRS = [f"{path}{num}/{subdir}" for num in ppe_numbers]
COMMENTS = [f"Ens #:{num}" for num in ppe_numbers]   

VARS = ['LAI_MODIS',
    'FATES_GPP_FLUXCOM',
    'EFLX_LH_TOT_FLUXCOM',
    'VEGC_ESACCI',
    'FATES_BURNFRAC_GFED',
    'FSR_GEWEX.SRB',
    'H2OSNO_CanSISE',
    'TSA_CRU4.07'
    ]

output_path='/datalake/NS9560K/www/diagnostics/noresm/rosief/marp_files/'

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


