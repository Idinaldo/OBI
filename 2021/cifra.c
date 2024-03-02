#include <stdio.h>
#include <string.h>

int isVowel(char letter);
void consonant(char letter);
void nearestVowel(char letter);

char vowels[] = {'a', 'e', 'i', 'o', 'u'};
char nova_palavra[120];
int position = 0;

int main()
{
    char palavra[30];

    int pos = 0;
    while (scanf("%s", &palavra) != -1){};

    int len = strlen(palavra);
    for (int i = 0; i < len; i++)
    {
        if (isVowel(palavra[i]) == 0)
            consonant(palavra[i]);
        else
        {
            nova_palavra[position] = palavra[i];
            position++;
        }
    }

    len = strlen(nova_palavra);
    for (int i = 0; i < len; i++)
    {
        printf("%c", nova_palavra[i]);
    }
    printf("\n");

}

int isVowel(char letter)
{
    int ascii_vowels[] = {97, 101, 105, 111, 117};
    for (int i = 0; i < 5; i++)
    {
        if (letter == ascii_vowels[i])
            return 1;
    }
    return 0;
}

void consonant(char letter)
{
    nova_palavra[position] = letter;
    position++;

    nearestVowel(letter);
    position++;

    int next_letter = letter;
    if (letter != 'z')
        next_letter++;

    char letra = next_letter;

    while (isVowel(letra) == 1)
        letra++;

    nova_palavra[position] = letra;
    position++;
}

void nearestVowel(char letter)
{
    int smallest;
    int change = 0;
    int ascii_letter = letter;
    int distances[] = {ascii_letter - 97, ascii_letter - 101, ascii_letter - 105,
    ascii_letter - 111, ascii_letter - 117};

    for (int i = 0; i < 5; i++)
    {
        if (distances[i] < 0)
            distances[i] *= -1;

        if (i == 0)
            smallest = distances[i];

        else if (smallest > distances[i])
        {
            smallest = distances[i];
            change = i;
        }
    }
    nova_palavra[position] = vowels[change];
}
