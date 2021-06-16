# This script provides a simple demonstration of parsing and
# manipulating the ROOT file contents, and a simple method to identify
# the true z0 position of the primary vertex.

import numpy as np

# The 'uproot' package allows to read/parse ROOT files without any
# dependency on the ROOT software project.
import uproot

# High Energy Physics data structures are typically nested and of
# variable length. We make use of 'jagged' or 'ragged' or 'awkward'
# arrays. Just Google 'uproot' and these terms, there is plenty of
# support/documentation! Here are some useful example sites, talks,
# and videos: 
# https://github.com/scikit-hep/uproot
# https://github.com/scikit-hep/awkward-array
# https://www.youtube.com/watch?v=2NxWpU7NArk
# https://indico.cern.ch/event/587955/contributions/
# https://indico.cern.ch/event/745288/contributions/

# Open test file (first copy to local space!).
file = uproot.open('0.root')

# Navigate to the directory containing the branches.
events = file[b'L1TrackNtuple/eventTree']

# Browse the contents of the ROOT file (several 'jagged arrays').
print()
print(events.show())

# "Tracking particles" provide the track parameters that are obtained
# directly from the Monte-Carlo (generator) and GEANT (detector
# simulation) programmes. They provide "truth-level" information that
# can be used for e.g. classification and regression studies. Branches
# beginning with 'tp_*' are related to the TPs. Reconstructed tracks
# are often associated with a TP (so we can "link" reconstructed to
# simulated quantities). Branches beginning with 'trk_*' are related
# to the tracks.

# Inspect the 'tp_eventid' branch from 1st event.
# 'tp_eventid' has a unique value for each pp collision (see details below).
# '0' means primary interaction (as defined by GEN info).
print()
print('Number of TPs in 1st event:',len(events['tp_eventid'].array()[0]))
print('List of "tp_eventid" values:',' '.join(['{:.0f}, '.format(x) for x in events['tp_eventid'].array()[0]]))

# Let's compare the kinematic quantities of tracks and their
# associated TPs. We'll look at the 1st event and the first 10 tracks.
# The 'measured' trk_* values are typically close to the 'truth-level'
# tp_* values. 
print()
print("Kinematic variables (truth and measured) from the slice [0,:10]")
print('tp_pt       ',' '.join(['{:6.2f}'.format(x) for x in events['tp_pt'].array()[0,:10]]))
print('matchtrk_pt ',' '.join(['{:6.2f}'.format(x) for x in events['matchtrk_pt'].array()[0,:10]]))
print('tp_eta      ',' '.join(['{:6.2f}'.format(x) for x in events['tp_eta'].array()[0,:10]]))
print('matchtrk_eta',' '.join(['{:6.2f}'.format(x) for x in events['matchtrk_eta'].array()[0,:10]]))
print('tp_phi      ',' '.join(['{:6.2f}'.format(x) for x in events['tp_phi'].array()[0,:10]]))
print('matchtrk_phi',' '.join(['{:6.2f}'.format(x) for x in events['matchtrk_phi'].array()[0,:10]]))
print('tp_z0       ',' '.join(['{:6.2f}'.format(x) for x in events['tp_z0'].array()[0,:10]]))
print('matchtrk_z0 ',' '.join(['{:6.2f}'.format(x) for x in events['matchtrk_z0'].array()[0,:10]]))

# There are many proton-proton (pp) interactions in an LHC event. Each
# pp interaction produces many particles that we associated to a
# "collision vertex" (CV). The "tp_eventid" identifies the CV from
# which each Tracking Particle (TP) originates.

# The most interesting proton-proton interaction is the "primary
# vertex" (PV). The PV is defined as the vertex with the largest pT^2
# when summing over all particles associated to the vertex. The
# tp_eventid value of 0 is a special value that indicates the PV.

# Look in more detail at 20 example "Trigger Primitives" found in 1st
# event. We inspect 20th-40th, so we see a range of tp_eventid.
print()
print("Variables from the slice [0,20:40]")
print('tp_eventid',' '.join(['{:6.0f}'.format(x) for x in events['tp_eventid'].array()[0,20:40]]))
print('tp_z0     ',' '.join(['{:6.2f}'.format(x) for x in events['tp_z0'].array()[0,20:40]]))
print('tp_d0     ',' '.join(['{:6.2f}'.format(x) for x in events['tp_d0'].array()[0,20:40]]))
print('tp_pt     ',' '.join(['{:6.2f}'.format(x) for x in events['tp_pt'].array()[0,20:40]]))
print('tp_eta    ',' '.join(['{:6.2f}'.format(x) for x in events['tp_eta'].array()[0,20:40]]))
print('tp_phi    ',' '.join(['{:6.2f}'.format(x) for x in events['tp_phi'].array()[0,20:40]]))
print('tp_pdgid  ',' '.join(['{:6.0f}'.format(x) for x in events['tp_pdgid'].array()[0,20:40]]))

