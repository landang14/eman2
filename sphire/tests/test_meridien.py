from __future__ import print_function
from __future__ import division



from numpy import allclose

# import mpi
# import sp_global_def
# mpi.mpi_init(0, [])
# sp_global_def.BATCH = True
# sp_global_def.MPI = True

# from sphire.bin_py3 import sp_meridien as oldfu
# from sphire.bin import sp_meridien as fu

from sp_utilities import get_im
from os import listdir,system as os_system,path
from os.path import isfile, join

from .test_module import ABSOLUTE_OLDBIN_PATH,ABSOLUTE_PATH_TO_SPHIRE_DEMO_RESULTS_FOLDER_NEW,ABSOLUTE_BIN_PATH,remove_dir
import unittest

try:
    # python 3.4+ should use builtin unittest.mock not mock package
    from unittest.mock import patch
except ImportError:
    from mock import patch

try:
    from StringIO import StringIO  # python2 case
except ImportError:
    # python3 case. You will get an error because 'sys.stdout.write(msg)' presents in the library not in the test!!
    from io import StringIO


import subprocess
import os


MPI_PATH = "/home/adnan/applications/sphire/miniconda3/envs/py3_v6/bin/mpirun" #"/home/adnan/applications/sphire/v1.1/envs/conda_fresh/bin/"
NUM_PROC = 8

"""
WHAT IS MISSING:
RESULT AND KNOWN ISSUES
"""


