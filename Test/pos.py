import glafic

glafic.init(0.3, 0.7, -1.0, 0.7, '/Users/ainsleylewis/Documents/Astronomy/Lensing_Py/WFI2026/pow_models/POW+SHEAR', -3.5, -3.5, 3.5, 3.5, 0.01, 0.01, 1, verb = 0)

glafic.set_secondary('chi2_splane 1', verb = 0)
glafic.set_secondary('chi2_checknimg 0', verb = 0)
glafic.set_secondary('chi2_restart   -1', verb = 0)
glafic.set_secondary('chi2_usemag    0', verb = 0)
glafic.set_secondary('hvary          0', verb = 0)
glafic.set_secondary('ran_seed -122000', verb = 0)

glafic.startup_setnum(2, 0, 1)
glafic.set_lens(1, 'pow', 1.0400, 2.230000e+00, -4.883297e-02, 2.788928e-02, 2.999980e-01, 80.0, 6.681184e-01, 1.900001e+00)
glafic.set_lens(2, 'pert', 1.0400, 2.230000e+00, 0.0, 0.0, 0.01, -40.0, 0.0, 0.0)
glafic.set_point(1, 2.2300, -1.599974e-02, 1.195229e-01)

glafic.setopt_lens(1, 0, 0, 1, 1, 1, 1, 1, 1)
glafic.setopt_lens(2, 0, 0, 0, 0, 1, 1, 0, 0)
glafic.setopt_point(1, 0, 1, 1)

# model_init needs to be done again whenever model parameters are changed
glafic.model_init(verb = 0)

glafic.readobs_point('/Users/ainsleylewis/Documents/Astronomy/Lensing_Py/WFI2026/obs_point.dat')
glafic.parprior('/Users/ainsleylewis/Documents/Astronomy/Lensing_Py/WFI2026/prior.dat')
glafic.optimize()
glafic.findimg()
glafic.writecrit(2.2300)
glafic.writelens(2.2300)
glafic.quit()