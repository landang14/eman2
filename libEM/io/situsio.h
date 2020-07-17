/*
 * Author: Grant Tang, 06/07/2011 (gtang@bcm.edu)
 * Copyright (c) 2000-2006 Baylor College of Medicine
 *
 * This software is issued under a joint BSD/GNU license. You may use the
 * source code in this file under either license. However, note that the
 * complete EMAN2 and SPARX software packages have some GPL dependencies,
 * so you are responsible for compliance with the licenses of these packages
 * if you opt to use BSD licensing. The warranty disclaimer below holds
 * in either instance.
 *
 * This complete copyright notice must be included in any revised version of the
 * source code. Additional authorship citations may be added, but existing
 * author citations must be preserved.
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
 *
 * */

#ifndef eman__situsio_h__
#define eman__situsio_h__ 1

#include "imageio.h"

namespace EMAN
{
	/**situs is a a Situs-specific format on a cubic lattice. This allows Situs programs
	 * to keep track of coordinate systems and it makes the core Situs programs
	 * independent of the ever changing map format standards. In the editable
	 * (ASCII or text) Situs format, a short header holds the voxel spacing WIDTH,
	 * the map origin as defined by the 3D coordinates of the first voxel ORIGX, ORIGY, ORIGZ,
	 * and the map dimensions (number of increments) NX, NY, NZ. This minimalist header
	 * is followed by the data fields such that x increments change fastest and z increments change slowest.
	 * http://situs.biomachina.org/fguide.html#map2map
	 * */
	class SitusIO : public ImageIO
	{
	public:
		explicit SitusIO(const string & fname, IOMode rw_mode = READ_ONLY);
		~SitusIO();

		DEFINE_IMAGEIO_FUNC;

		static bool is_valid(const void *first_block);

	private:
		IOMode rw_mode;
		FILE *situsfile;

		bool initialized;
		bool is_new_file;

		float apix, origx, origy, origz;
		int nx, ny, nz;

		static const int SITUS_HEADER_LINES;
		static const int FLOAT_SIZE;
		static const int NFLOAT_PER_LINE;
		static const char * OUTFORMAT;
		static const int LINE_LENGTH;	//10 number per line, echo take 11 character space
	};


}

#endif	//eman__situsio_h__
