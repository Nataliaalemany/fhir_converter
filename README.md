<div align="center">
    
# FHIR converter
    
</div>


## Table of Contents
- [Description](#Description)
- [Technology used](#TechnologyUsed)
- [Run](#Run)
- [Information](#Information)

## Description
This repository contains a REST API endpoint that receives an input JSON and maps it to a different output JSON with the parameters according to output_description.json

## Technology used
Python 3.10<br>

## Run
``` sh
https://github.com/Nataliaalemany/fhir_converter.git
```

Copy the link above and clone it onto your computer using Git Bash.<br>
After the repository is successfully cloned, open it in your prefered IDE (e.g. pycharm, vscode).<br>
Start the program, then go to postman and use the following port to add and convert HL7 FHIR files:<br>
``` sh
http://127.0.0.1:5000/data
``` 

## Information
If your HL7 FHIR file has multiple measurement values, measurement units, or performers, the API will only collect the first one given.<br>
Measurement units in centimeters will be converted to meters.<br>
Observation type "Hgb, blood gas" will be given in g/dL.<br>
Measurement coding only includes items that have system: "http://loinc.org". 
