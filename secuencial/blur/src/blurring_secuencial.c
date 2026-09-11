// se corre:
// ./blurring_secuencial ../../../data/blur/pequena.bmp ../../../data/blur/salida_sec_pequena.bmp


#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    // Ruta de entrada y salida configurables por línea de comandos, para
    // poder probar las 3 imágenes (pequeña/mediana/grande) de data/blur/
    // sin recompilar. Si no se pasan argumentos, se usan estos valores
    // por defecto:
    const char *ruta_entrada = "../../../data/blur/pequena.bmp";
    const char *ruta_salida  = "../../../data/blur/resultado_blur.bmp";

    if (argc >= 2) ruta_entrada = argv[1];
    if (argc >= 3) ruta_salida  = argv[2];

    // abrir imagen original y preparar la de salida
    FILE *archivo_entrada = fopen(ruta_entrada, "rb");
    FILE *archivo_salida = fopen(ruta_salida, "wb");

    if (!archivo_entrada || !archivo_salida) {
        printf("Error al abrir los archivos. Verifica la ruta: %s\n", ruta_entrada);
        return 1;
    }

    // cabecera del archivo BMP (54 bytes: file header + info header)
    unsigned char cabecera[54];
    fread(cabecera, sizeof(unsigned char), 54, archivo_entrada);
    fwrite(cabecera, sizeof(unsigned char), 54, archivo_salida);

    // leer dimensiones de la imagen desde la cabecera
    int ancho = *(int*)&cabecera[18];
    int alto = *(int*)&cabecera[22];
    if (alto < 0) alto = -alto;

    // Matrices de ENTRADA: la imagen original tal cual se lee del archivo
    unsigned char **rojo = malloc(alto * sizeof(unsigned char*));
    unsigned char **verde = malloc(alto * sizeof(unsigned char*));
    unsigned char **azul = malloc(alto * sizeof(unsigned char*));

    // Matrices de SALIDA: resultado del blur, separadas de las de entrada
    unsigned char **rojo_out = malloc(alto * sizeof(unsigned char*));
    unsigned char **verde_out = malloc(alto * sizeof(unsigned char*));
    unsigned char **azul_out = malloc(alto * sizeof(unsigned char*));

    for (int i = 0; i < alto; i++) {
        rojo[i] = malloc(ancho);
        verde[i] = malloc(ancho);
        azul[i] = malloc(ancho);
        rojo_out[i] = malloc(ancho);
        verde_out[i] = malloc(ancho);
        azul_out[i] = malloc(ancho);
    }

    int padding = (4 - (ancho * 3) % 4) % 4;

    // cargar los pixeles reales a las matrices
    for (int y = 0; y < alto; y++) {
        for (int x = 0; x < ancho; x++) {
            azul[y][x] = fgetc(archivo_entrada);
            verde[y][x] = fgetc(archivo_entrada);
            rojo[y][x] = fgetc(archivo_entrada);
        }
        // ignorar los bytes de relleno al final de cada fila (si los hay)
        fseek(archivo_entrada, padding, SEEK_CUR);
    }

    // Aplicar blurring (3x3), fila por fila, en orden secuencial
    for (int y = 0; y < alto; y++) {
        for (int x = 0; x < ancho; x++) {

            // bordes de la imagen se quedan igual
            if (y == 0 || y == alto - 1 || x == 0 || x == ancho - 1) {
                azul_out[y][x] = azul[y][x];
                verde_out[y][x] = verde[y][x];
                rojo_out[y][x] = rojo[y][x];
                continue;
            }

            int sumaR = 0, sumaG = 0, sumaB = 0;

            for (int dy = -1; dy <= 1; dy++) {
                for (int dx = -1; dx <= 1; dx++) {
                    sumaR += rojo[y + dy][x + dx];
                    sumaG += verde[y + dy][x + dx];
                    sumaB += azul[y + dy][x + dx];
                }
            }

            // promedio resultante
            rojo_out[y][x]  = sumaR / 9;
            verde_out[y][x] = sumaG / 9;
            azul_out[y][x]  = sumaB / 9;
        }
    }

    // escribir la imagen de salida
    for (int y = 0; y < alto; y++) {
        for (int x = 0; x < ancho; x++) {
            fputc(azul_out[y][x], archivo_salida);
            fputc(verde_out[y][x], archivo_salida);
            fputc(rojo_out[y][x], archivo_salida);
        }
        for (int p = 0; p < padding; p++) {
            fputc(0, archivo_salida);
        }
    }

    // liberar memoria
    for (int i = 0; i < alto; i++) {
        free(rojo[i]); free(verde[i]); free(azul[i]);
        free(rojo_out[i]); free(verde_out[i]); free(azul_out[i]);
    }
    free(rojo); free(verde); free(azul);
    free(rojo_out); free(verde_out); free(azul_out);

    fclose(archivo_entrada);
    fclose(archivo_salida);

    printf("Imagen desenfocada con exito (version secuencial)!\n");
    return 0;
}