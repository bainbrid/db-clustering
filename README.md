# db-clustering
Density based clustering for L1 tracks

## Physics context

Details can be found in [this](https://www.dropbox.com/s/alijxemlawo8tsq/CMS-L1-TDR-Trk-Vtx-Tim.pdf?dl=0) document (semi-permanent link), which is the Technical Design Report (TDR) for the CMS Level-1 (L1) Trigger Upgrade project, aimed at the High Luminosity LHC (HL-LHC). Below are some relevant tables and plots, taken from the TDR. 

In our system design, up to 1665 tracks arrive every 0.5us. The table below summarises the bandwidth specification. We're interested in the row labelled "TRK". You can see the bandwidth is large but most of these objects will be zero (empty) most of the time. <br>

<img src="https://github.com/bainbrid/db-clustering/blob/master/L1TriggerInputData.png" width="600"/>

The plot below shows the occupancy for 1/9 of the detector, and you can see the peak is around 40 objects, so even multiplying this by 9 (which is in itself probably an overestimate) gives ~350 objects, so the specification is really worst case and quite generous to preserve the "tail" in the plot. <br>

<img src="https://github.com/bainbrid/db-clustering/blob/master/TracksPerPhiSector.png" width="600"/>

The table below shows the anticipated contents of the 96 bits which describe each object. The table does not exactly represent the content of the ntuple (as studies have evolved), but it is representative of the interesting variables. For example, the z0 is the quantity we want to cluster and the other quantities can be used as weighting or in any other way which improves the quality of the clustering. A key variable is q/R which gives the momentum of the particle. <br>

<img src="https://github.com/bainbrid/db-clustering/blob/master/TrackParameters.png" width="400"/>

## Available files 

Location: https://cernbox.cern.ch/index.php/s/HW5Ggy6nw0h7klP

`0.root`: test file containing jets from 250 LHC events. 

`00.root`-`39.root`: 40 files containing jets from ~1M LHC events (~25000 events/file, 0.5 GB/file).

## Definition of file contents

(This documentation is a work in progress!)

[Here](https://github.com/cms-l1t-offline/cmssw/blob/l1t-phase2-v2.37.0/L1Trigger/TrackFindingTracklet/test/L1TrackNtupleMaker.cc) is where the branches are filled in the CMS software. [This](https://github.com/cms-l1t-offline/cmssw/blob/l1t-phase2-v2.37.0/L1Trigger/TrackFindingTracklet/test/L1TrackNtupleMaker.cc#L567) is the method that iterates over LHC events. 

### Track information 

Each LHC event contains several proton-proton (pp) interactions, as many as ~200 for the LH-LHC. 

The tracks from charged particles from each LHC event should be "clustered" according to trk_z0 to identify as many pp interaction as possible, in terms of their longitudinal positions (z0). There are several variables associated to each track that may be of use.

| Variable           | Description |
| ---                | --- |
| trk_pt             | Track transverse momentum | 
| trk_eta            | Track pseudorapidity | 
| trk_phi            | Track azimuthal angle | 
| trk_d0             | Track impact parameter (distance from point of closest approach to originating vertex) | 
| trk_z0             | Track longitudinal position (along beam pipe) at point of closest approach to originating vertex | 
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

Tracking particles provide the track parameters that are obtained directly from the Monte-Carlo (generator) and GEANT (detector simulation) programmes. They provide "truth-level" information that can be used for classification and regression studies. 

| Variable           | Description |
| ---                | --- |
| tp_pt              | TP transverse momentum |
| tp_eta             | TP pseudorapidity |
| tp_phi             | TP azimuthal angle |
| tp_dxy             | TP transverse impact parameter (transverse distance from point of closest approach to originating vertex) |
| tp_d0              | TP impact parameter (distance from point of closest approach to originating vertex) |
| tp_z0              | Track longitudinal position (along beam pipe) at point of closest approach to originating vertex |
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

### Jet-level information 

Jets are sprays of collinear particles (both charged and neutral) that are clustered using the [anti-kT algorithm](https://arxiv.org/abs/0802.1189) with distance parameter R = 0.4. Jets typically contain tens of tracks from charged particles. The jet objects are of lesser interest for this study.

| Variable                   | Description |
| ---                        | --- |
| jet_eta                    | Jet pseudorapidity |
| jet_phi                    | Jet azimuthal angle |
| jet_pt                     | Jet transverse momentum |
| jet_tp_sumpt               | Transverse-momentum sum over "tracking particles" associated to jet |
| jet_trk_sumpt              | Transverse-momentum sum over tracks associated to jet |
| jet_matchtrk_sumpt         |     |
| jet_loosematchtrk_sumpt    |     |

## Scripts

The `analysis.py` script provides simple examples of how to read and manipulate the ROOT file contents, and a simple method to estimate the true z0 position of the primary vertex. The `histograms.py` script produces some example plots, one of which is shown below. The plot shows the difference between the z0 position of each track found an LHC event and our estimate of the "true" z0 position of the "primary vertex" (from the most interesting proton-proton interaction in the LHC event). There is a strong peak at zero, which is due to the tracks originating from the primary vertex. The peak is superimposed on an almost-flat continuous background, which is due to tracks from the other (less interesting) proton-proton interactions in the same LHC event. (The scripts contain descriptions of the terms used here in more detail.)

<img src="https://github.com/bainbrid/db-clustering/blob/master/residuals.png" width="400"/>
