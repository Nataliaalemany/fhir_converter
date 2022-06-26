import datetime


def convert(input_json):
    entry = []
    for data in input_json["entry"]:
        if "resource" in data:
            entry_dictionary = {}
            resource = data["resource"]
            entry_dictionary["observationId"] = get_observation_id(resource)
            entry_dictionary["patientId"] = get_patient_id(resource)
            entry_dictionary["performerId"] = get_performer_id(resource)
            entry_dictionary["measurementCoding"] = get_measurement_coding(resource)
            entry_dictionary["measurementValue"] = get_measurement_value(resource)
            entry_dictionary["measurementUnit"] = get_measurement_unit(resource)
            entry_dictionary["measurementDate"] = get_measurement_date(resource)
            entry_dictionary["dataFetched"] = data_fetch_date()
            entry.append(entry_dictionary)
    return entry


def get_observation_id(resource):
    if "id" in resource:
        return resource["id"]
    else:
        return "N/A"


def get_patient_id(resource):
    if "subject" in resource \
            and "reference" in resource["subject"]:
        patient = resource["subject"]["reference"]
        patient_id = patient.split("Patient/")
        return patient_id[1]
    else:
        return "N/A"


def get_performer_id(resource):
    if "performer" in resource:
        for practitioner in resource["performer"]:
            performer = practitioner["reference"]
            performer_id = performer.split("Practitioner/")
            return performer_id[1]
    else:
        return "N/A"


def get_measurement_coding(resource):
    coding = []
    coding_dictionary = {}
    if "code" in resource and "coding" in resource["code"]:
        for data in resource["code"]["coding"]:
            if "system" in data and data["system"] == "http://loinc.org":
                coding_dictionary["system"] = data["system"]
                if "code" in data:
                    coding_dictionary["code"] = data["code"]
                if "display" in data:
                    coding_dictionary["display"] = data["display"]
                coding.append(coding_dictionary)
    return coding


def get_measurement_value(resource):
    if "component" in resource:
        for value in resource["component"]:
            if "valueQuantity" in value \
                    and "value" in value["valueQuantity"]:
                return convert_cm_to_m(value)
    elif "valueQuantity" in resource and "value" in resource["valueQuantity"]:
        return convert_cm_to_m(resource)
    else:
        return "N/A"


def convert_cm_to_m(component):
    if "unit" in component["valueQuantity"] and component["valueQuantity"]["unit"] == "cm":
        component["valueQuantity"]["value"] = round(component["valueQuantity"]["value"] / 100, 3)
    return component["valueQuantity"]["value"]


def get_measurement_unit(resource):
    if "component" in resource:
        for unit in resource["component"]:
            if "valueQuantity" in unit:
                return convert_unit(unit)
    elif "valueQuantity" in resource:
        return convert_unit(resource)
    else:
        return "N/A"


def convert_unit(component):
    if "unit" in component["valueQuantity"] and component["valueQuantity"]["unit"] == "cm":
        return "m"
    elif "unit" in component["valueQuantity"]:
        if component["valueQuantity"]["unit"] == "g/dl":
            return "g/dL"
        return component["valueQuantity"]["unit"]
    elif "code" in component \
            and "text" in component["code"] \
            and component["code"]["text"] == "Hgb, blood gas":
        return "g/dL"
    return "N/A"


def get_measurement_date(resource):
    if "effectiveDateTime" in resource:
        return resource["effectiveDateTime"]
    else:
        return "N/A"


def data_fetch_date():
    output_date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    return output_date
