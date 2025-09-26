#!/usr/bin/env python
import glafic

glafic.init(0.3, 0.7, -1.0, 0.7, 'Test/POW+SHEAR', -3.5, -3.5, 3.5, 3.5, 0.01, 0.01, 1, verb=0)

glafic.set_secondary('chi2_splane 1', verb=0)
glafic.set_secondary('chi2_checknimg 0', verb=0)
glafic.set_secondary('chi2_restart -1', verb=0)
glafic.set_secondary('chi2_usemag 0', verb=0)
glafic.set_secondary('hvary 0', verb=0)
glafic.set_secondary('ran_seed -122000', verb=0)

glafic.startup_setnum(2, 0, 1)
glafic.set_lens(1, 'pow', 0.2300,  7.770000e-01,  3.197980e-03, -5.702846e-03,  4.731000e-01, -3.611298e+01,  1.383255e+00,  1.9)
glafic.set_lens(2, 'pert',0.2300,  7.770000e-01, 0.0,  0.0,  0.03, -3.298301e+01,  0.000000e+00,  0.0)
glafic.set_point(1, 0.777, -2.347666e-01, -9.181065e-02)

glafic.setopt_lens(1, 0, 0, 1, 1, 1, 1, 1, 1)
glafic.setopt_lens(2, 0, 0, 0, 0, 1, 1, 0, 0)
glafic.setopt_point(1, 0, 1, 1)
# model_init needs to be done again whenever model parameters are changed
glafic.model_init(verb=0)

glafic.readobs_point('Test/obs_point.dat')
glafic.optimize()
glafic.findimg()
glafic.writecrit(0.777)
glafic.writelens(0.777)

glafic.quit()