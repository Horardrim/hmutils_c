#ifndef VERSION_H
#define VERSION_H

#include <stdio.h>

#define HMUTILS_C_VERSION "1.0.0"

void show_version();
{
    printf("hmtuils-c library version:\n");
    printf("%s:\n", HMUTILS_C_VERSION);
}

#endif
