import glafic

glafic.init(0.3, 0.7, -1.0, 0.7, 'Test/POW+SHEAR', -3.5, -3.5, 3.5, 3.5, 0.01, 0.01, 1.0, verb=0)

glafic.set_secondary('chi2_splane 0.0', verb=0)
glafic.set_secondary('chi2_checknimg 0', verb=0)
glafic.set_secondary('chi2_restart -1', verb=0)
glafic.set_secondary('chi2_usemag 0', verb=0)
glafic.set_secondary('hvary 0', verb=0)
glafic.set_secondary('ran_seed -122000', verb=0)

glafic.startup_setnum(2, 0, 1)
glafic.set_lens(1, 'pow', 0.2300, 7.770000e-01, 3.197980e-03, -5.702846e-03, 4.731000e-01, -3.611298e+01, 1.383255e+00, 1.9)
glafic.set_optlens(1, 0, 0, 0, 0, 0, 0, 0, 0)

glafic.set_lens(2, 'shear', 0.2300, 7.770000e-01, 0.0, 0.0, 0.03, -3.298301e+01, 0.000000e+00, 0.0)
glafic.set_optlens(2, 0, 0, 0, 0, 0, 0, 0, 0)

glafic.set_point(1, 0.777, -2.347666e-01, -9.181065e-02)
glafic.set_optpoint(1, 0, 0, 0)

glafic.model_init(verb=0)

glafic.optimize()
glafic.findimg()
glafic.write_crit(0.777)
glafic.write_lens(0.777)

glafic.quit()
