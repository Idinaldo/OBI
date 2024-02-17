#include <cs50.h>
#include <stdio.h>

typedef struct
{
    int tamanho;
    char lado;
} DTBotas;


int calculaPares(DTBotas array[], int len);

int main(void)
{

    int qtd_botas = get_int("");
    DTbotas botas[qtd_botas+10];

    for (int i = 0; i < qtd_botas; i++)
    {
        int tamanho_bota;
        char space, lado_bota;
        scanf("%d%c%c", tamanho_bota, space, lado_bota);

        botas[i].tamanho = tamanho_bota;
        botas[i].lado = lado_bota;
    }

    int pares = calculaPares(botas, qtd_botas);
    printf("%i\n", pares);

    return 0;
}

int calculaPares(DTBotas array[], int len)
{

    int qtd_pares;
    for (int i = 0; i < len; i++)
    {
        for (int j = 0; j < len; j++)
        {
            if (array[i].tamanho == array[j].tamanho)
            {
                if (array[i].lado != array[j].lado)
                {
                    qtd_pares++;
                    break;
                }
            }
        }
    }

    return qtd_pares;
}