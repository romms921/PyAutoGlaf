import glafic

glafic.init(0.3, 0.7, -1.0, 0.7, 'Output/POW+SHEAR', -3.5, -3.5, 3.5, 3.5, 0.01, 0.01, 1, verb=0)

glafic.set_secondary('chi2_splane 1', verb=0)
glafic.set_secondary('chi2_checknimg 0', verb=0)
glafic.set_secondary('chi2_restart -1', verb=0)
glafic.set_secondary('chi2_usemag 0', verb=0)
glafic.set_secondary('hvary 0', verb=0)
glafic.set_secondary('ran_seed -122000', verb=0)

glafic.startup_setnum(2, 0, 1)
glafic.set_lens(1, 'pow', 0.23, 0.777, 0.0, 0.0, 0.060282266642452384, 115.30107178796541, 0.5698657377125327, 2.444769115774246)
glafic.setopt_lens(1, 1, 1, 1, 1, 1, 1, 1, 1)

glafic.set_lens(2, 'pert', 0.23, 0.777, 0.0, 0.0, 0.07284256235845336, 305.78164390211487, 0, 0.17868726104549257)
glafic.setopt_lens(2, 1, 1, 1, 1, 1, 1, 1, 1)

glafic.set_point(1, 0.777, 0.0, 0.0)
glafic.setopt_point(1, 1, 1, 1)

glafic.model_init(verb=0)

glafic.readobs_point('Run/input.dat')
glafic.optimize()
glafic.findimg()
glafic.writecrit(0.777)
glafic.writelens(0.777)

glafic.quit()
