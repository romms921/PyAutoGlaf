import glafic

glafic.init(0.3, 0.7, -1.0, 0.7, 'Test/NFW+SHEAR', -3.5, -3.5, 3.5, 3.5, 0.01, 0.01, 1.0, verb=0)

glafic.set_secondary('chi2_splane 0', verb=0)
glafic.set_secondary('chi2_checknimg 0', verb=0)
glafic.set_secondary('chi2_restart -1', verb=0)
glafic.set_secondary('chi2_usemag 0', verb=0)
glafic.set_secondary('hvary 0', verb=0)
glafic.set_secondary('flag_hodensity 2', verb=0)
glafic.set_secondary('ran_seed -122000', verb=0)

glafic.startup_setnum(2, 0, 1)
glafic.set_lens(1, 'anfw', 0.23, 363082888658.0666, 0.0, 0.0, 0.10995996200936457, 72.60042853112898, 58.54207260919006, 0)
glafic.set_optlens(1, 1, 1, 1, 1, 1, 1, 1, 1)

glafic.set_lens(2, 'pert', 0.23, 0.777, 0.0, 0.0, 0.01056905892454293, 211.0867016064577, 0, 0.25985619506562513)
glafic.set_optlens(2, 1, 1, 1, 1, 1, 1, 1, 1)

glafic.set_point(1, 0.777, 0.0, 0.0)
glafic.set_optpoint(1, 1, 1, 1)

glafic.model_init(verb=0)

glafic.readobs_point('Test/input.dat')
glafic.optimize()
glafic.findimg()
glafic.write_crit(0.777)
glafic.write_lens(0.777)

glafic.quit()
