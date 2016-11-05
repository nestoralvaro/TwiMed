# BRAT tool configuration

# Basic configuration

To use the basic configuration the needed files are *annotation.conf* and *visual.conf*, which should be placed under *data/* folder in Brat tool.

These two files contain the possible values for the entities, attributes and relations that we used in our project.


# Concepts normalization

For the normalization the following two files are needed:
* Tools.conf which contains the normalization settings.
* Concepts.txt which contains the list of concepts with the unique identifiers.

The normalization configuration is explained in detail in this link: http://brat.nlplab.org/normalization.html

To start using the normalization in Brat:
* Put the file "Concepts.txt" in the folder that you want (e.g. in the folder "normalizationFiles/" under Brat root directory).
* Go to Brat root directory and run the following command:
python tools/norm_db_init.py normalizationFiles/Concepts.txt

If you don't have all the dependencies (i.e. Simstring http://chokkan.org/software/simstring/ ) the normalization configuration will fail. This is the part that I didn't manage to run in Mac OS.
