#!/usr/bin/env/python3

import sys
from os import path
from osgeo import gdal

def main(filename):
    process(filename)

def process(basename, form_values):
    input_file = path.join("./tmp", basename + ".tif")
    output_file = path.join("./tmp", basename + ".xml")
    options = make_options(form_values)
    translate(input_file,output_file,options)

def translate(input_file,output_file,options):
    ds = gdal.Open( input_file )
    translate_options = gdal.TranslateOptions( format = "PDS4", options = options )
    gdal.Translate( output_file, ds, options = translate_options )

def make_options(form):
    options = []
    for key, value in form.items():
        options.append('-co')
        options.append(key + '=' + value)
    return options

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))