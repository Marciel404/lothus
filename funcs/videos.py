from moviepy.editor import *

async def lulamaromba(avatar):
    clip = VideoFileClip("./videos/feijãopuro.mp4").subclip(0, 10)
    image = ImageClip(avatar)

    image1 = image.set_start(0)
    image1 = image1.set_end(1.65)
    image1 = image1.rotate(-35)
    image1 = image1.set_position((330,400))
    image1 = image1.resize(width = 250, height = 250)

    image2 = image.set_start(1.9)
    image2 = image2.set_end(3.4)
    image2 = image2.set_position((300,415))
    image2 = image2.resize(width = 250, height = 250)

    image3 = image.set_start(3.6)
    image3 = image3.set_end(6)
    image3 = image3.set_position((355,260))
    image3 = image3.resize(width = 250, height = 250)

    image4 = image.set_start(6)
    image4 = image4.set_end(10)
    image4 = image4.set_position((260,100))
    image4 = image4.resize(width = 250, height = 250)

    video = CompositeVideoClip([clip, image1, image2, image3, image4])
    video.write_videofile(
        filename = "./videos/save/lulamaromba.mp4",
        codec = 'libx264',
        fps = 24,
        preset ='ultrafast',
        threads = 8,
        audio_bitrate = '70k',
        audio_codec = 'libmp3lame',
        ffmpeg_params = ["-crf", "24"],
        logger = None
    )
    video.close()