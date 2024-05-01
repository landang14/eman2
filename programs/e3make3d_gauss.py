#!/usr/bin/env python
#
# Author: Steven Ludtke  4/28/2024
# Copyright (c) 2023- Baylor College of Medicine
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
# Foundation, Inc., 59 Temple Place, Suite 330, Boston MA 02111-1307 USA
#

from EMAN3 import *
from EMAN3tensor import *
import numpy as np
import sys

def main():

	usage="""e3make3d_gauss.py <projections>


	"""
	parser = EMArgumentParser(usage=usage,version=EMANVERSION)
	parser.add_argument("--volout", type=str,help="Volume output file", default=None)
	parser.add_argument("--gaussout", type=str,help="Gaussian list output file",default="gauss.txt")
	parser.add_argument("--volfilt", type=float, help="Lowpass filter to apply to output volume, absolute, Nyquist=0.5", default=0.3)
	parser.add_argument("--initgauss",type=int,help="Gaussians in the first pass, scaled with stage, default=250", default=250)

	parser.add_argument("--gpudev",type=int,help="GPU Device, default 0", default=0)
	parser.add_argument("--gpuram",type=int,help="Maximum GPU ram to allocate in MB, default=4096", default=4096)
	parser.add_argument("--verbose", "-v", dest="verbose", action="store", metavar="n", type=int, default=0, help="verbose level [0-9], higher number means higher level of verbosity")

	(options, args) = parser.parse_args()
	tf_set_device(dev=0,maxmem=options.gpuram)

	pid=E3init(sys.argv)

	nptcl=EMUtil.get_image_count(args[0])
	nx=EMData(args[0],0,True)["nx"]


	# stage 1 - limit to ~1000 particles for initial low resolution work
	ptcls=EMStack2D(EMData.read_images(args[0],range(0,nptcl,max(1,nptcl//1000))))
	orts,txty=ptcls.orientations
	ptclsf=ptcls.do_fft()

	# stage 1, heavy downsampling
	ptclsfds=ptcls.downsample(16)    # downsample specifies the final size, not the amount of downsampling
	ny=ptclsfds.shape[1]

	gaus=Gaussians()
	#Initialize Gaussians to random values with amplitudes over a narrow range
	rnd=tf.random.uniform((options.initgauss,4))     # specify the number of Gaussians to start with here
	rnd+=(-.5,-.5,-.5,100.0)
	gaus._data=rnd/(1.5,1.5,1.5,100.0)

	for i in range(32):
		qual,shift,sca=gradient_step(gaus,ptclsfds,orts,txty,1.5)
		print(f"{qual}\t{shift}\t{sca}")

	# vol=gaus.volume(map1["nx"])
	# vol.emdata[0].process_inplace("filter.lowpass.gauss",{"cutoff_abs":0.3})
	# vol.write_images("A_vol_opt_1.hdf")


	E3end(pid)

@tf.function
def gradient_step(gaus,ptclsfds,orts,tytx,weight=1.0):
	"""Takes one gradient step on the Gaussian coordinates given a set of particle FFTs at the appropriate scale,
	computing FRC to axial Nyquist, with specified linear weighting factor (def 1.0). Linear weight goes from
	0-2. 1 is unweighted, >1 upweights low resolution, <1 upweights high resolution"""
	ny=ptclsfds.shape[1]
	with tf.GradientTape() as gt:
		gt.watch(gaus.tensor)
		projs=gaus.project_simple(orts,ny,tytx=tytx)
		projsf=projs.do_fft()
		frcs=tf_frc(projsf.tensor,ptclsfds.tensor,ny/2,weight)	# specifying ny/2 radius explicitly so weight functions

	grad=gt.gradient(frcs,gaus._data)
	qual=tf.math.reduce_mean(frcs)			# this is the average over all projections, not the average over frequency
	shift=tf.math.reduce_std(grad[:,:3])	# translational std
	sca=tf.math.reduce_std(grad[:,3])		# amplitude std
	xyzs=1.0/(shift*1000)   				# xyz scale factor, 1000 heuristic, TODO: may change
	gaus.add_tensor(grad*(xyzs,xyzs,xyzs,1.0/(sca*500)))	# amplitude scale, 500 heuristic, TODO: may change

	return (float(qual),float(shift),float(sca))
#	print(f"{i}) {float(qual)}\t{float(shift)}\t{float(sca)}")


if __name__ == '__main__':
	main()
