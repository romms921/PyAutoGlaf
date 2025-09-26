#!/usr/bin/env python
import glafic
from tqdm import tqdm  # Import tqdm for the progress bar
# Wrap initialization and configuration steps in tqdm
with tqdm(total=100, desc="Initializing and Configuring") as pbar:
    glafic.init(0.3, 0.7, -1.0, 0.7, '/Users/ainsleylewis/Documents/Astronomy/Lensing_Py/lens_models/Fresh Models/PRPF', -3.5, -3.5, 3.5, 3.5, 0.01, 0.01, 1, verb=0)
    pbar.update(10)  # Progress update
    glafic.set_secondary('chi2_splane 0', verb=0)
    glafic.set_secondary('chi2_checknimg 0', verb=0)
    glafic.set_secondary('chi2_restart -1', verb=0)
    glafic.set_secondary('chi2_usemag 0', verb=0)
    glafic.set_secondary('hvary 0', verb=0)
    glafic.set_secondary('ran_seed -122000', verb=0)
    pbar.update(20)  # Progress update
    glafic.startup_setnum(2, 0, 1)
    glafic.set_lens(1, 'pow', 0.2300,  7.770000e-01,  3.197980e-03, -5.702846e-03,  4.731000e-01, -3.611298e+01,  1.383255e+00,  1.9)
    glafic.set_lens(2, 'pert',0.2300,  7.770000e-01, 0.0,  0.0,  0.03, -3.298301e+01,  0.000000e+00,  0.0)
    glafic.set_point(1, 0.777, -2.347666e-01, -9.181065e-02)
    pbar.update(30)  # Progress update
    glafic.setopt_lens(1, 0, 0, 1, 1, 1, 1, 1, 1)
    glafic.setopt_lens(2, 0, 0, 0, 0, 1, 1, 0, 0)
    glafic.setopt_point(1, 0, 1, 1)
    pbar.update(40)  # Progress update
    # model_init needs to be done again whenever model parameters are changed
    glafic.model_init(verb=0)
    pbar.update(50)  # Progress update
# Wrap optimization and output steps in tqdm
with tqdm(total=100, desc="Optimization and Output") as pbar:
    glafic.readobs_point('/Users/ainsleylewis/Documents/Astronomy/Lensing_Py/lens_models/obs_point_SIE(POS+FLUX).dat')
    glafic.parprior('/Users/ainsleylewis/Documents/Astronomy/Lensing_Py/lens_models/priorfile.dat')
    glafic.optimize()
    glafic.findimg()
    glafic.writecrit(0.777)
    glafic.writelens(0.777)
    pbar.update(100)  # Complete progress
glafic.quit()