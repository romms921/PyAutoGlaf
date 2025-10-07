import glafic

glafic.init(0.3, 0.7, -1.0, 0.7, 'Test/POW+SHEAR', -3.5, -3.5, 3.5, 3.5, 0.01, 0.01, 1.0, verb=0)

glafic.set_secondary('chi2_splane 0', verb=0)
glafic.set_secondary('chi2_checknimg 0', verb=0)
glafic.set_secondary('chi2_restart -1', verb=0)
glafic.set_secondary('chi2_usemag 0', verb=0)
glafic.set_secondary('hvary 0', verb=0)
glafic.set_secondary('ran_seed -122000', verb=0)

glafic.startup_setnum(2, 0, 1)
glafic.set_lens(1, 'pow', 0.23, 0.777, 0.0, 0.0, 0.6713554015203755, 317.12605269339093, 0.7222669319431374, 1.7120077971172076)
glafic.set_optlens(1, 1, 1, 1, 1, 1, 1, 1, 1)

glafic.set_lens(2, 'shear', 0.23, 0.777, 0.0, 0.0, 0.09579081108763163, 66.71011416829519, 0, 0.3733569644991829)
glafic.set_optlens(2, 1, 1, 1, 1, 1, 1, 1, 1)

glafic.set_point(1, 0.777, 0.0, 0.0)
glafic.set_optpoint(1, 1, 1, 1)

glafic.model_init(verb=0)

glafic.optimize()
glafic.findimg()
glafic.write_crit(0.777)
glafic.write_lens(0.777)

glafic.quit()