class Test_run(unittest.TestCase):
    out_dir_old = "oldmeridien"
    out_dir_new = "newmeridien"

    @classmethod
    def tearDownClass(cls):
        remove_dir(cls.out_dir_old)
        remove_dir(cls.out_dir_new)

    #it is not the same run of the tutorial (pg.55) because I minimized the iteration to speed up the test.
    # At pg.92 there is another run. I did not test it because it performs the same operation done in this test
    # It takes anyway an hour
    @unittest.skip("Had initialization issue")
    def test_old(self):

        os_system(MPI_PATH
            + " -np "
            +str(NUM_PROC)
            +" "+path.join(ABSOLUTE_OLDBIN_PATH,"sp_meridien.py")+" "
            + " 'bdb:"+path.join(ABSOLUTE_PATH_TO_SPHIRE_DEMO_RESULTS_FOLDER_NEW,"06_SUBSTACK#isac_substack'")
            +" "+self.out_dir_old
            + " " + path.join(ABSOLUTE_PATH_TO_SPHIRE_DEMO_RESULTS_FOLDER_NEW, "09_ADJUSTMENT","vol3d_ref_moon_eliminated_mask.hdf")
            +" --initialshifts"
            + " --radius=145"
            +" --mask3D="+ path.join(ABSOLUTE_PATH_TO_SPHIRE_DEMO_RESULTS_FOLDER_NEW, "10_MASK","sp_mask_mask.hdf")
           +" --symmetry=c5")
        os_system(
            MPI_PATH
            + " -np "
            +str(NUM_PROC)
            +" "+path.join(ABSOLUTE_BIN_PATH,"sp_meridien.py")
            + " 'bdb:"+path.join(ABSOLUTE_PATH_TO_SPHIRE_DEMO_RESULTS_FOLDER_NEW,"06_SUBSTACK#isac_substack'")
            +" "+self.out_dir_new
            + " " + path.join(ABSOLUTE_PATH_TO_SPHIRE_DEMO_RESULTS_FOLDER_NEW, "09_ADJUSTMENT","vol3d_ref_moon_eliminated_mask.hdf")
            + " --initialshifts"
            + " --radius=145"
            + " --mask3D=" + path.join(ABSOLUTE_PATH_TO_SPHIRE_DEMO_RESULTS_FOLDER_NEW, "10_MASK", "sp_mask_mask.hdf")
            + " --symmetry=c5")

        # as they are ordered alphanumerically the first is always vol0
        hdfFilesOld = [f for f in listdir(self.out_dir_old) if isfile(join(self.out_dir_old, f)) and f.split(".")[1] == "hdf"]
        hdfFilesNew = [f for f in listdir(self.out_dir_new) if isfile(join(self.out_dir_new, f)) and f.split(".")[1] == "hdf"]
        old_v0 = get_im(path.join(self.out_dir_old, hdfFilesOld[0]))
        old_v1 = get_im(path.join(self.out_dir_old, hdfFilesOld[1]))
        new_v0 = get_im(path.join(self.out_dir_new, hdfFilesNew[0]))
        new_v1 = get_im(path.join(self.out_dir_new, hdfFilesNew[1]))
        self.assertTrue(allclose(old_v0.get_3dview(),new_v0.get_3dview(),atol=0.05))
        self.assertTrue(allclose(old_v1.get_3dview(), new_v1.get_3dview(), atol=0.05))
        # self.assertTrue(allclose(new_v0.get_3dview().flatten().tolist()[0:100],[0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539],atol=0.005))
        # self.assertTrue(allclose(new_v1.get_3dview().flatten().tolist()[0:100], [0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855], atol=0.005))


    def test_new(self):
        out_dir_old = "oldmeridien"
        out_dir_new = "newmeridien"

        os.mkdir(out_dir_old)
        os.mkdir(out_dir_new)
        testcommand_old = (MPI_PATH
            + " -np "
            +str(NUM_PROC)
            +" "+path.join(ABSOLUTE_OLDBIN_PATH,"sp_meridien.py")+" "
            + " 'bdb:"+path.join(ABSOLUTE_PATH_TO_SPHIRE_DEMO_RESULTS_FOLDER_NEW,"06_SUBSTACK_ANO#isac_substack'")
            +" "+self.out_dir_old
            + " " + path.join(ABSOLUTE_PATH_TO_SPHIRE_DEMO_RESULTS_FOLDER_NEW, "09_ADJUSTMENT","vol3d_ref_moon_eliminated_mask.hdf")
            +" --initialshifts"
            + " --radius=145"
            +" --mask3D="+ path.join(ABSOLUTE_PATH_TO_SPHIRE_DEMO_RESULTS_FOLDER_NEW, "10_MASK","sp_mask_mask.hdf")
           +" --symmetry=c5")

        testcommand_new = (
            MPI_PATH
            + " -np "
            +str(NUM_PROC)
            +" "+path.join(ABSOLUTE_BIN_PATH,"sp_meridien.py")
            + " 'bdb:"+path.join(ABSOLUTE_PATH_TO_SPHIRE_DEMO_RESULTS_FOLDER_NEW,"06_SUBSTACK_ANO#isac_substack'")
            +" "+self.out_dir_new
            + " " + path.join(ABSOLUTE_PATH_TO_SPHIRE_DEMO_RESULTS_FOLDER_NEW, "09_ADJUSTMENT","vol3d_ref_moon_eliminated_mask.hdf")
            + " --initialshifts"
            + " --radius=145"
            + " --mask3D=" + path.join(ABSOLUTE_PATH_TO_SPHIRE_DEMO_RESULTS_FOLDER_NEW, "10_MASK", "sp_mask_mask.hdf")
            + " --symmetry=c5")

        # as they are ordered alphanumerically the first is always vol0

        a = subprocess.run(args =[testcommand_old], shell=True, stderr=subprocess.STDOUT)
        b = subprocess.run(args=[testcommand_new], shell=True, stderr=subprocess.STDOUT)


        # hdfFilesOld = [f for f in listdir(self.out_dir_old) if isfile(join(self.out_dir_old, f)) and f.split(".")[1] == "hdf"]
        # hdfFilesNew = [f for f in listdir(self.out_dir_new) if isfile(join(self.out_dir_new, f)) and f.split(".")[1] == "hdf"]
        # old_v0 = get_im(path.join(self.out_dir_old, hdfFilesOld[0]))
        # old_v1 = get_im(path.join(self.out_dir_old, hdfFilesOld[1]))
        # new_v0 = get_im(path.join(self.out_dir_new, hdfFilesNew[0]))
        # new_v1 = get_im(path.join(self.out_dir_new, hdfFilesNew[1]))
        # self.assertTrue(allclose(old_v0.get_3dview(), new_v0.get_3dview(),atol=0.05))
        # self.assertTrue(allclose(old_v1.get_3dview(), new_v1.get_3dview(), atol=0.05))
        # self.assertTrue(allclose(new_v0.get_3dview().flatten().tolist()[0:100],[0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539, 0.000977565417997539],atol=0.005))
        # self.assertTrue(allclose(new_v1.get_3dview().flatten().tolist()[0:100], [0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855, 0.0011777321342378855], atol=0.005))





















