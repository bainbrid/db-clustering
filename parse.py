# Documention: https://github.com/scikit-hep/uproot
# Or google "uproot", plenty of support!
import uproot

# Open ROOT file (without any dependency on ROOT software)
file = uproot.open("0.root")

# Navigate to directory containing branches
events = file[b"L1TrackNtuple/eventTree"]

# Print branch names
print(events.keys())

# Browse the contents
print(events.show())

# Print contents of jet_pt branch, a "jagged array" or a list of events containing a list of (jet-level) variables
jet_pt = events.array("jet_pt")
jet_pt = events["jet_pt"].array() # equivalent
print(jet_pt)

# Plot the jet_pt distribution
import numpy as np
import matplotlib.pyplot as plt
counts,edges = np.histogram(jet_pt,bins=50,range=(0.,500.))
plt.step(x=edges, y=np.append(counts,0), where="post");
plt.xlim(edges[0], edges[-1]);
plt.ylim(0.5, counts.max()*2.);
plt.yscale("log");
plt.xlabel("Jet transverse momentum (GeV)");
plt.ylabel("Counts/bin");
plt.savefig("jet_pt.pdf")
