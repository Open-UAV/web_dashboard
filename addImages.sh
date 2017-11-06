#!/usr/bin/env bash
#This script adds all files in its current directory to the images stored on the AgDSS server.
#It takes one argument, which is the category for all the files that will be added
#
#SERVER="162.243.97.220"
SERVER="https://label.ag"
URL="/webclient/addImage"
echo "Category is $1"
if [ "$#" -lt 1 ]
then
    echo "Category is required"
    exit 1
fi
IMAGE_TYPES="{jpg, jpeg, png, bmp}"
shopt -s nullglob
for file in *.jpg *.jpeg *.png *.bmp; do
    echo "path=$(pwd)&image_name=$file&category=$1"
    curl --data "path=$(pwd)&image_name=$file&category=$1" "$SERVER$URL"
done
