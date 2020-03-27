# This script produces some example histograms

import uproot
import numpy as np
import matplotlib.pyplot as plt # plotting package

file = uproot.open('0.root') 
events = file[b'L1TrackNtuple/eventTree']

# Define useful variables, masks, and true z0 of primary vertex
tp_vertex_id = events['tp_eventid'].array()
tp_z0 = events['tp_z0'].array()
tp_d0 = events['tp_d0'].array()
trk_z0 = events['trk_z0'].array()
trk_pt = events['trk_pt'].array()
mask = tp_vertex_id == 0
mask_no_sv = np.abs(tp_d0) < 0.01
true_z0 = tp_z0[mask&mask_no_sv].mean()

# Plot the trk_pt distribution
counts,edges = np.histogram(trk_pt.flatten(),bins=75,range=(0.,150.))
plt.step(x=edges, y=np.append(counts,0), where='post')
plt.xlim(edges[0], edges[-1])
plt.yscale('log')
plt.ylim(0.5, counts.max()*2.)
plt.xlabel('Track transverse momentum (GeV)')
plt.ylabel('Counts/bin')
plt.savefig('trk_pt.pdf')
plt.clf()

# Plot the trk_z0 distribution
counts,edges = np.histogram(trk_z0.flatten(),bins=20,range=(-5.,5.))
plt.step(x=edges, y=np.append(counts,0), where='post')
plt.xlim(edges[0], edges[-1])
plt.yscale('linear')
plt.ylim(0., counts.max()*2.)
plt.xlabel('Track z0 position (cm)')
plt.ylabel('Counts/bin')
plt.savefig('trk_z0.pdf')
plt.clf()

# Plot the tp_z0 distribution
counts,edges = np.histogram(tp_z0.flatten(),bins=20,range=(-5.,5.))
plt.step(x=edges, y=np.append(counts,0), where='post')
plt.xlim(edges[0], edges[-1])
plt.yscale('linear')
plt.ylim(0., counts.max()*2.)
plt.xlabel('TP z0 position (cm)')
plt.ylabel('Counts/bin')
plt.savefig('tp_z0.pdf')
plt.clf()

# Plot the true z0 position of the primary vertex
counts,edges = np.histogram(true_z0.flatten(),bins=10,range=(-5.,5.))
plt.step(x=edges, y=np.append(counts,0), where='post')
plt.xlim(edges[0], edges[-1])
plt.yscale('linear')
plt.ylim(0., counts.max()*2.)
plt.xlabel('True primary vertex z0 position (cm)')
plt.ylabel('Counts/bin')
plt.savefig('true_z0.pdf')
plt.clf()

# Plot the residuals between the trk_z0 and true_z0
residuals = trk_z0 - true_z0
counts,edges = np.histogram(residuals.flatten(),bins=100,range=(-5.,5.))
plt.step(x=edges, y=np.append(counts,0), where='post')
plt.xlim(edges[0], edges[-1])
plt.yscale('linear')
plt.ylim(0., counts.max()*2.)
plt.xlabel('Track z0 position - (true) primary vertex z0 position (cm)')
plt.ylabel('Counts/bin')
plt.savefig('residuals.pdf')
plt.clf()

# The final plot shows a strong peak at zero, which is due to the
# tracks originating from the primary vertex. The peak is superimposed
# on an almost-flat continuous background, which is due to tracks from
# the other interactions that happen in an LHC event (called pileup).


