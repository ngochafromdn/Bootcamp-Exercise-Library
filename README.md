# Bootcamp-Exercise-Library

Introduction about the bootcamp-exercise-library

This is a package for converting files to png, includes png, heic, tiff, pdf. The main repo includes the following main functions/classes:

- converter.py: the main file for converting files to png
- test_myconverter.py: the unittest file for converter.py
- setup.py: the setup file for the package
- README.md: the readme file for the package
- LICENSE: the license file for the package



How to use :

- Install the package: pip install File-Converter-to-image
- Import the package: from myconverter.converter import MyConverter
- Create an instance of MyConverter class: cvt = MyConverter(input_file_path, output_file_path)
- Call the convert() method: cvt.convert()

### Create Anaconda environment

```
conda env create -f environment.yml
conda activate cinna-lab2
```

### Define pakage

```
python -m pip install -e . 
```

### Run unit tests
Run the following command:

```
python test/test_myconverter.py
```

### Unit test result
<img src="images/result.jpg">

