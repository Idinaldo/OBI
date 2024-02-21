#include <stdio.h>

int main(void)
{
    int qtd_posicoes, pos_disco, pos_aviao;
    scanf("%d%d%d", &qtd_posicoes, &pos_disco, &pos_aviao);

    int qtd_movs = 0;

    if (pos_disco < pos_aviao)
    {
        qtd_movs = (qtd_posicoes - pos_aviao) + pos_disco;
    }

    else
    {
        qtd_movs = pos_disco - pos_aviao;
    }

    printf("%d\n", qtd_movs);
}
