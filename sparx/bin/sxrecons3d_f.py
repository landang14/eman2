#!/usr/bin/env python
from __future__ import print_function

#
# Author: Pawel A.Penczek, 09/09/2006 (Pawel.A.Penczek@uth.tmc.edu)
# Copyright (c) 2000-2006 The University of Texas - Houston Medical School
#
# This software is issued under a joint BSD/GNU license. You may use the
# source code in this file under either license. However, note that the
# complete EMAN2 and SPARX software packages have some GPL dependencies,
# so you are responsible for compliance with the licenses of these packages
# if you opt to use BSD licensing. The warranty disclaimer below holds
# in either instance.
#
# This complete copyright notice must be included in any revised version of the
# source code. Additional authorship citations may be added, but existing
# author citations must be preserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
#
import global_def
from   global_def import *
import sys
from   optparse import OptionParser
import os
from   utilities import get_image
def main():

	arglist = []
	for arg in sys.argv:
		arglist.append( arg )

	progname = os.path.basename( arglist[0] )
	usage = progname + " prj_stack volume fsc_curve <mask> --CTF --snr=signal_noise_ratio --list=file --group=ID --sym=symmetry -verbose=(0|1) --MPI"
	parser = OptionParser(usage, version=SPARXVERSION)

	parser.add_option("--CTF",     action="store_true", default=False, help="perform ctf correction")
	parser.add_option("--snr",     type="float",        default=1.0,   help="Signal-to-Noise Ratio in the data" )
	parser.add_option("--sym",     type="string",       default="c1",  help="symmetry" )
	parser.add_option("--list",    type="string",                      help="file with list of images to be used in the first column" )
	parser.add_option("--group",   type="int",          default=-1,    help="perform reconstruction using images for a given group number (group is attribute in the header)" )
	parser.add_option("--MPI",     action="store_true", default=False, help="use MPI version ")
	parser.add_option("--npad",    type="int",	        default=2,     help="number of times padding (default 2)" )
	parser.add_option("--verbose", type="int",          default=0,     help="verbose level: 0 no, 1 yes" )
	(options,args) = parser.parse_args(arglist[1:])     


	if len(args) != 3 and len(args) != 4:
		print(usage)
		sys.exit(-1)

	prj_stack = args[0]
	vol_stack = args[1]
	fsc_curve = args[2]

	if len(args) == 3: mask = None
	else:              mask = get_image( args[3] )

	if options.MPI:
		from mpi import mpi_init
		sys.argv = mpi_init(len(sys.argv), sys.argv)
		
	if global_def.CACHE_DISABLE:
		from utilities import disable_bdb_cache
		disable_bdb_cache()

	if(options.list and options.group > -1):
		ERROR("options group and list cannot be used together","recon3d_n",1)
		sys.exit()

	from applications import recons3d_f

	global_def.BATCH = True
	recons3d_f(prj_stack, vol_stack, fsc_curve, mask, options.CTF, options.snr, options.sym, options.list, options.group, options.npad, options.verbose, options.MPI)
	global_def.BATCH = False
	
	if options.MPI:
		from mpi import mpi_finalize
		mpi_finalize()


if __name__ == "__main__":
	main()
