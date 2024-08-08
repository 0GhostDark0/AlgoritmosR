import math

def rectangular_to_cylindrical(x, y, z):
    """
    Convierte coordenadas rectangulares (x, y, z) a cilíndricas (r, theta, z)
    """
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    return r, theta, z

def rectangular_to_spherical(x, y, z):
    """
    Convierte coordenadas rectangulares (x, y, z) a esféricas (r, theta, phi)
    """
    r = math.sqrt(x**2 + y**2 + z**2)
    theta = math.atan2(y, x)
    phi = math.acos(z / r)
    return r, theta, phi

# Coordenadas rectangulares de ejemplo
x = 3
y = 4
z = 5

# Convertir a coordenadas cilíndricas
r_cyl, theta_cyl, z_cyl = rectangular_to_cylindrical(x, y, z)
print(f"Coordenadas cilíndricas: r={r_cyl:.2f}, theta={theta_cyl:.2f} rad, z={z_cyl:.2f}")

# Convertir a coordenadas esféricas
r_sph, theta_sph, phi_sph = rectangular_to_spherical(x, y, z)
print(f"Coordenadas esféricas: r={r_sph:.2f}, theta={theta_sph:.2f} rad, phi={phi_sph:.2f} rad")