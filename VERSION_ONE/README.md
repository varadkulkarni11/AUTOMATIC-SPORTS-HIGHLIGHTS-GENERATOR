This is a basic version of the model, in which only the difference between the audio amplitude levels are considered.

'mp4_to_wav_file.py' is for converting the match video to a *.wav format.

We later used the amplitude levels of each audio frame and extracted the time ranges in which the audio levels are above the average level of the total audio amplitudes
The code for the above description can be found in 'Extract_Time_Ranges.py'

Lastly, we used the time ranges and sliced the found ranges from the main match video, that can be found in 'final_v1_out.py'
