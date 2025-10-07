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
glafic.set_lens(1, 'anfw', 0.23, 8969773375008.418, 0.0, 0.0, 0.5659520122192441, 221.87744517263104, 80.79620116250311, 0)
glafic.set_optlens(1, 1, 1, 1, 1, 1, 1, 1, 1)

glafic.set_lens(2, 'pert', 0.23, 0.777, 0.0, 0.0, 0.0981741964114337, 48.97651507938833, 0, 0.5385645755193087)
glafic.set_optlens(2, 1, 1, 1, 1, 1, 1, 1, 1)

glafic.set_point(1, 0.777, 0.0, 0.0)
glafic.set_optpoint(1, 1, 1, 1)

glafic.model_init(verb=0)

glafic.optimize()
glafic.findimg()
glafic.write_crit(0.777)
glafic.write_lens(0.777)

glafic.quit()
