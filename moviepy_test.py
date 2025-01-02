
from moviepy import VideoFileClip, TextClip, CompositeVideoClip

# Load file example.mp4 and keep only the subclip from 00:00:10 to 00:00:20
# Reduce the audio volume to 80% of its original volume

clip = (
    VideoFileClip("1_AutoPlane.mp4")
    .subclipped(0, 97)
)


# Overlay the text clip on the first video clip
final_video = CompositeVideoClip([clip])
final_video.write_videofile("1_AutoPlane-0-97.mp4")






from moviepy import VideoFileClip, concatenate_videoclips

# We load all the clips we want to concatenate
# clip1 = VideoFileClip("1_AutoPlane.mp4").subclipped(0, 97)
# clip2 = VideoFileClip("example2.mp4").subclipped(0, 1)
# clip2 = VideoFileClip("2.mp4")
# clip3 = VideoFileClip("1_AutoPlane.mp4").subclipped(122, 160)
final_clip = concatenate_videoclips([clip1, clip3])

clip1 = VideoFileClip("1.mp4")
clip2 = VideoFileClip("2.mp4")
clip3 = VideoFileClip("3.mp4")
# We concatenate them and write the result
final_clip = concatenate_videoclips([clip1,clip2 ,clip3])

final_clip.write_videofile("autocap.mp4")