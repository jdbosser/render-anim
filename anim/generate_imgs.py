from matplotlib.animation import Animation, AbstractMovieWriter
import tempfile 
from pathlib import Path
import subprocess
from typing import Optional

class MWriter(AbstractMovieWriter):
    
    def __init__(self, num_frames: int, basename: str, *args, callback = None, **kwargs):
        self.basename = basename
        self.frame_num = 0
        self.callback = callback
        
        self.format = "{:0" + str(len(str(num_frames))) + "}"

        super().__init__(*args, **kwargs)

    def setup(self, fig, outfile, dpi = None):
        super().setup(fig, outfile, dpi = dpi)
        self.outfile

    def grab_frame(self, **savefig_kwargs):
        print("saving frame", self.frame_num)
        self.fig.savefig(self.basename + "/" + self.format.format(self.frame_num) + ".png", **savefig_kwargs)
        self.frame_num += 1
        

    def finish(self):

        print("Done!")


PathLike = Path | str
def export_frames(anim: Animation, directory: PathLike, num_frames: int):
    directory = Path(directory)
    writer = MWriter(num_frames, str(directory.absolute()))
    anim.save("blurgh", writer = writer)

def movie(anim: Animation, destination: str, num_frames: int, fps: Optional[int] = None) -> None:
    
    if fps is None:
        fps = 5

    with tempfile.TemporaryDirectory() as tmpdirname:
        print('created temporary directory', tmpdirname)
        
        tmpdirname = Path(tmpdirname) 
        writer = MWriter(num_frames, str(tmpdirname.absolute()))

        anim.save("", writer = writer)
        # ffmpeg -framerate 24 -i Project%03d.png Project.mp4
        subprocess.run(["ffmpeg", "-framerate", str(fps), "-i", str(tmpdirname.absolute()) + "/%" + writer.format[2:4] + "d.png", destination]) 
