#!/bin/bash

read -p "Introduce el directorio donde buscar las imágenes: " DIRECTORIO

read -p "Introduce el hash MD5 objetivo: " HASH_OBJETIVO

for archivo in "$DIRECTORIO"/*; do

    hash_actual=$(md5sum "$archivo" | awk '{print $1}')

    if [ "$hash_actual" == "$HASH_OBJETIVO" ]; then
        echo "El archivo con el hash es: $archivo"
        break
    fi

done
