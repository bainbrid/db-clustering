# db-clustering
Density based clustering for L1 tracks

## Physics context

In our system design up to 1665 tracks arrive every 0.5us. The table below summarises the bandwidth specification. We're interested in the row labelled "TRK". You can see the bandwidth is large but most of these objects will be zero (empty) most of the time. 
![Summary of L1 input data](https://github.com/bainbrid/db-clustering/blob/master/L1TriggerInputData.png)

The plot below shows the occupancy for 1/9 of the detector, and you can see the peak is around 40 objects, so even multiplying this by 9 (which is in itself probably an overestimate) gives ~350 objects, so the specification is really worst case and quite generous to preserve the "tail" in the plot.
![Number of tracks per phi sector](https://github.com/bainbrid/db-clustering/blob/master/TracksPerPhiSector.png)

The table below shows the contents of the 96 bits which describe each object. The z0 is the quantity we want to cluster and the other quantities can be used as weighting or in any other way which improves the quality of the clustering. The key one is q/R which gives the momentum of the particle.
![Number of tracks per phi sector](https://github.com/bainbrid/db-clustering/blob/master/TrackParameters.png)

## Available files 

`0.root`: test file containing jets from 250 LHC events. 

`00.root`-`39.root`: 40 files containing jets from ~1M LHC events (~25000 events/file, 0.5 GB/file).

## Definition of file contents

Documentation to come!

[Here](https://github.com/cms-l1t-offline/cmssw/blob/l1t-phase2-v2.37.0/L1Trigger/TrackFindingTracklet/test/L1TrackNtupleMaker.cc) is where the branches are filled in the CMS software. [This](https://github.com/cms-l1t-offline/cmssw/blob/l1t-phase2-v2.37.0/L1Trigger/TrackFindingTracklet/test/L1TrackNtupleMaker.cc#L567) is the method that iterates over LHC events. 

### Jet-level information 

Jets are sprays of collinear particles (both charged and neutral) that are clustered using the [anti-kT algorithm](https://arxiv.org/abs/0802.1189) with distance parameter R = 0.4. Jets typically contain tens of tracks from charged particles. 

| Variable                   | Description |
| ---                        | --- |
| jet_eta                    | Jet pseudorapidity |
| jet_phi                    | Jet azimuthal angle |
| jet_pt                     | Jet transverse momentum |
| jet_tp_sumpt               | Transverse-momentum sum over "tracking particles" associated to jet |
| jet_trk_sumpt              | Transverse-momentum sum over tracks associated to jet |
| jet_matchtrk_sumpt         |     |
| jet_loosematchtrk_sumpt    |     |

### Track information 

| Variable           | Description |
| ---                | --- |
| trk_pt             | Track transverse momentum | 
| trk_eta            | Track pseudorapidity | 
| trk_phi            | Track azimuthal angle | 
| trk_d0             | Track impact parameter (distance from point of closest approach to primary vertex) | 
| trk_z0             | Track longitudinal position (along beam pipe) at point of closest approach to primary vertex | 
| trk_chi2           | Chi squared for track helix fit | 
| trk_bendchi2       |     | 
| trk_nstub          |     | 
| trk_lhits          |     | 
| trk_dhits          |     | 
| trk_seed           |     | 
| trk_genuine        |     | 
| trk_loose          |     | 
| trk_unknown        |     | 
| trk_combinatoric   |     | 
| trk_fake           |     | 
| trk_matchtp_pdgid  |     | 
| trk_matchtp_pt     |     | 
| trk_matchtp_eta    |     | 
| trk_matchtp_phi    |     | 
| trk_matchtp_z0     |     | 
| trk_matchtp_dxy    |     | 
| trk_injet          |     | 
| trk_injet_highpt   |     | 
| trk_injet_vhighpt  |     |

### Tracking particle information 

| Variable           | Description |
| ---                | --- |
| tp_pt              | TP transverse momentum |
| tp_eta             | TP pseudorapidity |
| tp_phi             | TP azimuthal angle |
| tp_dxy             | TP transverse impact parameter (transverse distance from point of closest approach to primary vertex) |
| tp_d0              | TP impact parameter (distance from point of closest approach to primary vertex) |
| tp_z0              | Track longitudinal position (along beam pipe) at point of closest approach to primary vertex |
| tp_d0_prod         |     |
| tp_z0_prod         |     |
| tp_pdgid           | TP particle type (Particle Data Group identifier) |
| tp_nmatch          |     |
| tp_nloosematch     |     |
| tp_nstub           |     |
| tp_eventid         |     |
| tp_charge          | TP electric charge |
| tp_injet           |     |
| tp_injet_highpt    |     |
| tp_injet_vhighpt   |     |


