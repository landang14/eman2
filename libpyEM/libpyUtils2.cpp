
// Boost Includes ==============================================================
#include <boost/python.hpp>
#include <boost/cstdint.hpp>

// Includes ====================================================================
#include <emdata.h>
#include <emutil.h>
#include <testutil.h>
#include <util.h>

// Using =======================================================================
using namespace boost::python;

// Declarations ================================================================
namespace  {

BOOST_PYTHON_FUNCTION_OVERLOADS(EMAN_Util_find_max_overloads_3_4, EMAN::Util::find_max, 3, 4)

BOOST_PYTHON_FUNCTION_OVERLOADS(EMAN_Util_find_min_and_max_overloads_4_6, EMAN::Util::find_min_and_max, 4, 6)

BOOST_PYTHON_FUNCTION_OVERLOADS(EMAN_EMUtil_get_imageio_overloads_2_3, EMAN::EMUtil::get_imageio, 2, 3)

BOOST_PYTHON_FUNCTION_OVERLOADS(EMAN_EMUtil_process_region_io_overloads_7_13, EMAN::EMUtil::process_region_io, 7, 13)


}// namespace 


// Module ======================================================================
BOOST_PYTHON_MODULE(libpyUtils2)
{
    class_< EMAN::Util >("Util", init<  >())
        .def(init< const EMAN::Util& >())
        .def("ap2ri", &EMAN::Util::ap2ri)
        .def("flip_complex_phase", &EMAN::Util::flip_complex_phase)
        .def("file_lock_wait", &EMAN::Util::file_lock_wait)
        .def("file_unlock", &EMAN::Util::file_unlock)
        .def("check_file_by_magic", &EMAN::Util::check_file_by_magic)
        .def("is_file_exist", &EMAN::Util::is_file_exist)
        .def("flip_image", &EMAN::Util::flip_image)
        .def("sstrncmp", &EMAN::Util::sstrncmp)
        .def("int2str", &EMAN::Util::int2str)
        .def("get_line_from_string", &EMAN::Util::get_line_from_string)
        .def("get_str_float", (bool (*)(const char*, const char*, float*))&EMAN::Util::get_str_float)
        .def("get_str_float", (bool (*)(const char*, const char*, float*, float*))&EMAN::Util::get_str_float)
        .def("get_str_float", (bool (*)(const char*, const char*, int*, float*, float*))&EMAN::Util::get_str_float)
        .def("get_str_int", (bool (*)(const char*, const char*, int*))&EMAN::Util::get_str_int)
        .def("get_str_int", (bool (*)(const char*, const char*, int*, int*))&EMAN::Util::get_str_int)
        .def("get_str_int", (bool (*)(const char*, const char*, int*, int*, int*))&EMAN::Util::get_str_int)
        .def("get_filename_by_ext", &EMAN::Util::get_filename_by_ext)
        .def("sbasename", &EMAN::Util::sbasename)
        .def("calc_least_square_fit", &EMAN::Util::calc_least_square_fit)
        .def("save_data", (void (*)(const std::vector<float,std::allocator<float> >&, const std::vector<float,std::allocator<float> >&, std::string))&EMAN::Util::save_data)
        .def("save_data", (void (*)(float, float, const std::vector<float,std::allocator<float> >&, std::string))&EMAN::Util::save_data)
        .def("save_data", (void (*)(float, float, float*, size_t, std::string))&EMAN::Util::save_data)
        .def("get_frand", (float (*)(int, int))&EMAN::Util::get_frand)
        .def("get_frand", (float (*)(float, float))&EMAN::Util::get_frand)
        .def("get_frand", (float (*)(double, double))&EMAN::Util::get_frand)
        .def("get_gauss_rand", &EMAN::Util::get_gauss_rand)
        .def("round", (int (*)(float))&EMAN::Util::round)
        .def("round", (int (*)(double))&EMAN::Util::round)
        .def("bilinear_interpolate", &EMAN::Util::bilinear_interpolate)
        .def("trilinear_interpolate", &EMAN::Util::trilinear_interpolate)
        .def("find_max", &EMAN::Util::find_max, EMAN_Util_find_max_overloads_3_4())
        .def("find_min_and_max", &EMAN::Util::find_min_and_max, EMAN_Util_find_min_and_max_overloads_4_6())
        .def("calc_best_fft_size", &EMAN::Util::calc_best_fft_size)
        .def("square", (int (*)(int))&EMAN::Util::square)
        .def("square", (float (*)(float))&EMAN::Util::square)
        .def("square", (float (*)(double))&EMAN::Util::square)
        .def("square_sum", &EMAN::Util::square_sum)
        .def("hypot3", (float (*)(int, int, int))&EMAN::Util::hypot3)
        .def("hypot3", (float (*)(float, float, float))&EMAN::Util::hypot3)
        .def("hypot3", (float (*)(double, double, double))&EMAN::Util::hypot3)
        .def("fast_floor", &EMAN::Util::fast_floor)
        .def("agauss", &EMAN::Util::agauss)
        .def("min", (int (*)(int, int))&EMAN::Util::min)
        .def("min", (int (*)(int, int, int))&EMAN::Util::min)
        .def("min", (float (*)(float, float))&EMAN::Util::min)
        .def("min", (float (*)(float, float, float))&EMAN::Util::min)
        .def("min", (float (*)(float, float, float, float))&EMAN::Util::min)
        .def("max", (float (*)(float, float))&EMAN::Util::max)
        .def("max", (float (*)(float, float, float))&EMAN::Util::max)
        .def("max", (float (*)(float, float, float, float))&EMAN::Util::max)
        .def("angle_sub_2pi", &EMAN::Util::angle_sub_2pi)
        .def("angle_sub_pi", &EMAN::Util::angle_sub_pi)
        .def("goodf", &EMAN::Util::goodf)
        .def("get_time_label", &EMAN::Util::get_time_label)
        .def("set_log_level", &EMAN::Util::set_log_level)
        .def("eman_copysign", &EMAN::Util::eman_copysign)
        .def("eman_erfc", &EMAN::Util::eman_erfc)
        .staticmethod("flip_complex_phase")
        .staticmethod("square")
        .staticmethod("int2str")
        .staticmethod("get_str_int")
        .staticmethod("calc_best_fft_size")
        .staticmethod("get_frand")
        .staticmethod("angle_sub_pi")
        .staticmethod("get_time_label")
        .staticmethod("trilinear_interpolate")
        .staticmethod("file_lock_wait")
        .staticmethod("min")
        .staticmethod("is_file_exist")
        .staticmethod("save_data")
        .staticmethod("set_log_level")
        .staticmethod("get_str_float")
        .staticmethod("angle_sub_2pi")
        .staticmethod("get_gauss_rand")
        .staticmethod("find_max")
        .staticmethod("max")
        .staticmethod("file_unlock")
        .staticmethod("fast_floor")
        .staticmethod("ap2ri")
        .staticmethod("sstrncmp")
        .staticmethod("check_file_by_magic")
        .staticmethod("agauss")
        .staticmethod("eman_erfc")
        .staticmethod("bilinear_interpolate")
        .staticmethod("calc_least_square_fit")
        .staticmethod("find_min_and_max")
        .staticmethod("get_filename_by_ext")
        .staticmethod("get_line_from_string")
        .staticmethod("square_sum")
        .staticmethod("goodf")
        .staticmethod("hypot3")
        .staticmethod("flip_image")
        .staticmethod("eman_copysign")
        .staticmethod("sbasename")
        .staticmethod("round")
    ;

    scope* EMAN_EMUtil_scope = new scope(
    class_< EMAN::EMUtil >("EMUtil", init<  >())
        .def(init< const EMAN::EMUtil& >())
        .def("vertical_acf", &EMAN::EMUtil::vertical_acf, return_value_policy< manage_new_object >())
        .def("make_image_median", &EMAN::EMUtil::make_image_median, return_value_policy< manage_new_object >())
        .def("get_image_ext_type", &EMAN::EMUtil::get_image_ext_type)
        .def("get_image_type", &EMAN::EMUtil::get_image_type)
        .def("get_image_count", &EMAN::EMUtil::get_image_count)
        .def("get_imageio", &EMAN::EMUtil::get_imageio, EMAN_EMUtil_get_imageio_overloads_2_3()[ return_internal_reference< 1 >() ])
        .def("get_imagetype_name", &EMAN::EMUtil::get_imagetype_name)
        .def("get_datatype_string", &EMAN::EMUtil::get_datatype_string)
        .def("process_region_io", &EMAN::EMUtil::process_region_io, EMAN_EMUtil_process_region_io_overloads_7_13())
        .def("dump_dict", &EMAN::EMUtil::dump_dict)
        .def("is_same_size", &EMAN::EMUtil::is_same_size)
        .def("is_same_ctf", &EMAN::EMUtil::is_same_ctf)
        .staticmethod("vertical_acf")
        .staticmethod("get_datatype_string")
        .staticmethod("dump_dict")
        .staticmethod("get_imageio")
        .staticmethod("get_image_count")
        .staticmethod("get_imagetype_name")
        .staticmethod("get_image_type")
        .staticmethod("is_same_size")
        .staticmethod("make_image_median")
        .staticmethod("process_region_io")
        .staticmethod("is_same_ctf")
        .staticmethod("get_image_ext_type")
    );

    enum_< EMAN::EMUtil::EMDataType >("EMDataType")
        .value("EM_SHORT_COMPLEX", EMAN::EMUtil::EM_SHORT_COMPLEX)
        .value("EM_SHORT", EMAN::EMUtil::EM_SHORT)
        .value("EM_UCHAR", EMAN::EMUtil::EM_UCHAR)
        .value("EM_FLOAT_COMPLEX", EMAN::EMUtil::EM_FLOAT_COMPLEX)
        .value("EM_CHAR", EMAN::EMUtil::EM_CHAR)
        .value("EM_INT", EMAN::EMUtil::EM_INT)
        .value("EM_USHORT", EMAN::EMUtil::EM_USHORT)
        .value("EM_USHORT_COMPLEX", EMAN::EMUtil::EM_USHORT_COMPLEX)
        .value("EM_UNKNOWN", EMAN::EMUtil::EM_UNKNOWN)
        .value("EM_UINT", EMAN::EMUtil::EM_UINT)
        .value("EM_DOUBLE", EMAN::EMUtil::EM_DOUBLE)
        .value("EM_FLOAT", EMAN::EMUtil::EM_FLOAT)
    ;


    enum_< EMAN::EMUtil::ImageType >("ImageType")
        .value("IMAGE_XPLOR", EMAN::EMUtil::IMAGE_XPLOR)
        .value("IMAGE_MRC", EMAN::EMUtil::IMAGE_MRC)
        .value("IMAGE_GATAN2", EMAN::EMUtil::IMAGE_GATAN2)
        .value("IMAGE_ICOS", EMAN::EMUtil::IMAGE_ICOS)
        .value("IMAGE_UNKNOWN", EMAN::EMUtil::IMAGE_UNKNOWN)
        .value("IMAGE_LST", EMAN::EMUtil::IMAGE_LST)
        .value("IMAGE_DM3", EMAN::EMUtil::IMAGE_DM3)
        .value("IMAGE_TIFF", EMAN::EMUtil::IMAGE_TIFF)
        .value("IMAGE_SAL", EMAN::EMUtil::IMAGE_SAL)
        .value("IMAGE_IMAGIC", EMAN::EMUtil::IMAGE_IMAGIC)
        .value("IMAGE_VTK", EMAN::EMUtil::IMAGE_VTK)
        .value("IMAGE_HDF", EMAN::EMUtil::IMAGE_HDF)
        .value("IMAGE_SPIDER", EMAN::EMUtil::IMAGE_SPIDER)
        .value("IMAGE_EMIM", EMAN::EMUtil::IMAGE_EMIM)
        .value("IMAGE_SINGLE_SPIDER", EMAN::EMUtil::IMAGE_SINGLE_SPIDER)
        .value("IMAGE_PNG", EMAN::EMUtil::IMAGE_PNG)
        .value("IMAGE_PGM", EMAN::EMUtil::IMAGE_PGM)
        .value("IMAGE_EM", EMAN::EMUtil::IMAGE_EM)
        .value("IMAGE_PIF", EMAN::EMUtil::IMAGE_PIF)
        .value("IMAGE_AMIRA", EMAN::EMUtil::IMAGE_AMIRA)
    ;

    delete EMAN_EMUtil_scope;

    class_< EMAN::ImageSort >("ImageSort", init< const EMAN::ImageSort& >())
        .def(init< int >())
        .def("sort", &EMAN::ImageSort::sort)
        .def("set", &EMAN::ImageSort::set)
        .def("get_index", &EMAN::ImageSort::get_index)
        .def("get_score", &EMAN::ImageSort::get_score)
        .def("size", &EMAN::ImageSort::size)
    ;

    class_< EMAN::TestUtil >("TestUtil", init<  >())
        .def(init< const EMAN::TestUtil& >())
        .def("get_debug_int", &EMAN::TestUtil::get_debug_int)
        .def("get_debug_float", &EMAN::TestUtil::get_debug_float)
        .def("get_debug_string", &EMAN::TestUtil::get_debug_string)
        .def("get_debug_image", &EMAN::TestUtil::get_debug_image)
        .def("to_emobject", &EMAN::TestUtil::to_emobject)
        .def("test_IntPoint", &EMAN::TestUtil::test_IntPoint)
        .def("test_FloatPoint", &EMAN::TestUtil::test_FloatPoint)
        .def("test_IntSize", &EMAN::TestUtil::test_IntSize)
        .def("test_FloatSize", &EMAN::TestUtil::test_FloatSize)
        .def("test_Vec3i", &EMAN::TestUtil::test_Vec3i)
        .def("test_Vec3f", &EMAN::TestUtil::test_Vec3f)
        .staticmethod("test_IntPoint")
        .staticmethod("test_Vec3f")
        .staticmethod("get_debug_string")
        .staticmethod("test_FloatPoint")
        .staticmethod("test_Vec3i")
        .staticmethod("test_IntSize")
        .staticmethod("test_FloatSize")
        .staticmethod("get_debug_int")
        .staticmethod("get_debug_float")
        .staticmethod("get_debug_image")
        .staticmethod("to_emobject")
    ;

}

