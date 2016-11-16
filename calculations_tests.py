from calcuations import cubic_volume, cuboid_volume
from calcuations import pyrimidal_volume,spherical_volume, conical_volume, cylindrical_volume, prism_volume
from numpy.testing import assert_allclose

def test_volume_cube():
    print("cubic_volume")
    print(cubic_volume(2))
    assert cubic_volume(2) == 8

def test_volume_pyramid():
    print("%s != %s" % (pyrimidal_volume(3,1), 1,))
    assert pyrimidal_volume(6,10) == 20

def test_volume_sphere():
    assert_allclose (actual=spherical_volume (1),desired=4.19, rtol=1e-3)
    assert_allclose(actual=spherical_volume(3), desired=113.09, rtol=1e-3)


def test_volume_cone():
    assert_allclose(actual=conical_volume(1), desired=1.04, rtol=1e-2)


def test_volume_cylinder():
    not assert_allclose(actual=cylindrical_volume(1, 1), desired=3.14, rtol=1e-2)

def test_volume_prism():
    assert prism_volume(2, 2) == 4

def test_cuboid_volume():
    assert cuboid_volume(1, 1, 1) == 1



