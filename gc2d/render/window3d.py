
from mayavi import mlab
import numpy as np

@mlab.show
@mlab.animate
def anim():
    f = mlab.gcf()
    while 1:
        f.scene.camera.azimuth(10)
        f.scene.render()
        yield


def render3d(array):
    mlab.clf()

    #array = np.ma.fix_invalid(array, fill_value=0)
    vis = mlab.surf(array, warp_scale='auto')
    vis_mut = vis.mlab_source

    

    a = anim() # Starts the animation.

def render_window_3d(data):
    render3d(data)
