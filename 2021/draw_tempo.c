#include <stdio.h>
#include <string.h>

typedef struct
{
    int time = 0;
    char answered = 'f';
} friend;

typedef struct
{
    int friend_ID;
    char registro;
} regis;


void treat_register(char reg, int x);
void increase_time(int increaser);

regis registers[30];
friend data_array[150];
int current_position = 0;

int main()
{
    int registers_count;
    
    for (int i = 0; i < registers_count; i++)
    {
        int integer_x;
        char register_type;
        
        scanf("%i%c", &register_type, &integer_x);
        treat_register(register_type, integer_x);
        
        
        current_position++;
    }
    
    
    
    return 0;
}




void treat_register(char reg, int x)
{
    registers[current_position] = reg;
    
    if (strcmp(reg, 'T') == 0)
        increase_time(x);
    
    else if (strcmp(reg, 'R') == 0)
        data.array[current_position].answered = 'f';
    
    else if (strcmp(reg, 'E') == 0)
        data.array[current_position].answered = 't';
}

void increase_time(int increaser)
{
    for (int i = 0; i < current_position; i++)
    {
        if (strcmp(data_array[current_position].answered, 'f') == 0)
            data_array[current_position].time += increaser;
    }
}

void verify_RE()
{
    
}



