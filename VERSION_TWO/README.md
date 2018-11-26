Our second version of the project.

Observations:
Scorecard at the bottom of the frame is removed when un-necessary things like replays, ads, highlights within highlights, or any other
useless stuff.
Hence, we thought of using this properties of frames to delete such frames (ads,replays etc)

For detection of scorecard at the bottom of each frame, we first calculated Hue/Color Histograms of our main scoreboard and current frame.

For comparison of the histograms, we used greedy approach, by comparing the similarity between the trends of the color and color levels
appearing in the two frames. (We were surprised this approach actually worked :P)

Hope, this is helpful.
