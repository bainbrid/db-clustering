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

| Variable           | Description |
| ---                | --- |
| trk_pt             |     | 
| trk_eta            |     | 
| trk_phi            |     | 
| trk_d0             |     | 
| trk_z0             |     | 
| trk_chi2           |     | 
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

