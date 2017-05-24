# Project

## Abstract
### Background
Work on pharmacovigilance systems using texts from PubMed and Twitter typically target at different elements and use different annotation guidelines resulting in a scenario where there is no comparable set of documents from both Twitter and PubMed annotated in the same manner.
### Objective
This study aimed to provide a comparable corpus of texts from PubMed and Twitter that can be used to study drug reports from these two sources of information, allowing researchers in the area of pharmacovigilance using natural language processing (NLP) to perform experiments to better understand the similarities and differences between drug reports in Twitter and PubMed.
### Methods
We produced a corpus comprising 1000 tweets and 1000 PubMed sentences selected using the same strategy and annotated at entity level by the same experts (pharmacists) using the same set of guidelines.
Results: The resulting corpus, annotated by two pharmacists, comprises semantically correct annotations for a set of drugs, diseases, and symptoms. This corpus contains the annotations for 3144 entities, 2749 relations, and 5003 attributes.
### Conclusions
We present a corpus that is unique in its characteristics as this is the first corpus for pharmacovigilance curated from Twitter messages and PubMed sentences using the same data selection and annotation strategies. We believe this corpus will be of particular interest for researchers willing to compare results from pharmacovigilance systems (eg, classifiers and named entity recognition systems) when using data from Twitter and from PubMed. We hope that given the comprehensive set of drug names and the annotated entities and relations, this corpus becomes a standard resource to compare results from different pharmacovigilance studies in the area of NLP.

## Citation 
Please cite as:
<br/>
Alvaro N, Miyao Y, Collier N
<br/>
TwiMed: Twitter and PubMed Comparable Corpus of Drugs, Diseases, Symptoms, and Their Relations
<br/>
JMIR Public Health Surveill 2017;3(2):e24
<br/>
DOI: [10.2196/publichealth.6396](http://doi.org/10.2196/publichealth.6396)
<br/>
PMID: [28468748](http://www.ncbi.nlm.nih.gov/pubmed/28468748)



## Organization

We provide four different folders two of these folders (*gold* and *gold_conflated*) contains the annotations we curated. The remaining two folders contain tools or configuration files needed to visualize the annotations.

### *Gold* folder

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


### *Gold_conflated* folder

This folder contains all the annotations we collected using Relaxed constraints and **conflating** the data. The spans of the annotated entities correspond to the overlapping spans were the annotators agreed on the conflated type of entity.
We annotated 2 different types of entities:
* Drug
* Disease_Symptom
We annotated 2 types of relations between those entities:
* Benefit
* Outcome-negative
We allowed the annotation of the same 8 attributes annotated in *gold* folder.


### *Tools_for_twitter* folder

Contains the needed tools to download and preprocess the messages from twitter. Once these messages are ready they should be placed into the corresponding folders within *gold* and *gold_conflated* directories.


### *Files_for_brat* folder

Contains the files needed to have Brat tool (http://brat.nlplab.org/) ready to use the annotations provided in *gold* and *gold_conflated* folders.