# CMS coordinate system: z is along the LHC beam line, x and y are in
# the transverse plane. "phi" is the azimuthal angle, defined in the
# transverse plane. "eta" is the psuedorapidity, another angle defined
# in the longitudinal plane. phi and eta give the direction of the
# particle. "pt" is the projection of the particle momentum onto the
# transverse plane.

# The "tp_d0" is the impact parameter of each TP, the (3D) distance
# from the point of closest approach (PCA) to the vertex to which the
# TP is associated. Related, the "tp_z0" is the z position at the PCA.

# In addition to the PV and the many CVs, there is a third class of
# vertices. "Secondary vertices" (SV) arise from the decay of
# long-lived particles. Long-lived "mother" particles produced in the
# LHC pp interactions decay to "daughter" particles at some point in
# space away from the originating pp interaction. Typically,
# interesting SVs are found away from the beam line (because otherwise
# we cannot distinguish them from the other CV). ie x != 0 and y != 0
# or, equivalantly, at a radius R > 0. Further, TPs from SVs will
# typically have nonzero values of tp_d0.

# For these studies, we only care about TPs from the PV and we can
# ignore all TPs from the other CVs and SVs in the event.

# A "mask" to inspect only data related to the PVs (for which tp_eventid == 0) 
mask = events['tp_eventid'].array() == 0

print()
print("Same variables from the slice [mask][0,-7:] (ie for the PV only)")
print('tp_eventid',' '.join(['{:6.0f}'.format(x) for x in events['tp_eventid'].array()[mask][0,-7:]]))
print('tp_z0     ',' '.join(['{:6.2f}'.format(x) for x in events['tp_z0'].array()[mask][0,-7:]]))
print('tp_d0     ',' '.join(['{:6.2f}'.format(x) for x in events['tp_d0'].array()[mask][0,-7:]]))
print('tp_pt     ',' '.join(['{:6.2f}'.format(x) for x in events['tp_pt'].array()[mask][0,-7:]]))
print('tp_eta    ',' '.join(['{:6.2f}'.format(x) for x in events['tp_eta'].array()[mask][0,-7:]]))
print('tp_phi    ',' '.join(['{:6.2f}'.format(x) for x in events['tp_phi'].array()[mask][0,-7:]]))
print('tp_pdgid  ',' '.join(['{:6.0f}'.format(x) for x in events['tp_pdgid'].array()[mask][0,-7:]]))

# Note that some entries of "tp_d0" are nonzero, which implies that
# the TPs are "daughter TPs" (that arise from the decay of a mother
# particle) and should be associated with a SV and not the PV. Hence,
# we mask these TPs out.

# Let's define some new variables (just for "shorthand")
tp_eventid = events['tp_eventid'].array()
tp_z0 = events['tp_z0'].array()
tp_d0 = events['tp_d0'].array()
tp_pt = events['tp_pt'].array()

# Filter our TPs from SVs by requiring tp_d0 ~= 0.
# Threshold of 0.01 (cm) is loosely motivated by the tracker position resolution of O(10 um)
mask_no_sv = np.abs(tp_d0) < 0.01

# Let's look again and print which TPs would be masked
print()
print("Same again but also mask_no_sv")
print('tp_eventid',' '.join(['{:6.0f}'.format(x) for x in tp_eventid[mask][0,-7:]]))
print('tp_z0     ',' '.join(['{:6.2f}'.format(x) for x in tp_z0[mask][0,-7:]]))
print('tp_d0     ',' '.join(['{:6.2f}'.format(x) for x in tp_d0[mask][0,-7:]]))
print('mask_no_sv',' '.join(['{:>6s}'.format('ok' if x else 'mask!') for x in mask_no_sv[mask][0,-7:]]))

# TPs with nonzero values of tp_d0 also have different values of tp_z0
# from the TPs from the same PV. These will be masked. Let's look at
# some values of tp_z0 from TPs from the PV, with SVs masked, from a
# number of example events.
print()
print("Consider 'tp_z0' for TPs from PV and not SVs from first 10 events")
for x in tp_z0[mask&mask_no_sv][:10] : print('(len={:2.0f},'.format(len(x)),
                                             'mean={:5.2f})'.format(np.mean(x)),
                                             ' '.join(['{:.2f}'.format(y) for y in x]))

# We can determine an estimate for the "true PV position" using the
# mean of the masked tp_z0 values. Below you can see the effect of the
# masks, by determining the mean tp_z0 value with TPs associated with
# 1) all vertices, 2) just the PV, and 3) also after removing SVs.
print()
print('All vertices   ',' '.join(['{:6.2f}'.format(x) for x in tp_z0.mean()[:10]]))
print('All PVs        ',' '.join(['{:6.2f}'.format(x) for x in tp_z0[mask].mean()[:10]]))
print('All PVs, no SVs',' '.join(['{:6.2f}'.format(x) for x in tp_z0[mask&mask_no_sv].mean()[:10]]))

# Finally, we end up with this expression:
true_z0 = tp_z0[mask&mask_no_sv].mean()
print()
print('len(true_z0) = {:.0f},'.format(len(true_z0)),
      'values:',' '.join(['{:.2f}'.format(x) for x in true_z0.tolist()]))
