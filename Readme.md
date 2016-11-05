# Organization

## Folders

We provide four different folders two of these folders (*gold* and *gold_conflated*) contains the annotations we curated. The remaining two folders contain tools or configuration files needed to visualize the annotations.

## *Gold* folder

This folder contains all the annotations we collected using Relaxed constraints and not conflating the data. The spans of the annotated entities correspond to the overlapping spans were the annotators agreed on the type of entity.
We annotated 3 different types of entities:
* Drug
* Symptom
* Disease
We annotated 3 types of relations between those entities:
* Reason-to-use
* Outcome-positive
* Outcome-negative
We allowed the annotation of 8 attributes in our entities.
* Polarity
* Person
* Modality
* Exemplification
* Duration
* Severity
* Status
* Sentiment


## *Gold_conflated* folder
This folder contains all the annotations we collected using Relaxed constraints and **conflating** the data. The spans of the annotated entities correspond to the overlapping spans were the annotators agreed on the conflated type of entity.
We annotated 2 different types of entities:
* Drug
* Disease_Symptom
We annotated 2 types of relations between those entities:
* Benefit
* Outcome-negative
We allowed the annotation of the same 8 attributes annotated in *gold* folder.


## *Tools_for_twitter* folder

Contains the needed tools to download and preprocess the messages from twitter. Once these messages are ready they should be placed into the corresponding folders within *gold* and *gold_conflated* directories.


## *Files_for_brat* folder

Contains the files needed to have Brat tool (http://brat.nlplab.org/) ready to use the annotations provided in *gold* and *gold_conflated* folders.