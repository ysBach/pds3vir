from pathlib import Path
from .vicar import VicarImage
from planetaryimage import PDS3Image
from warnings import warn
import copy
import pvl

__all__ = ['open_pds3']


def open_pds3(path, vicar=True, extraneous='warn', cut=True,
            #   h_time="IMAGE_TIME", h_targ="TARGET_NAME", h_id="IMAGE_ID",
            #   h_filt="FILTER_NAME", h_exp="EXPOSURE_DURATION", h_gain="GAIN_MODE_ID",
              ):
    """
    Open a PDS3 image.

    Parameters
    ----------
    vicar : bool
        If True, open the .img as a VicarImage. While testing with Galileo PDS3
        images, we must use it. But just in case it gives wrong results, just
        simply set it to False so that it opens the .img as a PDS3Image.

    h_* : str
        The header keywords for time, target, id, filter, exposure, etc. The
        user can either use VICAR keywords or lbl file keywords (must use lbl
        file keyword if vical=False).
    """
    path = Path(path)
    pds = PDS3Image.open(str(path))
    if path.suffix == '.lbl':
        if vicar:
            imgpath = Path(pds.filename).parent/pds.data_filename
            vic = VicarImage.from_file(imgpath, extraneous=extraneous)

            pds.label_lbl = copy.deepcopy(pds.label)
            pds.label_img = pvl.loads(vic.header)
            for k, v in pds.label_img:
                pds.label.append(k, v)

            if cut and (cow := pds.label_img.get("CUT_OUT_WINDOW")) is not None:
                # label from lbl file looks strange... does not match that of img file.
                if (cow[2] - cow[0]) <= 1 or (cow[3] - cow[1] <= 1):
                    warn("CUT_OUT_WINDOW is incorrect. Omiting `cut`.", RuntimeWarning)
                    pds.data = vic.data_3d
                else:
                    pds.data = vic.data_3d[:, cow[0]:cow[2], cow[1]:cow[3]]
            else:
                pds.data = vic.data_3d

            pds.header_bytes = copy.deepcopy(vic.header_bytes)
            pds.header_str = copy.deepcopy(vic.header)
            pds.binary_header = copy.deepcopy(vic.binary_header)  # "Telemetry + bad data"
            pds.prefix_2d = copy.deepcopy(vic.prefix_2d)
            pds.prefix_3d = copy.deepcopy(vic.prefix_3d)


        # pds.time = Time(pds.label[h_time])
        # pds.targ = pds.label[h_targ]
        # pds.id = pds.label[h_id]
        # pds.filt = pds.label[h_filt]
        # pds.exp_ms = pds.label[h_exp]
        # pds.gain = pds.label[h_gain]
        # pds.ra

        return pds

    if path.suffix == '.img':
        return pds

