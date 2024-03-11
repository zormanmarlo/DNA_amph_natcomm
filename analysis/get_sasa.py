import matplotlib.pyplot as plt
import mdtraj as md
import numpy as np
import pickle

##------------------------------------------------------------------------------
## Script to calculate and plot SASA ##
## for hydrophobic portion of DNA amph ##
##------------------------------------------------------------------------------

# import trajectory
job_name = "C88_single_85C_MD"
# job_name_ext = "C88_single_85C_MD_ext"
trj_path = "/Users/mdog/research/dna_amph/sims/"+job_name+"/"+job_name
# trj_path_ext = "/Users/mdog/research/dna_amph/sims/"+job_name_ext+"/"+job_name_ext
trj = md.load(trj_path+".dcd", top=trj_path+".pdb")
# trj_ext = md.load(trj_path_ext+".dcd", top=trj_path_ext+".pdb")
# trj = trj.join(trj_ext)

# select only hydrophobic portion of molecule
# (unnecessary right now because just saving chain A when I convert trj format)
# to_keep = [a.index for a in traj.topology.atoms if a.residue.name != "A"]
# sliced_trj = trj.atom_slice(to_keep)

# calculate sasa
sasa = md.shrake_rupley(trj).sum(axis=1)
rel_sasa = [i/sasa[0] for i in sasa]

# pickle data
pickle.dump(sasa, open("../data/"+job_name+"_SASA.p", "wb"))

# plot
plt.plot(rel_sasa)
plt.savefig("../figs/"+job_name+"_SASA.png")
