#include <chrono>
#include <iomanip>
#include <iostream>
#include <stdexcept>
#include <string>

namespace {

constexpr long long kNPorDefecto = 1'000'000;
constexpr double kLimiteInferior = 0.0;
constexpr double kLimiteSuperior = 1.0;

double funcion(const double x) {
    return x * x;
}

bool leer_subdivisiones(const int argc, char* argv[], long long& n) {
    if (argc > 2) {
        std::cerr << "Error: uso esperado: " << argv[0] << " [N]" << std::endl;
        return false;
    }

    if (argc == 1) {
        n = kNPorDefecto;
        return true;
    }

    try {
        std::size_t caracteres_leidos = 0;
        n = std::stoll(argv[1], &caracteres_leidos);

        if (caracteres_leidos != std::string(argv[1]).size()) {
            throw std::invalid_argument("caracteres adicionales");
        }
    } catch (const std::invalid_argument&) {
        std::cerr << "Error: N debe ser un numero entero positivo." << std::endl;
        return false;
    } catch (const std::out_of_range&) {
        std::cerr << "Error: N esta fuera del rango permitido." << std::endl;
        return false;
    }

    if (n <= 0) {
        std::cerr << "Error: N debe ser mayor que cero." << std::endl;
        return false;
    }

    return true;
}

}  // namespace

int main(int argc, char* argv[]) {
    long long n = 0;
    if (!leer_subdivisiones(argc, argv, n)) {
        return 1;
    }

    const double dx = (kLimiteSuperior - kLimiteInferior) /
                      static_cast<double>(n);
    double suma = 0.0;

    const auto inicio = std::chrono::steady_clock::now();

    for (long long i = 0; i < n; ++i) {
        const double x = kLimiteInferior +
                         (static_cast<double>(i) + 0.5) * dx;
        suma += funcion(x);
    }

    const double resultado = suma * dx;
    const auto fin = std::chrono::steady_clock::now();
    const std::chrono::duration<double> duracion = fin - inicio;

    std::cout << std::setprecision(15)
              << "Metodo: Secuencial\n"
              << "N: " << n << '\n'
              << "Intervalo: [" << kLimiteInferior << ", "
              << kLimiteSuperior << "]\n"
              << "Resultado: " << resultado << '\n'
              << "Tiempo: " << duracion.count() << " s" << std::endl;

    return 0;
}
